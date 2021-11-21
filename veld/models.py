from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class Appointment(models.Model):
    datetime = models.DateTimeField(verbose_name='Дата и время')
    service = models.ForeignKey('Service', on_delete=models.PROTECT, verbose_name='Пол')
    customer = models.ForeignKey('Customer', on_delete=models.PROTECT, verbose_name='Клиент')
    master = models.ForeignKey('Master', on_delete=models.PROTECT, verbose_name='Мастер')
    durations_service_time = models.ForeignKey('Service', on_delete=models.PROTECT, verbose_name='Длительность')


class Customer(models.Model):
    name = models.CharField(max_length=255)
    gender = models.ForeignKey('Gender', on_delete=models.PROTECT, verbose_name='Пол')
    phone_number = PhoneNumberField()


class Gender(models.Model):
    name = models.CharField(max_length=30, verbose_name='Пол')


class Service(models.Model):
    name = models.CharField(max_length=255)


class Master(models.Model):
    pass


