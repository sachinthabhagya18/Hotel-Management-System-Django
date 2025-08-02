from django.urls import path
from . import views

urlpatterns = [
    path('banners',views.BannersList.as_view()),
]