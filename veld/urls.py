from django.urls import path
from veld.views import *

urlpatterns = [
    path('', BannerHome.as_view(), name='index'),
    path('addappointment/', AddAppointment.as_view(), name='addappointment'),
    path('pricelist/', PriceList.as_view(), name='pricelist'),
    path('contacts/', Contacts.as_view(), name='contacts'),
    path('login/', login, name='login'),
    # path('register/', RegisterUser, name='register'),
]