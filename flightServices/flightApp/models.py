from django.db import models


class Flight(models.Model):
    flight_number = models.CharField(max_length=10)
    operating_airlines = models.CharField(max_length=20)
    departure_city = models.CharField(max_length=20)
    arrival_city = models.CharField(max_length=20)
    Date_of_departure = models.DateField()
    estimated_time_of_departure = models.TimeField()

    def __str__(self):
        return f'{self.flight_number} - {self.operating_airlines} - {self.departure_city} - {self.arrival_city}'


class Passenger(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)

    def __str__(self):
        return f'{self.first_name} - {self.last_name} - {self.email} - {self.phone}'


class Reservation(models.Model):
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    passenger = models.ForeignKey(Passenger, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.flight} - {self.passenger}'
