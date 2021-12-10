from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from datetime import datetime

from veld.forms import *
from veld.models import *


menu = [{'title': 'Запись', 'url_name': 'addappointment'},
          {'title': 'Цены', 'url_name': 'pricelist'},
          {'title': 'Контакты', 'url_name': 'contacts'},
          {'title': 'Войти', 'url_name': 'login'},
          ]


def main_page(request):
    banners = Banner.objects.filter(Q(is_published=True) & Q(end_date__gte=datetime.now()) | Q(is_published=True) & Q(end_date = None))
    posts = Post.objects.all().filter(Q(is_published=True) & Q(end_date__gte=datetime.now()) | Q(is_published=True) & Q(end_date = None))

    response_data = {
        'banners': banners,
        'posts': posts,
        'menu': menu,
    }

    return render(request, 'veld/index.html', response_data)

# class PostHome(ListView):
#     model = Post
#     template_name = 'veld/index.html'
#     context_object_name = 'posts'
#
#     def get_queryset(self):
#         return Post.objects.filter(Q(is_published=True) & Q(end_date__gte=datetime.now()) | Q(is_published=True) & Q(end_date = None))
#
#
# class BannerHome(ListView):
#     model = Banner
#     template_name = 'veld/index.html'
#     context_object_name = 'banners'
#
#     def get_queryset(self):
#         return Banner.objects.filter(Q(is_published=True) & Q(end_date__gte=datetime.now()) | Q(is_published=True) & Q(end_date = None))

# def index(request):
#     return render(request, 'veld/index.html')

@login_required
def addappointment(request):
    form = AddAppointmentForm()

    response_data = {
        'form': form,
        'menu': menu,
    }

    return render(request, 'veld/addappointment.html', response_data)


def pricelist(request):
    response_data = {
        'menu': menu,
    }

    return render(request, 'veld/pricelist.html', response_data)


def contacts(request):
    response_data = {
        'menu': menu,
    }

    return render(request, 'veld/contacts.html', response_data)


def login(request):
    response_data = {
        'menu': menu,
    }

    return render(request, 'veld/login.html', response_data)


class RegisterUser:
    pass