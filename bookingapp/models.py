from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

CONFIRMATION = ((0, "Unconfirmed"), (1, "Confirmed"))


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    date_time = models.DateTimeField(auto_now=False)
#    guests = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(8)])
    guests = models.IntegerField(validators=[MinValueValidator(1, message="Please enter a value between 1-8"), MaxValueValidator(8, message="Please enter a value between 1-8")])
    special_request = models.TextField()
    accepted = models.BooleanField(default=False)

    class Meta:
        ordering = ['-date_time']

    # String representation of the booking.
    def __str__(self):
        return f'{self.user} - {self.date_time} for {self.guests} guests.'
