from django.contrib import admin
from django.contrib.auth import get_user_model

User = get_user_model()


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    readonly_fields = ["followers"]

    def followers(self, instance):
        return instance.follower_set.all()
