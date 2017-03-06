# -*- coding: utf-8 -*-
from django.views.generic import UpdateView, DeleteView, CreateView
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from datetime import datetime
from django.contrib import messages
from django.utils.translation import ugettext as _
from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Field
from crispy_forms.bootstrap import FormActions
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from ..util import paginate, get_current_group
from ..models import Student, Group

# Create your views here.
def students_list(request):
    current_group = get_current_group(request)
    if current_group:
        students = Student.objects.filter(student_group=current_group)
    else:
        # otherwise show all students
        students = Student.objects.all()
        # try to order students list
        order_by = request.GET.get('order_by', '')
        if order_by in ('last_name', 'first_name', 'ticket'):
            students = students.order_by(order_by)
            if request.GET.get('reverse', '') == '1':
                students = students.reverse()
    return render(request, 'students/students_list.html',
{'students': students})

class StudentForm(ModelForm):
    class Meta:
        model = Student
    def __init__(self, *args, **kwargs):

        super(StudentForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        # set form tag attributes
        self.helper.form_method = 'POST'
        self.helper.form_class = 'form-horizontal'

            # set form field properties
        self.helper.help_text_inline = True
        self.helper.html5_required = True
        self.helper.label_class = 'col-sm-2 control-label'
        self.helper.field_class = 'col-sm-10'
            # add buttons
        self.helper.layout[-1] = FormActions(
        Submit('add_button', u'Зберегти',css_class="btn btn-primary"),
        Submit('cancel_button', u'Скасувати', css_class="btn btn-link"),
          )


class StudentUpdateForm(StudentForm):
    class Meta:
        model = Student
    def __init__(self, *args, **kwargs):
        super(StudentUpdateForm, self).__init__(*args, **kwargs)
        self.helper.form_action = reverse('students_edit',kwargs={'pk': kwargs['instance'].id})



class StudentCreateView(CreateView):
    model = Student
    template_name = "students/students_add.html"
    form_class = StudentForm
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(StudentCreateView, self).dispatch(*args, **kwargs)
    def get_success_url(self):
        return u'%s?status_message=Студента успішно збережено!' % reverse('home')

    def post(self, request, *args, **kwargs):
        if 'cancel_button' in request.POST:
            return HttpResponseRedirect(u'%s?status_message=Додавання студента відмінено!'% reverse('home'))
        else:
            return super(StudentCreateView, self).post(request, *args, **kwargs)


class StudentUpdateView(UpdateView):
    model = Student
    template_name = "students/students_edit.html"
    form_class = StudentUpdateForm
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(StudentUpdateView, self).dispatch(*args, **kwargs)

    def get_success_url(self):
        return u'%s?status_message=Студента успішно збережено!' % reverse('home')
    def post(self, request, *args, **kwargs):
        if request.POST.get('cancel_button'):
            return HttpResponseRedirect(u'%s?status_message=Редагування студента відмінено!'% reverse('home'))
        else:
            return super(StudentUpdateView, self).post(request, *args, **kwargs)

class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'students/students_delete.html'
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(StudentUpdateView, self).dispatch(*args, **kwargs)
    def get_success_url(self):
        return u'%s?status_message=Студента успішно видалено!'% reverse('home')
