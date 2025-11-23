from datetime import date
from django.shortcuts import render, redirect, get_object_or_404
from .forms import BookingForm
from .models import Booking
from django.contrib.auth.decorators import login_required

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

            if data['date'] < date.today():
                return render(request, "bookings/booking.html", {
                    "form": form,
                    "error": "You cannot book a date in the past.",
                })

            conflict = Booking.objects.filter(
                date=data['date'],
                time=data['time']
            )

            if conflict.exists():
                return render(request, "bookings/booking.html", {
                    "form": form,
                    "error": "Sorry, that time is already booked!",
                })

            booking = form.save(commit=False)
            if request.user.is_authenticated:
                booking.user = request.user
            booking.save()

            return redirect("booking_success")

    else:
        form = BookingForm()

    return render(request, "bookings/booking.html", {"form": form})

def booking_success(request):
    return render(request, "bookings/success.html")

@login_required
def my_bookings(request):
    bookings = Booking.objects.filter(user=request.user).order_by('-date', '-time')
    return render(request, "bookings/my_bookings.html", {"bookings": bookings})

@login_required
def edit_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)
    form = BookingForm(request.POST or None, instance=booking)

    if request.method == "POST" and form.is_valid():
        # Check for double-booking (same logic as new booking)
        data = form.cleaned_data
        conflict = Booking.objects.filter(
            date=data["date"],
            time=data["time"]
        ).exclude(id=booking_id)

        if conflict.exists():
            return render(request, "bookings/edit_booking.html", {
                "form": form,
                "error": "Sorry, that time is already booked!",
                "booking": booking,
            })

        form.save()
        return redirect("my_bookings")

    return render(request, "bookings/edit_booking.html", {
        "form": form,
        "booking": booking,
    })

@login_required
def delete_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)

    if request.method == "POST":
        booking.delete()
        return redirect("my_bookings")

    return render(request, "bookings/delete_booking.html", {"booking": booking})
