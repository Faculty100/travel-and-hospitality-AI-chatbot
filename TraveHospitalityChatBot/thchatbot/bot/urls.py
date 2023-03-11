from django.urls import path 
from . import views
app_name = "bot"

urlpatterns = [
    path("", views.index),
    path("chat/<str:msg>", views.chat)
]