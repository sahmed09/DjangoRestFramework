from django.urls import path
from . import views

urlpatterns = [
    path('employee/', views.employee_view),
]
