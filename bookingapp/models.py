from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import datetime, timedelta
from django.utils import timezone


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    date_time = models.DateTimeField(validators=[MinValueValidator(limit_value=timezone.now() + timedelta(minutes=1), message=('Please choose a date and time in the future.'))])
    guests = models.IntegerField(validators=[MinValueValidator(1, message="Please enter a value between 1-8"), MaxValueValidator(8, message="Please enter a value between 1-8")])
    special_request = models.TextField()
    accepted = models.BooleanField(default=False)

    class Meta:
        ordering = ['-date_time']
        unique_together = ('date_time', 'email')

    # String representation of the booking.
    def __str__(self):
        return f'{self.user} - {self.date_time} for {self.guests} guests.'
