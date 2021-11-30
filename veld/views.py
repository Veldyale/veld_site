from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView

from veld.forms import *
from veld.models import *


class PostHome(ListView):
    model = Post
    template_name = 'veld/index.html'


# def index(request):
#     return render(request, 'veld/index.html')


def addappointment(request):
    form = AddAppointmentForm()
    return render(request, 'veld/addappointment.html', {'form': form})


def pricelist(request):
    return render(request, 'veld/pricelist.html')


def contacts(request):
    return render(request, 'veld/contacts.html')


def login(request):
    return render(request, 'veld/login.html')


class RegisterUser:
    pass