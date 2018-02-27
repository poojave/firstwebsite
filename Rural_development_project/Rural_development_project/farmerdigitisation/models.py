from django.db import models

# Create your models here.
class Farmer(models.Model):
    def __str__(self):
        return self.name + '-' + self.type
    name = models.CharField(max_length = 100)
    type = models.CharField(max_length=100)
    address = models.CharField(max_length = 100)
    phone = models.CharField(max_length = 100)
    deals_in = models.CharField(max_length = 100)
    addhar_no = models.CharField(max_length = 100)