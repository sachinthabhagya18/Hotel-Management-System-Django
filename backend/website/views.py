from rest_framework.generics import ListAPIView
from . import serializers
from . import models


class BannersList(ListAPIView):
    serializer_class = serializers.BannersSerializer
    queryset = models.Banners.objects.all()  # This is correct as is
