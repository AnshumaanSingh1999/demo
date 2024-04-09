from django.urls import path
from . import views

urlpatterns=[
    path("",views.home,name="home"),
    path("badaKaam",views.badaKaam,name="badaKaam"),
    path("users",views.usersview,name="users"),


]