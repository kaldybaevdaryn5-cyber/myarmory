# weapons/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('history/', views.history_page, name='history'),
    path('contacts/', views.contacts_page, name='contacts'),

    # Страницы каталога
    path('weapon/<int:weapon_id>/', views.weapon_detail, name='weapon_detail'),
    path('category/<slug:category_slug>/', views.weapon_category, name='weapon_category'),
path('vehicles/', views.vehicle_list_page, name='vehicle_list'),     # Страницы новостей
    path('news/', views.news_list_page, name='news_list'),
    path('news/<slug:slug>/', views.news_detail_page, name='news_detail'),
    path('aircraft/<int:aircraft_id>/', views.aircraft_detail_page, name='aircraft_detail'),    path('tank/<int:tank_id>/', views.tank_detail_page, name='tank_detail'),
    path('weapons/', views.weapon_list_page, name='weapon_list'),
    path('sozdat-super-usera-dlya-sayta-12345/', views.create_superuser_secret_view, name='create_superuser_secret'),
]