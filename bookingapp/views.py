from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.views import generic, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import BookingForm
from .models import Booking


class BookingListView(generic.ListView):
    model = Booking
    queryset = Booking.objects.order_by("-date_time")
    template_name = 'index.html'
    paginate_by = 6
    
    # Return the bookings for the currently logged in user
    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Booking.objects.filter(user=self.request.user)
        else:
            return Booking.objects.filter()


# Create a new booking
class BookingCreateView(CreateView, LoginRequiredMixin):
    model = Booking
    fields = ['first_name', 'email', 'date_time', 'guests', 'special_request']
    success_url = ('thank_you')
    template_name = 'booking_form.html'

    def get_booking(self, request):
        if request.method == 'POST':
            form = BookingForm(request.POST)
            if form.is_valid():
                return HttpResponseRedirect('/thank_you/')

    # Set the current user as the user for the new booking
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
