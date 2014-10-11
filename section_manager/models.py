import datetime

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.timezone import utc

from school_year_manager.models import SchoolYear
from student_profiling.models import Student


optional = {
    'blank': True,
    'null': True,
}


class Section(models.Model):

    name        = models.CharField(_('section name'), max_length=15)

    created_at  = models.DateTimeField(_('created at'), editable=False)
    modified_at = models.DateTimeField(_('modified at'), **optional)

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = datetime.datetime.today().replace(tzinfo=utc)
        self.modified_at = datetime.datetime.today().replace(tzinfo=utc)

        return super(Section, self).save(*args, **kwargs)

    def __unicode__(self):
        return "{code} {name}".format(code=self.code, name=self.name)


class SectionInstance(models.Model):

    section     = models.ForeignKey(Section)
    school_year = models.ForeignKey(SchoolYear)

    students    = models.ManyToManyField(Student)

    created_at  = models.DateTimeField(_('created at'), editable=False)
    modified_at = models.DateTimeField(_('modified at'), **optional)

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = datetime.datetime.today().replace(tzinfo=utc)
        self.modified_at = datetime.datetime.today().replace(tzinfo=utc)

        return super(SubjectInstance, self).save(*args, **kwargs)

    def __unicode__(self):
        return "{code} {school_year}".format(code=self.subject.code,
                                             school_year=self.school_year.get_short_name())
