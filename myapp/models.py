from django.db import models

# Create your models here.
from django.db import models

class UserData(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)  # Consider hashing the password

    def __str__(self):
        return self.name


class TrafficData(models.Model):
    junction_id = models.CharField(max_length=100, unique=True)
    number_of_vehicles = models.IntegerField()

    def __str__(self):
        return f"Junction {self.junction_id}: {self.number_of_vehicles} vehicles"
