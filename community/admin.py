from django.contrib import admin
from .models import SuccessPost

@admin.register(SuccessPost)
class SuccessPostAdmin(admin.ModelAdmin):
    list_display = ('user', 'created_at')
    search_fields = ('user__username', 'content')
