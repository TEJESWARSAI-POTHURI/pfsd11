from django.db import models

class Flight(models.Model):
    FlightId = models.CharField(max_length=3)
    FlightName = models.CharField(max_length=200)
    FlightSource = models.CharField(max_length=10)
    FlightDestination = models.CharField(max_length=150)

    class Meta:
        db_table="Flight"



