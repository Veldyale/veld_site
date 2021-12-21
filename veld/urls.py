from django.urls import path
from veld.views import *

urlpatterns = [
    path('', main_page, name='index'),
    path('addappointment/', AddAppointment.as_view(), name='addappointment'),
    path('pricelist/', PriceList.as_view(), name='pricelist'),
    path('contacts/', Contacts.as_view(), name='contacts'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
]