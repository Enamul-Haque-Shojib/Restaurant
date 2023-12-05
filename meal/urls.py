
from django.urls import path
from . import views

urlpatterns = [
    path('showitem/', views.meal, name='showitem'),
]
