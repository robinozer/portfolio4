from .models import Booking
from django import forms


class BookingForm(forms.Form):
    model = Booking
    first_name = forms.CharField(label='First name', max_length=100)
    email = forms.EmailField(label='Email')
    date_time = forms.DateTimeField()
    guests = forms.IntegerField()
    special_request = forms.Textarea()