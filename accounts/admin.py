from accounts.models import User
from django.contrib import admin


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass
