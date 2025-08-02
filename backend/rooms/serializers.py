from rest_framework import serializers
from . import models

class RoomTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.RoomType
        fields = ['id', 'title', 'details']