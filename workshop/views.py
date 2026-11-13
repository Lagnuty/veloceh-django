from django.shortcuts import render


def home(request):
    return render(request, "workshop/home.html")


def about(request):
    return render(request, "workshop/about.html")


def contacts(request):
    return render(request, "workshop/contacts.html")


def directions(request):
    return render(request, "workshop/directions.html")


def routes(request):
    return render(request, "workshop/routes.html")


def schedule(request):
    return render(request, "workshop/schedule.html")
