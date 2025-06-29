from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('ventas/', views.dashboard_view_ventas, name='ventas'),
    path('performance/', views.dashboard_view_performance, name='performance'),
    path('dashboard3/', views.dashboard_view_3, name='dashboard_3'),
    path('dashboard4/', views.dashboard_view_4, name='dashboard_4'),
]


