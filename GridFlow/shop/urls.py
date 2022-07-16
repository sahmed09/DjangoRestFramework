from django.urls import path
from . import views

app_name = 'shop'
urlpatterns = [
    path('', views.index, name='index'),
    path('<str:room_name>/<str:token>/', views.room, name='room'),
]
