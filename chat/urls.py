from django.contrib import admin
from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.all_rooms, name="all_rooms"),
    path('token/', views.token, name="token"),
    re_path(r'rooms/(?P<slug>[-\w]+)/$', views.room_detail, name="room_detail"),

]
