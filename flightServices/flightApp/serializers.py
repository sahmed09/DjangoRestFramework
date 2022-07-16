from rest_framework import serializers
from .models import *
import re


# def is_validate_flight_number(data):
#     if re.match("^[a-zA-Z0-9]*$", data['flight_number']) is None:
#         raise serializers.ValidationError("Invalid flight number. Please make sure it is alphanumeric.")
#     return data


class FlightSerializers(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = '__all__'
        # validators = [is_validate_flight_number]  # Validations (First Process)

    # Validations (Second Process)
    # def validate_flight_number(self, flight_number):
    #     if re.match("^[a-zA-Z0-9]*$", flight_number) is None:
    #         raise serializers.ValidationError("Invalid flight number. Please make sure it is alphanumeric.")
    #     return flight_number

    # Validations (Third Process)
    def validate(self, data):
        if re.match("^[a-zA-Z0-9]*$", data['flight_number']) is None:
            raise serializers.ValidationError("Invalid flight number. Please make sure it is alphanumeric.")
        return data


class PassengerSerializers(serializers.ModelSerializer):
    class Meta:
        model = Passenger
        fields = '__all__'


class ReservationSerializers(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'
