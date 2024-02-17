from django.contrib import admin

from models_app.models import Message


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    ...
