from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.timezone import utc
import datetime


optional = {
    'blank': True,
    'null': True,
}


class Room(models.Model):

    room_name   = models.CharField(_('room name'), max_length=30)
    building    = models.CharField(_('building'), max_length=50, **optional)
    floor       = models.IntegerField(_('floor'), max_length=1, **optional)

    created_at  = models.DateTimeField(_('created at'), editable=False)
    modified_at = models.DateTimeField(_('modified at'), **optional)

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = datetime.datetime.today().replace(tzinfo=utc)
        self.modified_at = datetime.datetime.today().replace(tzinfo=utc)

        return super(Room, self).save(*args, **kwargs)

    def __unicode__(self):
        return "Room {room_name}".format(room_name=self.room_name)
