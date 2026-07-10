from django.contrib import admin
from django.urls import path, include
from shop import views as shop_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', shop_views.home, name='home'),
    path('shop/', include('shop.urls')),
    path('accounts/', include('accounts.urls')),
    path('community/', include('community.urls')),
    path('subscriptions/', include('subscriptions.urls')),
]
