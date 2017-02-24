# -*- coding: utf-8 -*-
from django.views.generic import UpdateView, DeleteView
from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage,PageNotAnInteger
from django.core.urlresolvers import reverse


from ..models import Group
from ..util import paginate


# Views for Groups
def groups_list(request):
    groups = Group.objects.all()

    # try to order groups list
    order_by = request.GET.get('order_by', '')
    if order_by in ('title',):
        groups = groups.order_by(order_by)
        if request.GET.get('reverse', '') == '1':
            groups = groups.reverse()

    # apply pagination, 2 groups per page
    context = paginate(groups, 2, request, {}, var_name='groups')

    return render(request, 'students/groups_list.html', context)
def groups_add(request):
    return HttpResponse('<h1>Group Add Form</h1>')

class GroupUpdateView(UpdateView):
    model = Group
    template_name = "students/groups_edit.html"
    def get_success_url(self):
        return u'%s?status_message=Групу успішно збережено!' % reverse('groups')
    def post(self, request, *args, **kwargs):
        if request.POST.get('cancel_button'):
            return HttpResponseRedirect(u'%s?status_message=Редагування групи відмінено!'% reverse('groups'))
        else:
            return super(GroupUpdateView, self).post(request, *args, **kwargs)


class GroupDeleteView(DeleteView):
    model = Group
    template_name = 'students/groups_delete.html'
    def get_success_url(self):
        return u'%s?status_message=Групу успішно видалено!'% reverse('groups')
