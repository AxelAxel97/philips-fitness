from django.contrib import admin
from .models import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'fitness_level', 'is_subscriber', 'created_at')
    list_filter = ('fitness_level', 'is_subscriber')
    search_fields = ('user__username', 'goal')
