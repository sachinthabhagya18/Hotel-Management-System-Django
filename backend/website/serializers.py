from rest_framework import serializers
from . import models

class BannersSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Banners  # This is correct
        fields = ['id', 'title', 'image']