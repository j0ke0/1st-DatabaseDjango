from . import views
from django.urls import path

app_name = 'mysites'
urlpatterns = [
    path('', views.index, name='index'),
    path('client/', views.client, name='client'),
    path('info/', views.info, name='info'),
    path('entry/', views.entry, name= 'entry'),
    path('edit_info/<str:pk>/', views.edit_info, name='edit_info'),
    path('delete/<str:pk>/', views.delete, name='delete'),
    path('add_plan', views.add_plan, name='add_plan'),
    path('delete_plan_info/<str:pk>/', views.delete_plan_info, name='delete_plan_info'),
    path('open_plan_info/', views.open_plan_info, name='open_plan_info'),
    path('edit_plan/<str:pk>/', views.edit_plan, name='edit_plan'),
    path('del_plan/<str:pk>/', views.del_plan, name='del_plan'),
    path('add_profile/', views.add_profile, name='add_profile'),
    path('verify_del/<str:pk>/', views.verify_del, name='verify_del'),
    path('announcement/', views.announcement, name='announcement'),
    path('del_announce/<str:pk>/', views.del_announce, name='del_announce'),
    path('edit_announce/<str:pk>/', views.edit_announce, name='edit_announce'),
    path('customer/', views.customer_view, name='customer_view'),
    path('portfolio/<str:pk>/', views.portfolio, name='portfolio'),
    ]
    