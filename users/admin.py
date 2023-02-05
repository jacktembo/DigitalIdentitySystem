from django.contrib import admin

from .models import *


@admin.register(UserDetails)
class UserDetailsAdmin(admin.ModelAdmin):
    pass