from django.shortcuts import render
from datetime import time
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import Booking
from .serializers import BookingSerializer

AVAILABLE_SLOTS = [
    time(hour=10, minute=0), time(hour=10, minute=30),
    time(hour=11, minute=0), time(hour=11, minute=30),
    time(hour=12, minute=0), time(hour=12, minute=30),
    time(hour=2, minute=0), time(hour=2, minute=30),
    time(hour=3, minute=0), time(hour=3, minute=30),
    time(hour=4, minute=0), time(hour=4, minute=30),
    time(hour=5, minute=0)
]

class AvailableSlotsView(APIView):
    def get(self, request):
        date = request.GET.get('date')
        if not date:
            return Response({"error": "Invalid Date"}, status=status.HTTP_400_BAD_REQUEST)

        # Get booked slots for the date
        booked_slots = Booking.objects.filter(date=date).values_list('time_slot', flat=True)

        # Get free slots
        free_slots = [slot.strftime('%H:%M') for slot in AVAILABLE_SLOTS if slot not in booked_slots]

        return Response({"date": date, "available_slots": free_slots})

class BookAppointmentView(APIView):
    def post(self, request):
        serializer = BookingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Appointment booked successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
