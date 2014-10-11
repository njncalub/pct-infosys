from django.contrib import admin
from room_manager.models import Room

class RoomAdmin(admin.ModelAdmin):
    model = Room

admin.site.register(Room, RoomAdmin)
