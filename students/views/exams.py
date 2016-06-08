# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from ..models import Exam

def exams(request):
  exams = Exam.objects.all()

    # try to order groups list
  order_by = request.GET.get('order_by', '')
  if order_by in ('title','datetime'):
    exams = exams.order_by(order_by)
    if request.GET.get('reverse', '') == '1':
      exams=exams.reverse() 

    # paginate groups
  paginator = Paginator(exams, 1)
  page = request.GET.get('page')
  try:
    exams = paginator.page(page)
  except PageNotAnInteger:
        # If page is not an integer, deliver first page.
    exams = paginator.page(1)
  except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
    exams = paginator.page(paginator.num_pages)
  return render(request, 'students/exam.html',{'exams':exams})
   

#def students_add(request):
 #   return HttpResponse('<h1>Student Add Form</h1>')
#def students_edit(request, sid):
#    return HttpResponse('<h1>Edit Student %s</h1>' % sid)
#def students_delete(request, sid):
#    return HttpResponse('<h1>Delete Student %s</h1>' % sid)
