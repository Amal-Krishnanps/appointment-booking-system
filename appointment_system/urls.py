
from django.contrib import admin
from django.urls import path,include
from booking.views import appointment_booking,AvailableSlotsView,BookAppointmentView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', appointment_booking, name='appointment_booking'),
    path('available-slots/', AvailableSlotsView.as_view(), name='available_slots'),
    path('book-appointment/', BookAppointmentView.as_view(), name='book_appointment'),
]
