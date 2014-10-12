from django.contrib import admin
from room_manager.models import Room

class RoomAdmin(admin.ModelAdmin):
    model = Room
    list_display = ('__unicode__', 'building', 'floor', )
    list_filter = ('building', 'floor', )
    search_fields = ('room_name', 'building', 'floor', )

admin.site.register(Room, RoomAdmin)
