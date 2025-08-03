from rest_framework import serializers
from . import models

class RoomTypeImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.RoomImage
        fields = ['Image']

class RoomTypeSerializer(serializers.ModelSerializer):
    room_type_imgs = RoomTypeImagesSerializer(many=True,read_only=True)
    class Meta:
        model = models.RoomType
        fields = ['id', 'title', 'details','room_type_imgs']