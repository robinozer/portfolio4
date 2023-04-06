from . import views
from django.urls import path

urlpatterns = [
    path('', views.BookingListView.as_view(), name='home'),
    path('booking_form', views.BookingCreateView.as_view(), name='booking_form')
]
