from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

class SchoolYear(models.Model):
    start_year = models.IntegerField(_('start year'), max_length=4, blank=True, null=True, unique=True)
    end_year   = models.IntegerField(_('end year'), max_length=4, blank=True, null=True, unique=True)
    is_active  = models.BooleanField(_('is active'), default=False)
    created_at = models.DateTimeField(_('created at'), auto_now_add=True)

    class Meta:
        verbose_name = _("school year")

    def get_short_name(self):
        return "SY {start_year}-{end_year}".format(start_year=str(self.start_year)[-2],
                                                   end_year=str(self.end_year)[-2])

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

        super(SchoolYear, self).save(*args, **kwargs)
