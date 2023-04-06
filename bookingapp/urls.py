from . import views
from django.urls import path
from .views import thank_you_view

urlpatterns = [
    path('', views.BookingListView.as_view(), name='home'),
    path('booking_form', views.BookingCreateView.as_view(), name='booking_form'),
    path('thank_you/', thank_you_view, name='thank_you'),
]
