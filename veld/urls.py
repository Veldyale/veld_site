from django.urls import path
from veld.views import *

urlpatterns = [
    # path('', PostHome.as_view(), name='index'),
    path('', BannerHome.as_view(), name='index'),
    path('addappointment/', addappointment, name='addappointment'),
    path('pricelist/', pricelist, name='pricelist'),
    path('contacts/', contacts, name='contacts'),
    path('login/', login, name='login'),
    # path('register/', RegisterUser, name='register'),
]