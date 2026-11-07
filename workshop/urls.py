from django.urls import path
from django.views.generic import TemplateView

app_name = "workshop"

urlpatterns = [
    path("", TemplateView.as_view(template_name="workshop/home.html"), name="home"),
    path("about/", TemplateView.as_view(template_name="workshop/about.html"), name="about"),
    path("about/contacts/", TemplateView.as_view(template_name="workshop/contacts.html"), name="contacts"),
    path("about/directions/", TemplateView.as_view(template_name="workshop/directions.html"), name="directions"),
    path("routes/", TemplateView.as_view(template_name="workshop/routes.html"), name="routes"),
    path("schedule/", TemplateView.as_view(template_name="workshop/schedule.html"), name="schedule"),
]


