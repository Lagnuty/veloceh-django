from datetime import date, time

from django.contrib.staticfiles import finders
from django.core.files import File
from django.core.management.base import BaseCommand

from workshop.models import Difficulty, Equipment, Guide, MeetingPoint, Member, Registration, Route, Trip


class Command(BaseCommand):
    help = "Добавляет учебные записи и фотографии для туристического клуба"

    def handle(self, *args, **options):
        difficulty, _ = Difficulty.objects.get_or_create(name="Начальный")
        Difficulty.objects.get_or_create(name="Средний")
        meeting_point, _ = MeetingPoint.objects.get_or_create(
            name="У входа в клуб", defaults={"address": "Москва, ул. Походная, 10"}
        )
        guide, _ = Guide.objects.get_or_create(
            name="Анна Соколова",
            defaults={"phone": "+7 (000) 000-00-00", "experience": "Ведёт походы выходного дня."},
        )
        route, _ = Route.objects.get_or_create(
            name="Лесная тропа",
            defaults={
                "distance": 8,
                "difficulty": difficulty,
                "description": "Пеший маршрут по лесу с остановкой у озера.",
            },
        )
        trip, _ = Trip.objects.get_or_create(
            route=route,
            date=date(2026, 11, 28),
            defaults={"guide": guide, "meeting_point": meeting_point, "time": time(9, 30)},
        )
        equipment, _ = Equipment.objects.get_or_create(
            name="Походный рюкзак",
            defaults={"quantity": 4, "description": "Рюкзак для однодневных походов."},
        )
        member, _ = Member.objects.get_or_create(
            email="member@example.com", defaults={"name": "Иван Петров"}
        )
        Registration.objects.get_or_create(member=member, trip=trip)

        for item, filename in ((route, "forest.jpg"), (equipment, "backpack.jpg")):
            if not item.photo:
                with open(finders.find(f"workshop/demo/{filename}"), "rb") as photo:
                    item.photo.save(filename, File(photo))

        self.stdout.write(self.style.SUCCESS("Учебные записи готовы."))
