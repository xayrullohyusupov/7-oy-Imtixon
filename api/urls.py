from django.urls import path
from .views import staff_list, attendance_create

urlpatterns = [
    path('staff-list/', staff_list, name='staff_list'),
    path('attendance-create/<int:id>/', attendance_create, name='attendance_create'),
]