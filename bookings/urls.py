from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("menu/", views.menu, name="menu"),
    path("booking/", views.booking, name="booking"),
    path("booking/success/", views.booking_success, name="booking_success"),
    path("bookings/", views.my_bookings, name="my_bookings"),
    path("booking/<int:booking_id>/edit/", views.edit_booking, name="edit_booking"),
    path("booking/<int:booking_id>/delete/", views.delete_booking, name="delete_booking"),
]
