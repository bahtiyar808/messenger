from django.contrib.auth.models import AbstractUser, User
from django.db import models
from django.urls import reverse


class Profile(AbstractUser):
    profile_pic = models.ImageField(null=True, blank=True, upload_to="images/profile", default=None)

    def __str__(self):
        return str(self.username)

    def get_absolute_url(self):
        return reverse('user_profile', args=[str(self.id)])


class Room(models.Model):
    room_name = models.CharField(max_length=255)
    created_by = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return self.room_name


