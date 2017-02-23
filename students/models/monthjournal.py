from django.db import models
from django.utils.translation import ugettext_lazy as _


class MonthJournal(models.Model):
    """Student Monthly Journal"""

    class Meta:
        verbose_name = _(u"Monthly Journal")
        verbose_name_plural = _(u"Monthly Journals")

    student = models.ForeignKey('Student',
        verbose_name=_(u"Student"),
        blank=False,
        unique_for_month='date')

    # we only need year and month, so always set day to first day of the month
    date = models.DateField(
        verbose_name=_(u"Date"),
        blank=False)




    def __unicode__(self):
        return u'%s: %d, %d' % (self.student.last_name, self.date.month,
            self.date.year)
for i in range(1, 32):
    MonthJournal.add_to_class(
        'present_day%d' % (i),
        models.BooleanField(default=False)
        )
