from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    image = models.ImageField(upload_to="usera_image", blank=True, null=True)

    class Meta:
        db_table = "users"

    def __str__(self):
        return self.username
