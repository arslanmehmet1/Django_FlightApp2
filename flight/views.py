from django.shortcuts import render
from rest_framework import viewsets
from .serializers import FlightSerializers, ReservationSerializers
from .models import Flight, Reservation
from rest_framework.permissions import IsAdminUser
from .permissions import IsStafforReadOnly


# Create your views here.
class FlightView(viewsets.ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializers
    permission_classes = (IsStafforReadOnly,)

class ReservationView(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializers
    # permission_classes = (IsStafforReadOnly,)
