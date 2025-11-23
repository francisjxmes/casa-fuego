from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Booking
from datetime import date, time

class BookingTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser", password="pass1234"
        )

    def test_booking_page_loads(self):
        response = self.client.get(reverse('booking'))
        self.assertEqual(response.status_code, 200)

    def test_create_booking(self):
        self.client.login(username="testuser", password="pass1234")

        response = self.client.post(reverse('booking'), {
            'name': 'Francis',
            'party_size': 2,
            'date': date.today(),
            'time': '18:00'
        })

        self.assertEqual(response.status_code, 302)
        self.assertEqual(Booking.objects.count(), 1)

    def test_double_booking_blocked(self):
        Booking.objects.create(
            user=self.user,
            name='A',
            party_size=2,
            date=date.today(),
            time=time(18, 0)
        )

        response = self.client.post(reverse('booking'), {
            'name': 'B',
            'party_size': 2,
            'date': date.today(),
            'time': '18:00'
        })

        self.assertContains(response, "already booked", status_code=200)
