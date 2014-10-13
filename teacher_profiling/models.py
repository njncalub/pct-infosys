import datetime

from django.db import models
from django.core.exceptions import ValidationError
from django.utils.timezone import utc
from django.utils.translation import ugettext_lazy as _


SEX_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female'),
)

optional = {
    'blank': True,
    'null': True,
}


class Teacher(models.Model):

    last_name       = models.CharField(_('last name'), max_length=200, **optional)
    first_name      = models.CharField(_('first name'), max_length=200, **optional)
    middle_name     = models.CharField(_('middle name'), max_length=200, **optional)
    sex             = models.CharField(_('sex'), max_length=1, choices=SEX_CHOICES, **optional)
    birth_date      = models.DateField(_('birth date'), **optional)

    created_at      = models.DateTimeField(_('created at'), editable=False)
    modified_at     = models.DateTimeField(_('modified at'), **optional)

    def get_full_name(self):
        if self.last_name and self.first_name and self.middle_name:
            return "{ln}, {fn} {mn}".format(ln=self.last_name,
                                            fn=self.first_name,
                                            mn=self.middle_name)
        elif self.last_name and self.first_name:
            return "{ln}, {fn}".format(ln=self.last_name,
                                       fn=self.first_name)
        else:
            return ""
    get_full_name.short_description = 'full name'

    def get_short_name(self):
        if self.first_name and self.middle_name:
            return "{fn} {mn}".format(fn=self.first_name,
                                      mn=self.middle_name)
        elif self.first_name and not self.middle_name:
            return "{fn}".format(fn=self.first_name)
        else:
            return ""

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = datetime.datetime.today().replace(tzinfo=utc)
        self.modified_at = datetime.datetime.today().replace(tzinfo=utc)

        return super(Teacher, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.get_full_name()
