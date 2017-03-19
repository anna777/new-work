# -*- coding: utf-8 -*-

from django.db import models
from django.core.exceptions import ValidationError

def validate_image(photo):
    filesize = photo.file.size
    megabyte_limit = 2.0
    if filesize > megabyte_limit*1024*1024:
        raise ValidationError("Max file size is %sMB" % str(megabyte_limit))


class Student(models.Model):
#    """Student Model"""

    class Meta(object):
        verbose_name = u"Студент"
        verbose_name_plural = u"Студенти"

    first_name = models.CharField(
        max_length=256,
        blank=False,
        verbose_name=u"Ім'я")

    last_name = models.CharField(
        max_length=256,
        blank=False,
        verbose_name=u"Прізвище")

    middle_name = models.CharField(
        max_length=256,
        blank=True,
        verbose_name=u"По-батькові",
        default='')

    student_group = models.ForeignKey('Group',
        verbose_name=u"Група",
	blank=False,
	null=True,
	on_delete=models.PROTECT)
    birthday = models.DateField(
        blank=False,
        verbose_name=u"Дата народження",
        null=True)

    photo = models.ImageField(
        blank=True,
        validators=[validate_image],
        verbose_name=u"Фото",
        null=True)

    ticket = models.CharField(
        max_length=256,
        blank=False,
        verbose_name=u"Білет")

    notes = models.TextField(
        blank=True,
        verbose_name=u"Додаткові нотатки")

    def __unicode__(self):
        return u"%s %s" % (self.first_name, self.last_name)
