from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['name', 'party_size', 'date', 'time']
        widgets = {
            'name': forms.TextInput(attrs={
                'autocomplete': 'name'
            }),
            'party_size': forms.NumberInput(attrs={
                'autocomplete': 'off'
            }),
            'date': forms.DateInput(attrs={
                'type': 'date',
                'autocomplete': 'off'
            }),
            'time': forms.TimeInput(attrs={
                'type': 'time',
                'autocomplete': 'off'
            }),
        }
