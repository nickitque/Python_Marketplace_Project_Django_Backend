from django.db import models
from django.conf import settings
from phonenumber_field.modelfields import PhoneNumberField


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    phone_number = PhoneNumberField(unique=True, blank=False)
    photo = models.ImageField(upload_to='users/%y/%m/%d', blank=True)

    def __str__(self):
        return self.user.username
