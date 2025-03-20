from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("church", views.church, name="church"),
    path("ladies", views.ladies, name="ladies"),
    path("rescue", views.rescue, name="rescue"),
    path("message_sent/", views.message_sent, name="message_sent")
]