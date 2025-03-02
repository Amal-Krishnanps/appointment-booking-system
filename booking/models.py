from django.db import models

class Booking(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    date = models.DateField()
    time_slot = models.TimeField()
    
    def __str__(self):
        return f"{self.name} - {self.date} at {self.time_slot}"