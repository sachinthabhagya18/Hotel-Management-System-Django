from rest_framework.generics import ListAPIView
from . import serializers
from . import models


class RoomTypeListView(ListAPIView):
    serializer_class = serializers.RoomTypeSerializer
    queryset = models.RoomType.objects.all()  # This is correct as is