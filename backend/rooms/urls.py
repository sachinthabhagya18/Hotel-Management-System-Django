from django.urls import path
from . import views

urlpatterns = [
    path('room-type',views.RoomTypeListView.as_view()),
]