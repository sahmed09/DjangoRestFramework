from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('flights', views.FlightViewSet)
router.register('passengers', views.PassengerViewSet)
router.register('reservations', views.ReservationViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('findFlights/', views.find_flight),
    path('saveReservation/', views.save_reservation),
]
