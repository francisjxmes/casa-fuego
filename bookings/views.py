from django.shortcuts import render

def index(request):
    return render(request, "bookings/index.html")

def menu(request):
    return render(request, "bookings/menu.html")

def booking(request):
    return render(request, "bookings/booking.html")
