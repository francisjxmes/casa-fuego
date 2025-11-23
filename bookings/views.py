from django.shortcuts import render, redirect
from .forms import BookingForm
from .models import Booking

def index(request):
    return render(request, "bookings/index.html")

def menu(request):
    return render(request, "bookings/menu.html")

def booking(request):
    if request.method == "POST":
        form = BookingForm(request.POST)

        if form.is_valid():
            # Check for double booking
            data = form.cleaned_data
            existing = Booking.objects.filter(
                date=data['date'],
                time=data['time']
            )

            if existing.exists():
                return render(request, "bookings/booking.html", {
                    "form": form,
                    "error": "Sorry, that time is already booked!",
                })

            booking = form.save(commit=False)
            booking.user = request.user if request.user.is_authenticated else None
            booking.save()

            return redirect("booking_success")

    else:
        form = BookingForm()

    return render(request, "bookings/booking.html", {"form": form})

def booking_success(request):
    return render(request, "bookings/success.html")


