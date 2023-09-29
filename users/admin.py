from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .models import Contr

User = get_user_model()


# Register your models here.
@admin.register(User)
class UserAdmin(UserAdmin):
    pass


admin.site.register(Contr)
