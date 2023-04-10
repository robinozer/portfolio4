from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.views import generic, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import BookingForm
from django.urls import reverse_lazy
from django.contrib import messages
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
    success_url = reverse_lazy('bookingapp:home')
    template_name = 'booking_form.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        response = super().form_valid(form)
        return response


# Update an existing booking
class BookingUpdateView(LoginRequiredMixin, UpdateView):
    model = Booking
    fields = ['first_name', 'email', 'date_time', 'guests', 'special_request']
    success_url = reverse_lazy('bookingapp:home')
    template_name = 'booking_edit.html'

    def get_object(self, queryset=None):
        pk = self.kwargs.get('pk')
        booking = get_object_or_404(Booking, pk=pk, user=self.request.user)
        if booking.user != self.request.user:
            raise Http404
        return booking

    def form_valid(self, form):
        form.instance.user = self.request.user
        response = super().form_valid(form)
        return response

    def find_booking(self, form):
        return Booking.objects.filter(user=self.request.user).filter(date_time=form['date_time'])


class BookingDeleteView(LoginRequiredMixin, DeleteView):
    model = Booking
    success_url = reverse_lazy('bookingapp:home')
    template_name = 'booking_delete.html'

    def get_object(self, queryset=None):
        pk = self.kwargs.get('pk')
        booking = get_object_or_404(Booking, pk=pk)
        if booking.user != self.request.user:
            raise Http404
        return booking

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Booking deleted successfully')
        return super().delete(request, *args, **kwargs)
