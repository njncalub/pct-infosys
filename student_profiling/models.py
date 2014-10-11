import datetime

from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import UserManager
from django.core.exceptions import ValidationError
from django.core.mail import send_mail
from django.utils.translation import ugettext_lazy as _
from django.utils.timezone import utc

from program_manager.models import DegreeProgram


SEX_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female'),
)

optional = {
    'blank': True,
    'null': True,
}


class StudentManager(BaseUserManager):

    def create_user(self, username, password=None):
        if not username:
            raise ValueError('The username must be set')
        user = self.model(username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password):
        user = self.create_user(username=username, password=password)
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Student(AbstractBaseUser, PermissionsMixin):

    username        = models.CharField(_('username'), max_length=30, unique=True)
    email           = models.EmailField(_('email'), **optional)

    last_name       = models.CharField(_('last name'), max_length=200, **optional)
    first_name      = models.CharField(_('first name'), max_length=200, **optional)
    middle_name     = models.CharField(_('middle name'), max_length=200, **optional)
    sex             = models.CharField(_('sex'), max_length=1, choices=SEX_CHOICES, **optional)
    birth_date      = models.DateField(_('birth date'), **optional)

    degree_program  = models.ForeignKey(DegreeProgram, **optional)

    address         = models.TextField(_('address'), max_length=200, **optional)
    mobile_number   = models.CharField(_('mobile number'), max_length=200, **optional)
    landline_number = models.CharField(_('landline number'), max_length=200, **optional)
    website_address = models.URLField(_('website address'), max_length=200, **optional)

    is_active       = models.BooleanField(_('is active'), default=True)
    is_staff        = models.BooleanField(_('is staff'), default=False)
    is_admin        = models.BooleanField(_('is admin'), default=False)
    created_at      = models.DateTimeField(_('created at'), editable=False)
    modified_at     = models.DateTimeField(_('modified at'), **optional)

    objects = StudentManager()

    USERNAME_FIELD  = 'username'
    REQUIRED_FIELDS = []

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

        return super(Student, self).save(*args, **kwargs)

    def email_user(self, subject, message, from_email=None):
        send_mail(subject, message, from_email, [self.email])

    def __unicode__(self):
        return "{0}".format(self.username)
