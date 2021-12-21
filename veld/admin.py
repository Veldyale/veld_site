from django.contrib import admin
from django.utils.safestring import mark_safe
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin, UserAdmin
from django.contrib.auth.models import User
from django.contrib import auth
# from django.contrib.auth import get_user_model

from .models import *
from .forms import *


class BannerAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "time_create", "get_html_photo", "queue", "is_published", "end_date",)
    list_display_links = ("id", "title", "time_create", "get_html_photo")
    list_filter = ("is_published", "time_create", "queue", "end_date",)
    search_fields = ("id", "title", "time_create", "end_date",)
    list_editable = ("is_published", "end_date", "queue",)
    # prepopulated_fields = {"slug": ("title",)}

    def get_html_photo(self, object):
        return mark_safe(f"<img src='{object.image_mobile.url}' width=50>")


class PostAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "time_create", "get_html_photo", "is_published", "end_date",)
    list_display_links = ("id", "title", "time_create",)
    list_filter = ("is_published", "time_create",)
    search_fields = ("id", "title", "time_create",)
    list_editable = ("is_published", "end_date",)
    # prepopulated_fields = {"slug": ("title",)}

    def get_html_photo(self, object):
        return mark_safe(f"<img src='{object.image.url}' width=50>")


class AppointmentAdmin(admin.ModelAdmin):
    list_display = ("id", "service", "datetime",)
    list_display_links = ("id", "service", "datetime",)
    # list_filter = ("is_published", "time_create",)
    # search_fields = ("id", "title", "time_create",)
    # list_editable = ("is_published",)
    # prepopulated_fields = {"slug": ("title",)}


class CustomerAdmin(admin.StackedInline):
    model = Customer
    can_delete = False
    verbose_name_plural = 'Клиент'
    list_display = ("name", "phone",)
    # list_display_links = ("id", "name",)
    # list_filter = ("id", "name",)
    # search_fields = ("id", "name",)
    # prepopulated_fields = {"slug": ("name",)}

class UserAdmin(BaseUserAdmin):
    inlines = (CustomerAdmin,)


class ServiceAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "price", "durations_service_time",)
    list_display_links = ("id", "name",)
    # list_filter = ("id", "name",)
    # search_fields = ("id", "name",)
    # prepopulated_fields = {"slug": ("name",)}


class MasterAdmin(admin.ModelAdmin):
    list_display = ("name",)
    list_display_links = ("name",)
    # list_filter = ("id", "name",)
    # search_fields = ("id", "name",)
    # prepopulated_fields = {"slug": ("name",)}


class LinkAdmin(admin.ModelAdmin):
    list_display = ("name",)
    list_display_links = ("name",)


admin.site.register(Appointment, AppointmentAdmin)
# admin.site.register(Customer, CustomerAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Master, MasterAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Banner, BannerAdmin)
admin.site.register(Link, LinkAdmin)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.unregister(auth.models.Group)
