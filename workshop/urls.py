from django.urls import path

from . import views

app_name = "workshop"

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("about/contacts/", views.contacts, name="contacts"),
    path("about/directions/", views.directions, name="directions"),
    path("routes/", views.RouteList.as_view(), name="routes"),
    path("routes/<int:pk>/", views.RouteDetail.as_view(), name="routes_detail"),
    path("routes/add/", views.RouteCreate.as_view(), name="routes_create"),
    path("routes/<int:pk>/edit/", views.RouteUpdate.as_view(), name="routes_update"),
    path("routes/<int:pk>/delete/", views.RouteDelete.as_view(), name="routes_delete"),

    path("schedule/", views.TripList.as_view(), name="schedule"),
    path("schedule/<int:pk>/", views.TripDetail.as_view(), name="schedule_detail"),
    path("schedule/add/", views.TripCreate.as_view(), name="schedule_create"),
    path("schedule/<int:pk>/edit/", views.TripUpdate.as_view(), name="schedule_update"),
    path("schedule/<int:pk>/delete/", views.TripDelete.as_view(), name="schedule_delete"),

    path("guides/", views.GuideList.as_view(), name="guides"),
    path("guides/<int:pk>/", views.GuideDetail.as_view(), name="guides_detail"),
    path("guides/add/", views.GuideCreate.as_view(), name="guides_create"),
    path("guides/<int:pk>/edit/", views.GuideUpdate.as_view(), name="guides_update"),
    path("guides/<int:pk>/delete/", views.GuideDelete.as_view(), name="guides_delete"),

    path("equipment/", views.EquipmentList.as_view(), name="equipment"),
    path("equipment/<int:pk>/", views.EquipmentDetail.as_view(), name="equipment_detail"),
    path("equipment/add/", views.EquipmentCreate.as_view(), name="equipment_create"),
    path("equipment/<int:pk>/edit/", views.EquipmentUpdate.as_view(), name="equipment_update"),
    path("equipment/<int:pk>/delete/", views.EquipmentDelete.as_view(), name="equipment_delete"),

    path("members/", views.MemberList.as_view(), name="members"),
    path("members/<int:pk>/", views.MemberDetail.as_view(), name="members_detail"),
    path("members/add/", views.MemberCreate.as_view(), name="members_create"),
    path("members/<int:pk>/edit/", views.MemberUpdate.as_view(), name="members_update"),
    path("members/<int:pk>/delete/", views.MemberDelete.as_view(), name="members_delete"),
]
