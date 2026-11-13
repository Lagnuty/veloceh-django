from django.db import models
from django.urls import reverse


class Difficulty(models.Model):
    name = models.CharField("Название", max_length=50)

    def __str__(self):
        return self.name


class MeetingPoint(models.Model):
    name = models.CharField("Название", max_length=120)
    address = models.CharField("Адрес", max_length=200)

    def __str__(self):
        return self.name


class Route(models.Model):
    name = models.CharField("Название", max_length=120)
    distance = models.PositiveIntegerField("Длина в километрах")
    difficulty = models.ForeignKey(Difficulty, verbose_name="Сложность", on_delete=models.PROTECT)
    description = models.TextField("Описание")
    photo = models.ImageField("Фото", upload_to='routes/', blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("workshop:routes_detail", args=[self.pk])


class Guide(models.Model):
    name = models.CharField("Имя", max_length=120)
    phone = models.CharField("Телефон", max_length=30)
    experience = models.TextField("Опыт")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("workshop:guides_detail", args=[self.pk])


class Trip(models.Model):
    route = models.ForeignKey(Route, verbose_name="Маршрут", on_delete=models.CASCADE)
    guide = models.ForeignKey(Guide, verbose_name="Инструктор", on_delete=models.SET_NULL, null=True, blank=True)
    meeting_point = models.ForeignKey(MeetingPoint, verbose_name="Место сбора", on_delete=models.PROTECT)
    date = models.DateField("Дата")
    time = models.TimeField("Время")

    def __str__(self):
        return f"{self.route} · {self.date:%d.%m.%Y}"

    def get_absolute_url(self):
        return reverse("workshop:schedule_detail", args=[self.pk])


class Equipment(models.Model):
    name = models.CharField("Название", max_length=120)
    quantity = models.PositiveIntegerField("Количество")
    description = models.TextField("Описание")
    photo = models.ImageField("Фото", upload_to='equipment/', blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("workshop:equipment_detail", args=[self.pk])


class Member(models.Model):
    name = models.CharField("Имя", max_length=120)
    email = models.EmailField("Электронная почта")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("workshop:members_detail", args=[self.pk])


class Registration(models.Model):
    member = models.ForeignKey(Member, verbose_name="Участник", on_delete=models.CASCADE)
    trip = models.ForeignKey(Trip, verbose_name="Поход", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.member} · {self.trip}"
