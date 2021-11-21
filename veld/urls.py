from django.urls import path
from veld.views import *

urlpatterns = [
    path('', index, name='index'),
]