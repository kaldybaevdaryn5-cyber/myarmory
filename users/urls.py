# users/urls.py
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
# ▼▼▼ ДОБАВЬ ЭТОТ НОВЫЙ ИМПОРТ ▼▼▼
from django.views.decorators.csrf import csrf_protect

urlpatterns = [
    path('register/', views.register, name='register'),
    
    # ▼▼▼ ИЗМЕНИ ЭТУ СТРОЧКУ ▼▼▼
    path('login/', csrf_protect(auth_views.LoginView.as_view(template_name='users/login.html')), name='login'),
    
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('profile/', views.profile_page, name='profile'),
    path('settings/', views.settings_page, name='settings'),
]