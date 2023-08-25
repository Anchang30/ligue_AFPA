from django.urls import path
from . import views

app_name = "afpa"

urlpatterns = [
    path("", views.home, name="home"),
    path("classement/", views.classement, name = "classement"),
    path("classement/<int:date_journee>", views.classement, name="classement"),
    path("rencontre/", views.rencontre, name="rencontre"),
    path("rencontre/<int:date_journee>", views.rencontre, name="rencontre")
    ]
