from . import views
from django.urls import path

app_name = 'bookingapp'

urlpatterns = [
    path('', views.BookingListView.as_view(), name='home'),
    path('booking_form/', views.BookingCreateView.as_view(), name='booking_form'),
    path('booking/<int:pk>/edit/', views.BookingUpdateView.as_view(), name='booking_edit'),
    path('booking/<int:pk>/delete/', views.BookingDeleteView.as_view(), name='booking_delete'),
]
