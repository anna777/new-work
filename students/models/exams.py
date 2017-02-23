# -*- coding: utf-8 -*-

from django.db import models



class Exam(models.Model):

    class Meta(object):
      verbose_name = u"Іспит"
      verbose_name_plural = u"Іспити"
    title = models.CharField(
      max_length=256,
      blank=False,
      verbose_name=u"Назва предмету")
    datetime = models.DateField(
      blank=False,
      verbose_name=u"Дата та час проведення",
      null=True)
    teatcher_name = models.CharField(
      max_length=256,
      verbose_name=u"Імя викладача",
      blank=True,
      null=True)
    group = models.ForeignKey('Group',
      verbose_name=u"Група",
      blank=True,
      null=True)

    def __unicode__(self):
      return u"%s" % (self.title)
