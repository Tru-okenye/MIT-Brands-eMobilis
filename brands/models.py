from django.db import models

# Create your models here.
class Brands(models.Model):
    name=models.CharField(max_length=100, blank=False, null=False)
   
    price=models.DecimalField(decimal_places=2, max_digits=6)
    description=models.TextField(default="Description")
    image=models.ImageField(upload_to="brands", default="")


def __str__(self):
    return self.name