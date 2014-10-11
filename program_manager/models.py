import datetime

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.timezone import utc


# DEGREE_PROGRAM_CHOICES = (
#     ('BSA',          'Bachelor of Science in Accountancy'),
#     ('BS AcT',       'Bachelor of Science in Accounting Technology'),
#     ('BSBM',         'Bachelor of Science in Business Management'),
#     ('BS ENTREP',    'Bachelor of Science in Entrepreneurship'),
#     ('BS FIN',       'Bachelor of Science in Finance'),
#     ('BS HRM',       'Bachelor of Science in Human Resource Management'),
#     ('BS MKTG',      'Bachelor of Science in Marketing'),
#     ('BS CS',        'Bachelor of Science in Computer Science'),
#     ('BS IS',        'Bachelor of Science in Information Systems'),
#     ('BS IT',        'Bachelor of Science in Information Technology'),
#     ('BEED',         'Bachelor of Elementary Education - General'),
#     ('BEED-PS',      'Bachelor of Elementary Education - Preschool'),
#     ('BSED-ENGLISH', 'Bachelor of Secondary Education Major in English'),
#     ('BSED-MATH',    'Bachelor of Secondary Education Major in Math'),
#     ('BSED-PHYS',    'Bachelor of Secondary Education Major in Physical Sciences'),
#     ('BSED-SS',      'Bachelor of Secondary Education Major in Social Studies'),
#     ('BSED-BIO',     'Bachelor of Secondary Education Major in Biological Sciences'),
#     ('BS Arch',      'Bachelor of Science in Architecture'),
#     ('BS CE',        'Bachelor of Science in Civil Engineering'),
#     ('BS Comp Eng',  'Bachelor of Science in Computer Engineering'),
#     ('BS ChE',       'Bachelor of Science in Chemical Engineering'),
#     ('BS ECE',       'Bachelor of Science in Electronics and Communications Engineering'),
#     ('BS EE',        'Bachelor of Science in Electrical Engineering'),
#     ('BS IE',        'Bachelor of Science in Industrial Engineering'),
#     ('BS ME',        'Bachelor of Science in Mechanical Engineering'),
#     ('AB ENG',       'Bachelor of Arts in English'),
#     ('AB MC',        'Bachelor of Arts in Mass Communication'),
#     ('AB PHILO',     'Bachelor of Arts Major in Philosophy'),
#     ('BS BIO',       'Bachelor of Science in Biology'),
#     ('BS CHEM',      'Bachelor of Science in Chemistry'),
#     ('BS MATH',      'Bachelor of Science in Mathematics'),
#     ('BS ENVI SCI',  'Bachelor of Science in Environmental Science'),
#     ('BSN',          'Bachelor of Science in Nursing'),
#     ('AB ECON',      'Bachelor of Arts in Economics'),
#     ('AB IS-AMST',   'Bachelor of Arts in International Studies - Major in American Studies'),
#     ('AB IS-ASST',   'Bachelor of Arts in International Studies - Major in Asian Studies'),
#     ('AB POLSCI',    'Bachelor of Arts in Political Science'),
#     ('AB PSYCH',     'Bachelor of Arts in Psychology'),
#     ('AB SOCIO',     'Bachelor of Arts in Sociology'),
#     ('BSSW',         'Bachelor of Science in Social Work'),
#     ('OTHER',        'Other'),
# )

optional = {
    'blank': True,
    'null': True,
}


class DegreeProgram(models.Model):

    short_name  = models.CharField(_('short name'), max_length=30)
    full_name   = models.CharField(_('full name'), max_length=100)

    created_at  = models.DateTimeField(_('created at'), editable=False)
    modified_at = models.DateTimeField(_('modified at'), **optional)

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = datetime.datetime.today().replace(tzinfo=utc)
        self.modified_at = datetime.datetime.today().replace(tzinfo=utc)

        return super(DegreeProgram, self).save(*args, **kwargs)

    def __unicode__(self):
        return "{short_name}".format(short_name=self.short_name)
