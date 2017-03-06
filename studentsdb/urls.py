"""studentsdb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import patterns, include, url
from django.contrib import admin
from .settings import MEDIA_ROOT, DEBUG
from django.contrib.auth import views as auth_views
from django.views.generic import RedirectView, TemplateView
from django.contrib.auth.decorators import login_required

from students.models.students import Student
from students.views.students import StudentUpdateView, StudentDeleteView, StudentCreateView
from students.views.groups import GroupUpdateView, GroupDeleteView
from students.views.journal import JournalView

urlpatterns = patterns ('',
    # Students urls
    url(r'^$', 'students.views.students.students_list', name='home'),
    url(r'^students/add/$',
    StudentCreateView.as_view(),
name= 'students_add'),
    url(r'^students/(?P<pk>\d+)/edit/$',
    StudentUpdateView.as_view(),
name='students_edit'),
    url(r'^students/(?P<pk>\d+)/delete/$',
    StudentDeleteView.as_view(),
    name='students_delete'),
    #journal

    url(r'^journal/(?P<pk>\d+)?/?$', JournalView.as_view(), name='journal'),

    # Groups urls
    url(r'^groups/$', 'students.views.groups.groups_list', name='groups'),
    url(r'^groups/add/$', 'students.views.groups.groups_add',
      name='groups_add'),
    url(r'^groups/(?P<pk>\d+)/edit/$',
      GroupUpdateView.as_view(),
      name='groups_edit'),
    url(r'^groups/(?P<pk>\d+)/delete/$',
      GroupDeleteView.as_view(),
      name='groups_delete'),

    url(r'^contact-admin/$',
    'students.views.contact_admin.contact_admin',
      name='contact_admin'),

    url(r'^exams/$', 'students.views.exams.exams', name='exams'),
    # User Related urls
    url(r'^users/profile/$', login_required(TemplateView.as_view(
template_name='registration/profile.html')), name='profile'),
    url(r'^users/logout/$', auth_views.logout, kwargs={'next_page': 'home'},
name='auth_logout'),
    url(r'^register/complete/$', RedirectView.as_view(pattern_name='home'),
name='registration_complete'),
url(r'^users/', include('registration.backends.simple.urls',
namespace='users')),
    # Social Auth Related urls
    url('^social/', include('social.apps.django_app.urls', namespace = 'social')),
    url(r'^admin/', include(admin.site.urls))

    )


if DEBUG:
# serve files from media folder
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': MEDIA_ROOT}))
