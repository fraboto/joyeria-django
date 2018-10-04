from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

# Register your models here.
class UDUserInline(admin.StackedInline):
    model       = UDUser
    can_delete  = False

class UserAdmin(BaseUserAdmin):
    inlines = (UDUserInline,)

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
