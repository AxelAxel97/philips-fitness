from django.urls import path
from . import views

urlpatterns = [
    path('', views.subscribe_page, name='subscribe'),
    path('checkout/', views.create_checkout_session, name='create_checkout_session'),
    path('success/', views.subscription_success, name='subscription_success'),
    path('cancel/', views.subscription_cancel, name='subscription_cancel'),
]
