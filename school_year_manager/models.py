import datetime

from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from django.utils.timezone import utc

from student_profiling.models import Student


SEMESTER_CHOICES = (
    ('1STSEM', '1st semester'),
    ('2NDSEM', '2nd semester'),
    ('SUMMER', 'Summer'),
)

SEMESTER_DICT = {
    '1STSEM': '1st semester',
    '2NDSEM': '2nd semester',
    'SUMMER': 'Summer',
}

optional = {
    'blank': True,
    'null': True,
}


class SchoolYear(models.Model):

    start_year  = models.IntegerField(_('start year'), max_length=4, blank=True, null=True)
    end_year    = models.IntegerField(_('end year'), max_length=4, blank=True, null=True)
    is_active   = models.BooleanField(_('is active'), default=False)

    created_at  = models.DateTimeField(_('created at'), auto_now_add=True)
    modified_at = models.DateTimeField(_('modified at'), **optional)

    class Meta:
        verbose_name = _("school year")
        unique_together = ('start_year', 'end_year',)

    def get_short_name(self):
        return "SY{start_year}-{end_year}".format(start_year=str(self.start_year)[-2:],
                                                   end_year=str(self.end_year)[-2:])

    def __unicode__(self):
        if_is_active = _(" (active)").__unicode__()
        return "{0}-{1}{2}".format(str(self.start_year),
                                   str(self.end_year),
                                   (if_is_active if self.is_active else ""))

    def clean(self):
        if (self.end_year - self.start_year) is not 1:
            raise ValidationError(_("School Year should have 1 year difference"))

    def save(self, *args, **kwargs):
        if self.is_active:
            SchoolYear.objects.filter(is_active=True).update(is_active=False)
        if not self.id:
            self.created_at = datetime.datetime.today().replace(tzinfo=utc)
        self.modified_at = datetime.datetime.today().replace(tzinfo=utc)

        super(SchoolYear, self).save(*args, **kwargs)


class Semester(models.Model):

    semester    = models.CharField(_('semester'), choices=SEMESTER_CHOICES, max_length=6)
    school_year = models.ForeignKey(SchoolYear)

    students    = models.ManyToManyField(Student, **optional)

    created_at  = models.DateTimeField(_('created at'), editable=False)
    modified_at = models.DateTimeField(_('modified at'), **optional)

    class Meta:
        unique_together = ('semester', 'school_year',)

    def get_short_name(self):
        return "{semester} of {school_year}".format(semester=SEMESTER_DICT.get(self.semester),
                                                    school_year=self.school_year)

    def get_semester_number(self):
        if self.semester == "1STSEM":
            return 1
        if self.semester == "2NDSEM":
            return 2
        if self.semester == "SUMMER":
            return 3

    def get_student_count(self):
        return self.students.count()
    get_student_count.short_description = 'students enrolled'

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = datetime.datetime.today().replace(tzinfo=utc)
        self.modified_at = datetime.datetime.today().replace(tzinfo=utc)

        return super(Semester, self).save(*args, **kwargs)

    def __unicode__(self):
        return "{semester} of {school_year}".format(semester=SEMESTER_DICT.get(self.semester),
                                                    school_year=self.school_year)
