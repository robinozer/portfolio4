from django.contrib import admin
from .models import Booking


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):

    list_display = ('first_name', 'date_time', 'guests', 'accepted')
    search_fields = ['first_name', 'email']
    list_filter = ('accepted', 'date_time')
    actions = ['accept_booking']

    def accept_booking(self, request, queryset):
        queryset.update(accepted=True)


"""

from django.contrib import admin
from .models import Booking
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Booking)
class BookingAdmin(SummernoteModelAdmin):

    list_display = ('date_time', 'guests', 'accepted', 'first_name')
    search_fields = ['first_name']
    list_filter = ('accepted', 'date_time')
"""
