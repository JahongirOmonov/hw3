from django.db import models

# Create your models here.

class BemorModel(models.Model):
    Bemor_Dardi = models.CharField(default='', max_length=200)
    Shikoyatlari = models.TextField()
    status = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.Bemor_Dardi
    

