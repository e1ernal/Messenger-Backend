from django.contrib import admin

from models_app.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('phone_number',)
