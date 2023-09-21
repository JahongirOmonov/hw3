from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class DoktorUser(AbstractUser):
    Doktor_turlari = (
        (3,'Tish'),
        (2, 'Lor'),
        (1, 'Xirurg')
    )

    roles = models.PositiveIntegerField(choices=Doktor_turlari, default=1)
