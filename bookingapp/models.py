from django.db import models
from django.contrib.auth.models import User

CONFIRMATION = ((0, "Unconfirmed"), (1, "Confirmed"))


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    date_time = models.DateTimeField(auto_now=True)
    guests = models.IntegerField()  # The number of guests for the booking
    special_request = models.TextField()
    accepted = models.BooleanField(default=False)

    class Meta:
        ordering = ['-date_time']

    # String representation of the booking.
    def __str__(self):
        return f'{self.user} - {self.date_time} for {self.guests} guests.'
