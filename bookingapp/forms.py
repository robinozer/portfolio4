from .models import Booking
from django import forms


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('first_name', 'email', 'date_time', 'guests', 'special_request',)
