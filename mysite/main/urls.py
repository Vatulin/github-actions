from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('health/', views.health_check, name='health_check'),
    path('volumes/', views.volume_info, name='volume_info'),
    path('api/data/', views.admin_data_api, name='admin_data_api'),
]