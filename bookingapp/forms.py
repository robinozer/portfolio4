from .models import Booking
from django import forms


class BookingForm(forms.ModelForm):

    class Meta:
        model = Booking
        fields = ('first_name', 'email', 'guests', 'special_request',)
        date_time = forms.DateTimeField(widget=forms.DateTimeInput(format='%Y-%m-%d %H:%M:%S'))
