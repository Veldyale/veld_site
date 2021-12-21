from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from datetime import datetime

from veld.forms import *
from veld.models import *
from veld.utils import DataMixin, menu

def main_page(request):
    banners = Banner.objects.order_by('queue').filter(Q(is_published=True) & Q(end_date__gte=datetime.now()) | Q(is_published=True) & Q(end_date = None))
    posts = Post.objects.all().order_by('time_create').filter(Q(is_published=True) & Q(end_date__gte=datetime.now()) | Q(is_published=True) & Q(end_date = None))

    user_menu = menu.copy()
    if not request.user.is_authenticated:
        user_menu.pop(5)
    else:
        user_menu.pop(3)
        user_menu.pop(3)

    context = {
        'banners': banners,
        'posts': posts,
        'menu': menu,
    }

    context['menu'] = user_menu

    return render(request, 'veld/index.html', context,)


# class BannerHome(DataMixin, ListView):
#     model = Banner
#     template_name = 'veld/index.html'
#     context_object_name = 'banners'
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         c_def = self.get_user_context(title='Главная')
#         return dict(list(context.items()) + list(c_def.items()))
#
#     def get_queryset(self):
#         return Banner.objects.filter(Q(is_published=True) & Q(end_date__gte=datetime.now()) | Q(is_published=True) & Q(end_date = None))
#
#
# class PostHome(ListView):
#     model = Post
#     template_name = 'veld/index.html'
#     context_object_name = 'posts'
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         c_def = self.get_user_context(title='Главная')
#         return dict(list(context.items()) + list(c_def.items()))
#
#     def get_queryset(self):
#         return Post.objects.filter(Q(is_published=True) & Q(end_date__gte=datetime.now()) | Q(is_published=True) & Q(end_date = None))


class AddAppointment(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddAppointmentForm
    template_name = 'veld/addappointment.html'
    context_object_name = 'addappointment'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Запись')
        return dict(list(context.items()) + list(c_def.items()))

class PriceList(DataMixin, ListView):
    model = Service
    template_name = 'veld/pricelist.html'
    context_object_name = 'prices'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Цены')
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return Service.objects.all()

class Contacts(DataMixin, ListView):
    model = Service
    template_name = 'veld/contacts.html'
    context_object_name = 'contacts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Контакты')
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return Service.objects.all()

def login(request):
    response_data = {
        # 'menu': menu,
    }

    return render(request, 'veld/login.html', response_data)


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'veld/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Регистрация')
        return dict(list(context.items()) + list(c_def.items()))
