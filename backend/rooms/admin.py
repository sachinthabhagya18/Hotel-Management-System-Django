from django.contrib import admin
from . import models

admin.site.register(models.RoomType)
admin.site.register(models.Room)
admin.site.register(models.Booking)
admin.site.register(models.Payment)
admin.site.register(models.Gallery)
admin.site.register(models.RoomImage)
