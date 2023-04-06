from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Booking


class BookingListView(generic.ListView):
    model = Booking
    queryset = Booking.objects.order_by("-date_time")
    template_name = 'index.html'
    paginate_by = 6




