from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.views import generic, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import BookingForm
from django.urls import reverse_lazy
from .models import Booking


class BookingListView(LoginRequiredMixin, generic.ListView):
    model = Booking

    template_name = 'index.html'
    paginate_by = 6

    # Return the bookings for the currently logged in user
    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Booking.objects.filter(user=self.request.user).order_by("-date_time")


# Create a new booking
class BookingCreateView(LoginRequiredMixin, CreateView):
    model = Booking
    fields = ['first_name', 'email', 'date_time', 'guests', 'special_request']
    success_url = reverse_lazy('thank_you_view/')
    template_name = 'booking_form.html'

    # Set the current user as the user for the new booking
    def form_valid(self, form):
        form.instance.user = self.request.user
        response = super().form_valid(form)
        return response


# User redirect page after submitting booking
def thank_you_view(request):
    return render(request, 'thank_you_view.html')


def edit_booking(request):
    return render(request, 'booking_edit.html')


# Update an existing booking
class BookingUpdateView(LoginRequiredMixin, UpdateView):
    model = Booking
    fields = ['first_name', 'email', 'date_time', 'guests', 'special_request']
    success_url = reverse_lazy('thank_you_view/')
    template_name = 'booking_edit.html'
    booking = Booking.objects.get(id=id)

    # Set the current user as the user for the new booking
    def form_valid(self, form):
        form.instance.user = self.request.user
        response = super().form_valid(form)
        return response
