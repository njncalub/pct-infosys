from django.db import models
from django.core.exceptions import ValidationError

class SchoolYear(models.Model):
    start_year = models.IntegerField(max_length=4, blank=True, null=True, unique=True)
    end_year   = models.IntegerField(max_length=4, blank=True, null=True, unique=True)
    is_active  = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "School Year"

    def __unicode__(self):
        return "%s-%s%s" % (str(self.start_year), str(self.end_year), (" (active)" if self.is_active else ""))

    def clean(self):
        if (self.end_year - self.start_year) is not 1:
            raise ValidationError('School Year should have 1 year difference')

    def save(self, *args, **kwargs):
        if self.is_active:
            SchoolYear.objects.filter(is_active=True).update(is_active=False)

        super(SchoolYear, self).save(*args, **kwargs)
