# config/urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# ▼▼▼ ДОБАВЬ ЭТИ ИМПОРТЫ ▼▼▼
from rest_framework import routers
from weapons import views as weapon_views

# ▼▼▼ ДОБАВЬ ЭТОТ КОД ▼▼▼
# Создаем роутер и регистрируем в нем наш вьюсет
router = routers.DefaultRouter()
router.register(r'weapons', weapon_views.WeaponViewSet, basename='weapon')

# ▼▼▼ ИЗМЕНИ urlpatterns ▼▼▼
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('weapons.urls')),
    path('users/', include('users.urls')),
    
    # Добавляем URL-адреса для API
    path('api/', include(router.urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)