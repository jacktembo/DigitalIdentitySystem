from django.contrib import admin

from .models import *

admin.AdminSite.index_title = 'Digital Identity System Administration'
admin.AdminSite.site_header = 'Digital Identity'
admin.AdminSite.site_title = 'Digital Identity'


@admin.register(UserDetails)
class UserDetailsAdmin(admin.ModelAdmin):
    pass

@admin.register(OtherUserDetails)
class OtherUserDetailsAdmin(admin.ModelAdmin):
    pass