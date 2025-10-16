# weapons/admin.py
from django.contrib import admin
# ▼▼▼ ИСПРАВЬ ЭТУ СТРОЧКУ ▼▼▼
from .models import Weapon, WeaponType, Manufacturer, HistoricalEra, HistoricalWeapon, NewsArticle, Tank, Aircraft
# --- Админка для основного каталога ---

@admin.register(Weapon)
class WeaponAdmin(admin.ModelAdmin):
    list_display = ('name', 'weapon_type', 'manufacturer', 'caliber')
    list_filter = ('weapon_type', 'manufacturer')
    search_fields = ('name', 'description')

@admin.register(WeaponType)
class WeaponTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    # Эта строчка автоматически заполняет поле slug на основе названия. Очень удобно!
    prepopulated_fields = {'slug': ('name',)} 

@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ('name', 'country')


# --- Админка для страницы "История" ---

class HistoricalWeaponInline(admin.StackedInline):
    """Позволяет добавлять оружие прямо на странице редактирования эпохи."""
    model = HistoricalWeapon
    extra = 1 # Количество пустых форм для добавления

@admin.register(HistoricalEra)
class HistoricalEraAdmin(admin.ModelAdmin):
    """Админка для управления эпохами."""
    list_display = ('year', 'title')
    inlines = [HistoricalWeaponInline] # Подключаем инлайн

@admin.register(NewsArticle)
class NewsArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'published_date')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}

# ▼▼▼ ДОБАВЬ ЭТОТ КОД В КОНЕЦ ФАЙЛА ▼▼▼
@admin.register(Tank)
class TankAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', 'main_armament')

@admin.register(Aircraft)
class AircraftAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', 'max_speed')