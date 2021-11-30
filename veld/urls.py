from django.urls import path
from veld.views import *

urlpatterns = [
    path('', index, name='index'),
    path('addappointment/', addappointment, name='addappointment'),
    path('pricelist/', pricelist, name='pricelist'),
    path('contacts/', contacts, name='contacts'),
    path('login/', login, name='login'),
    # path('register/', RegisterUser, name='register'),
]