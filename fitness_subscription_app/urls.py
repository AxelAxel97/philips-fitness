from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('shop.urls')),
    path('accounts/', include('accounts.urls')),
    path('community/', include('community.urls')),
    path('subscriptions/', include('subscriptions.urls')),
]
