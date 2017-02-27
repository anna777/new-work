# -*- coding: utf-8 -*-
from django.contrib import admin
from django.core.urlresolvers import reverse
from django.forms import ModelForm, ValidationError

from .models import Student, Group, Exam
from django.contrib.admin import RelatedFieldListFilter

class RelatedOnlyFieldListFilter(RelatedFieldListFilter):
    # class getting all leaders in group's filter
    def __init__(self, field, request, params, model, model_admin, field_path):
        super(RelatedOnlyFieldListFilter, self).__init__(
            field, request, params, model, model_admin, field_path)
        qs = field.related_field.model.objects.filter(
            id__in=model_admin.get_queryset(request).values_list(
                field.name, flat=True).distinct())
        self.lookup_choices = [(each.id, unicode(each)) for each in qs]

class StudentFormAdmin(ModelForm):
    def clean_student_group(self):
        groups = Group.objects.filter(leader=self.instance)
        if len(groups) > 0 and self.cleaned_data['student_group'] != groups[0]:
            raise ValidationError(u'Студент є старостою іншої групи.', code='invalid')
        return self.cleaned_data['student_group']

class StudentAdmin(admin.ModelAdmin):
    list_display = ['last_name', 'first_name', 'ticket', 'student_group']
    list_display_links = ['last_name', 'first_name']
    list_editable = ['student_group']
    ordering = ['last_name']
    list_filter = ['student_group']
    list_per_page = 10
    search_fields = ['last_name', 'first_name', 'middle_name', 'ticket', 'notes']
    form = StudentFormAdmin

    def view_on_site(self, obj):
        return reverse('students_edit', kwargs={'pk': obj.id})

class GroupAdmin(admin.ModelAdmin):
    list_display = ['title', 'leader', 'notes']
    list_display_links = ['title']
    list_editable = ['leader']
    ordering = ['title']
    list_filter = [('leader', RelatedOnlyFieldListFilter)]
    list_per_page = 10
    search_fields = ['title']

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'leader':
            group_id = (request.get_full_path()).split('/')
            if group_id[-2].isdigit():
                kwargs["queryset"] = Student.objects.filter(student_group=group_id[-2])

        return super(GroupAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def view_on_site(self, obj):
        return reverse('groups_edit', kwargs={'pk': obj.id})
# Register your models here.
admin.site.register(Student, StudentAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(Exam)
