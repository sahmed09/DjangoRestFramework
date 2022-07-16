from .serializers import *
from .models import *
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated


@api_view(['POST'])
def find_flight(request):
    flights = Flight.objects.filter(departure_city=request.data['departure_city'],
                                    arrival_city=request.data['arrival_city'],
                                    Date_of_departure=request.data['Date_of_departure'])
    # POST "departure_city, arrival_city, Date_of_departure" from Body->x-www-form-urlencoded using Postman
    serializer = FlightSerializers(flights, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def save_reservation(request):
    # finding the flight using flight_id, creating the passenger on the fly and save the reservation using flight_id
    # and passenger details.
    flight = Flight.objects.get(id=request.data['flight_id'])

    passenger = Passenger.objects.filter(first_name=request.data['first_name'], last_name=request.data['last_name'],
                                         email=request.data['email'], phone=request.data['phone']).first()

    if passenger is None:
        passenger = Passenger()
        passenger.first_name = request.data['first_name']
        passenger.last_name = request.data['last_name']
        passenger.email = request.data['email']
        passenger.phone = request.data['phone']
        passenger.save()

    reservation = Reservation()
    reservation.flight = flight
    reservation.passenger = passenger
    reservation.save()

    return Response(status=status.HTTP_201_CREATED)


class FlightViewSet(viewsets.ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializers
    filter_backends = [filters.SearchFilter]
    search_fields = ['flight_number', 'operating_airlines', 'departure_city', 'arrival_city']
    permission_classes = [IsAuthenticated]


class PassengerViewSet(viewsets.ModelViewSet):
    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializers
    filter_backends = [filters.SearchFilter]
    search_fields = ['first_name', 'last_name', 'email', 'phone']


class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializers
