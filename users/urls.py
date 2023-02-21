from . import views
from django.urls import path, include

app_name = 'users'
urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('register/', views.register, name='register'),
    path('activate_acc/<str:pk>/', views.activate_acc, name='activate_acc'),
    path('activate_dec/<str:pk>/', views.activate_dec, name='activate_dec'),
    
]
