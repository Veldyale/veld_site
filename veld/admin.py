from django.contrib import admin
from .models import *


class AppointmentAdmin(admin.ModelAdmin):
    list_display = ("id", "customer", "service", "datetime",)
    list_display_links = ("id", "customer", "service", "datetime",)
    # list_filter = ("is_published", "time_create",)
    # search_fields = ("id", "title", "time_create",)
    # list_editable = ("is_published",)
    # prepopulated_fields = {"slug": ("title",)}


class CustomerAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "phone_number", "gender",)
    list_display_links = ("id", "name",)
    # list_filter = ("id", "name",)
    # search_fields = ("id", "name",)
    # prepopulated_fields = {"slug": ("name",)}


class ServiceAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "price", "durations_service_time",)
    list_display_links = ("id", "name",)
    # list_filter = ("id", "name",)
    # search_fields = ("id", "name",)
    # prepopulated_fields = {"slug": ("name",)}


class GenderAdmin(admin.ModelAdmin):
    list_display = ("name",)
    list_display_links = ("name",)
    # list_filter = ("id", "name",)
    # search_fields = ("id", "name",)
    # prepopulated_fields = {"slug": ("name",)}


class MasterAdmin(admin.ModelAdmin):
    list_display = ("name",)
    list_display_links = ("name",)
    # list_filter = ("id", "name",)
    # search_fields = ("id", "name",)
    # prepopulated_fields = {"slug": ("name",)}


admin.site.register(Appointment, AppointmentAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Gender, GenderAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Master, MasterAdmin)
