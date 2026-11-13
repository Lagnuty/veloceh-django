from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from .models import Equipment, Guide, Member, Route, Trip


def home(request):
    return render(request, "workshop/home.html")


def about(request):
    return render(request, "workshop/about.html")


def contacts(request):
    return render(request, "workshop/contacts.html")


def directions(request):
    return render(request, "workshop/directions.html")


class RouteList(ListView):
    model = Route
    template_name = "workshop/records/list.html"
    ordering = "name"
    extra_context = {
        "title": "Маршруты",
        "list_name": "workshop:routes",
        "create_name": "workshop:routes_create",
    }


class RouteDetail(DetailView):
    model = Route
    template_name = "workshop/records/detail.html"
    extra_context = {
        "title": "Маршруты",
        "list_name": "workshop:routes",
        "update_name": "workshop:routes_update",
        "delete_name": "workshop:routes_delete",
    }


class RouteCreate(CreateView):
    model = Route
    template_name = "workshop/records/form.html"
    fields = ["name","distance","difficulty","description","photo"]
    extra_context = {
        "title": "Маршруты",
        "list_name": "workshop:routes",
        "action": "Добавление записи",
    }


class RouteUpdate(UpdateView):
    model = Route
    template_name = "workshop/records/form.html"
    fields = ["name","distance","difficulty","description","photo"]
    extra_context = {
        "title": "Маршруты",
        "list_name": "workshop:routes",
        "action": "Редактирование записи",
    }


class RouteDelete(DeleteView):
    model = Route
    template_name = "workshop/records/delete.html"
    success_url = reverse_lazy("workshop:routes")
    extra_context = {
        "title": "Маршруты",
        "list_name": "workshop:routes",
    }


class TripList(ListView):
    model = Trip
    template_name = "workshop/records/list.html"
    ordering = "date"
    extra_context = {
        "title": "Расписание",
        "list_name": "workshop:schedule",
        "create_name": "workshop:schedule_create",
    }


class TripDetail(DetailView):
    model = Trip
    template_name = "workshop/records/detail.html"
    extra_context = {
        "title": "Расписание",
        "list_name": "workshop:schedule",
        "update_name": "workshop:schedule_update",
        "delete_name": "workshop:schedule_delete",
    }


class TripCreate(CreateView):
    model = Trip
    template_name = "workshop/records/form.html"
    fields = ["route","guide","meeting_point","date","time"]
    extra_context = {
        "title": "Расписание",
        "list_name": "workshop:schedule",
        "action": "Добавление записи",
    }


class TripUpdate(UpdateView):
    model = Trip
    template_name = "workshop/records/form.html"
    fields = ["route","guide","meeting_point","date","time"]
    extra_context = {
        "title": "Расписание",
        "list_name": "workshop:schedule",
        "action": "Редактирование записи",
    }


class TripDelete(DeleteView):
    model = Trip
    template_name = "workshop/records/delete.html"
    success_url = reverse_lazy("workshop:schedule")
    extra_context = {
        "title": "Расписание",
        "list_name": "workshop:schedule",
    }


class GuideList(ListView):
    model = Guide
    template_name = "workshop/records/list.html"
    ordering = "name"
    extra_context = {
        "title": "Инструкторы",
        "list_name": "workshop:guides",
        "create_name": "workshop:guides_create",
    }


class GuideDetail(DetailView):
    model = Guide
    template_name = "workshop/records/detail.html"
    extra_context = {
        "title": "Инструкторы",
        "list_name": "workshop:guides",
        "update_name": "workshop:guides_update",
        "delete_name": "workshop:guides_delete",
    }


class GuideCreate(CreateView):
    model = Guide
    template_name = "workshop/records/form.html"
    fields = ["name","phone","experience"]
    extra_context = {
        "title": "Инструкторы",
        "list_name": "workshop:guides",
        "action": "Добавление записи",
    }


class GuideUpdate(UpdateView):
    model = Guide
    template_name = "workshop/records/form.html"
    fields = ["name","phone","experience"]
    extra_context = {
        "title": "Инструкторы",
        "list_name": "workshop:guides",
        "action": "Редактирование записи",
    }


class GuideDelete(DeleteView):
    model = Guide
    template_name = "workshop/records/delete.html"
    success_url = reverse_lazy("workshop:guides")
    extra_context = {
        "title": "Инструкторы",
        "list_name": "workshop:guides",
    }


class EquipmentList(ListView):
    model = Equipment
    template_name = "workshop/records/list.html"
    ordering = "name"
    extra_context = {
        "title": "Снаряжение",
        "list_name": "workshop:equipment",
        "create_name": "workshop:equipment_create",
    }


class EquipmentDetail(DetailView):
    model = Equipment
    template_name = "workshop/records/detail.html"
    extra_context = {
        "title": "Снаряжение",
        "list_name": "workshop:equipment",
        "update_name": "workshop:equipment_update",
        "delete_name": "workshop:equipment_delete",
    }


class EquipmentCreate(CreateView):
    model = Equipment
    template_name = "workshop/records/form.html"
    fields = ["name","quantity","description","photo"]
    extra_context = {
        "title": "Снаряжение",
        "list_name": "workshop:equipment",
        "action": "Добавление записи",
    }


class EquipmentUpdate(UpdateView):
    model = Equipment
    template_name = "workshop/records/form.html"
    fields = ["name","quantity","description","photo"]
    extra_context = {
        "title": "Снаряжение",
        "list_name": "workshop:equipment",
        "action": "Редактирование записи",
    }


class EquipmentDelete(DeleteView):
    model = Equipment
    template_name = "workshop/records/delete.html"
    success_url = reverse_lazy("workshop:equipment")
    extra_context = {
        "title": "Снаряжение",
        "list_name": "workshop:equipment",
    }


class MemberList(ListView):
    model = Member
    template_name = "workshop/records/list.html"
    ordering = "name"
    extra_context = {
        "title": "Участники",
        "list_name": "workshop:members",
        "create_name": "workshop:members_create",
    }


class MemberDetail(DetailView):
    model = Member
    template_name = "workshop/records/detail.html"
    extra_context = {
        "title": "Участники",
        "list_name": "workshop:members",
        "update_name": "workshop:members_update",
        "delete_name": "workshop:members_delete",
    }


class MemberCreate(CreateView):
    model = Member
    template_name = "workshop/records/form.html"
    fields = ["name","email"]
    extra_context = {
        "title": "Участники",
        "list_name": "workshop:members",
        "action": "Добавление записи",
    }


class MemberUpdate(UpdateView):
    model = Member
    template_name = "workshop/records/form.html"
    fields = ["name","email"]
    extra_context = {
        "title": "Участники",
        "list_name": "workshop:members",
        "action": "Редактирование записи",
    }


class MemberDelete(DeleteView):
    model = Member
    template_name = "workshop/records/delete.html"
    success_url = reverse_lazy("workshop:members")
    extra_context = {
        "title": "Участники",
        "list_name": "workshop:members",
    }
