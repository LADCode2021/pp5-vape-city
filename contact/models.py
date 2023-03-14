from django.db import models
from django.core.validators import MinLengthValidator, EmailValidator


class Contact(models.Model):
    """
    Class to define fields for ContactForm and Contact table in db
    """

    first_name = models.CharField(max_length=25, null=False, blank=False)
    last_name = models.CharField(max_length=25, null=False, blank=False)
    email_address = models.EmailField(validators=[EmailValidator()])
    phone_number = models.CharField(validators=[
        MinLengthValidator
        (
            11, message="Please enter valid phone number starting with 0"
            )
            ], max_length=11, null=False, blank=False
            )
    comments = models.TextField()

    def __str__(self):  # code adapted from Models Part 2 FST walk-through
        return self.first_name + " " + self.last_name + " | "
