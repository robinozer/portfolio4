from .models import Booking
from django import forms


class BookingForm(forms.ModelForm):

    class Meta:
        model = Booking
        fields = ('first_name', 'email', 'guests', 'special_request',)

