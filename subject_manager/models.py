import datetime

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.timezone import utc

from room_manager.models import Room
from school_year_manager.models import SchoolYear, Semester
from student_profiling.models import Student
from teacher_profiling.models import Teacher
from section_manager.models import SectionInstance


TIME_SLOT_CHOICES = (
    ('0800AM', '08:00AM-12:00PM'),
    ('0100PM', '01:00PM-05:00PM'),
    ('0530PM', '05:30PM-09:30PM'),
)

DAYS_CHOICES = (
    ('M-F', 'Mondays-Fridays'),
    ('SAT', 'Saturdays'),
    ('SUN', 'Sundays'),
)

TIME_SLOT_DICT = {
    '0800AM': '08:00AM-12:00PM',
    '0100PM': '01:00PM-05:00PM',
    '0530PM': '05:30PM-09:30PM',
}

DAYS_DICT = {
    'M-F': 'Mondays-Fridays',
    'SAT': 'Saturdays',
    'SUN': 'Sundays',
}

optional = {
    'blank': True,
    'null': True,
}


class Subject(models.Model):

    code        = models.CharField(_('code'), max_length=15)
    name        = models.CharField(_('name'), max_length=35)
    description = models.TextField(_('description'), **optional)
    units       = models.IntegerField(_('units'), max_length=1, default=3)

    created_at  = models.DateTimeField(_('created at'), editable=False)
    modified_at = models.DateTimeField(_('modified at'), **optional)

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = datetime.datetime.today().replace(tzinfo=utc)
        self.modified_at = datetime.datetime.today().replace(tzinfo=utc)

        return super(Subject, self).save(*args, **kwargs)

    def __unicode__(self):
        return "{code} {name}".format(code=self.code, name=self.name)


class SubjectInstance(models.Model):

    subject       = models.ForeignKey(Subject)
    semester      = models.ForeignKey(Semester)
    section       = models.ForeignKey(SectionInstance)

    instance_code = models.CharField(_('instance code'), max_length=25, **optional)

    time          = models.CharField(_('time'), max_length=6, choices=TIME_SLOT_CHOICES, default='0800AM')
    days          = models.CharField(_('days'), max_length=3, choices=DAYS_CHOICES, default='M-F')
    date_start    = models.DateField(_('start date'), **optional)
    date_end      = models.DateField(_('end date'), **optional)
    room          = models.ForeignKey(Room, **optional)

    students      = models.ManyToManyField(Student, **optional)
    teacher       = models.ForeignKey(Teacher, **optional)

    created_at    = models.DateTimeField(_('created at'), editable=False)
    modified_at   = models.DateTimeField(_('modified at'), **optional)

    def prettify_time(self):
        return TIME_SLOT_DICT.get(self.time)

    def prettify_days(self):
        return DAYS_DICT.get(self.days)

    def get_student_count(self):
        return self.students.count()
    get_student_count.short_description = 'students enrolled'

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = datetime.datetime.today().replace(tzinfo=utc)
        self.modified_at = datetime.datetime.today().replace(tzinfo=utc)

        return super(SubjectInstance, self).save(*args, **kwargs)

    def __unicode__(self):
        return "{code} {semester}".format(code=self.subject.code,
                                          semester=self.semester.get_short_name())
