from django.urls import path

from . import views

app_name = "workshop"

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("about/contacts/", views.contacts, name="contacts"),
    path("about/directions/", views.directions, name="directions"),
    path("routes/", views.routes, name="routes"),
    path("schedule/", views.schedule, name="schedule"),
]
