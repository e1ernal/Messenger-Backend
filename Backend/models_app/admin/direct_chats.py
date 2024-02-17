from django.contrib import admin

from models_app.models import DirectChat


@admin.register(DirectChat)
class DirectChatAdmin(admin.ModelAdmin):
    ...
