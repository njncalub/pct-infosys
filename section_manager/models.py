import datetime

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.timezone import utc

from program_manager.models import DegreeProgram
from school_year_manager.models import SchoolYear
from student_profiling.models import Student


YEAR_LEVEL_CHOICES = (
    (1, '1'),
    (2, '2'),
    (3, '3'),
    (4, '4'),
    (5, '5'),
)

optional = {
    'blank': True,
    'null': True,
}


class Section(models.Model):

    name           = models.CharField(_('section name'), max_length=15)
    degree_program = models.ForeignKey(DegreeProgram, **optional)
    year_level     = models.IntegerField(_('year level'), choices=YEAR_LEVEL_CHOICES, default=1, max_length=1, **optional)

    created_at     = models.DateTimeField(_('created at'), editable=False)
    modified_at    = models.DateTimeField(_('modified at'), **optional)

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = datetime.datetime.today().replace(tzinfo=utc)
        self.modified_at = datetime.datetime.today().replace(tzinfo=utc)

        return super(Section, self).save(*args, **kwargs)

    def __unicode__(self):
        return "{name}".format(name=self.name)


class SectionInstance(models.Model):

    school_year = models.ForeignKey(SchoolYear)
    section     = models.ForeignKey(Section)

    students    = models.ManyToManyField(Student, **optional)

    created_at  = models.DateTimeField(_('created at'), editable=False)
    modified_at = models.DateTimeField(_('modified at'), **optional)

    class Meta:
        unique_together = ('section', 'school_year',)

    def get_year_level(self):
        return self.section.year_level
    get_year_level.short_description = 'year level'

    def get_degree_program(self):
        return self.section.degree_program.full_name
    get_degree_program.short_description = 'degree program'

    def get_school_year(self):
        return self.school_year
    get_school_year.short_description = 'school year'

    def get_student_count(self):
        return self.students.count()
    get_student_count.short_description = 'students enrolled'

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = datetime.datetime.today().replace(tzinfo=utc)
        self.modified_at = datetime.datetime.today().replace(tzinfo=utc)

        return super(SectionInstance, self).save(*args, **kwargs)

    def __unicode__(self):
        return "{name} {sy}".format(name=self.section.name,
                                    sy=self.school_year.get_short_name())
