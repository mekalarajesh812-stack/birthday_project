from django.contrib import admin
from .models import Greeting

@admin.register(Greeting)
class GreetingAdmin(admin.ModelAdmin):
    list_display = ('title', 'viewed', 'view_count', 'last_viewed_at')
    readonly_fields = ('viewed', 'view_count', 'last_viewed_at')
