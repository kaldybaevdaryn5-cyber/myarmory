# weapons/views.py
from django.shortcuts import render, get_object_or_404
from .models import Weapon, WeaponType, HistoricalEra, NewsArticle, Tank, Aircraft

# API imports
from rest_framework import viewsets
from .serializers import WeaponSerializer

# --- Views for main site functionality ---

def home_page(request):
    """Отображает главную страницу со всем оружием и категориями."""
    all_weapons = Weapon.objects.all()
    all_types = WeaponType.objects.all()
    context = {
        'weapons': all_weapons,
        'weapon_types': all_types,
    }
    return render(request, 'weapons/home.html', context)

# ▼▼▼ ДОБАВЬ ЭТУ НОВУЮ ФУНКЦИЮ ▼▼▼


# ▼▼▼ ЗАМЕНИ СТАРУЮ weapon_detail НА ЭТУ ▼▼▼
def weapon_detail(request, weapon_id):
    # Находим наше оружие
    weapon = get_object_or_404(Weapon, pk=weapon_id) 
    
    # Находим другое оружие из той же категории, исключая текущее
    related_weapons = Weapon.objects.filter(weapon_type=weapon.weapon_type).exclude(pk=weapon_id)[:3] # Берем 3 похожих

    context = {
        'weapon': weapon,
        'related_weapons': related_weapons,
    }
    return render(request, 'weapons/weapon_detail.html', context)

def weapon_category(request, category_slug):
    """Отображает страницу со списком оружия в определенной категории."""
    category = get_object_or_404(WeaponType, slug=category_slug)
    weapons_in_category = Weapon.objects.filter(weapon_type=category)
    context = {
        'category': category,
        'weapons': weapons_in_category,
    }
    return render(request, 'weapons/category.html', context)

def history_page(request):
    """Отображает динамическую страницу 'История' из базы данных."""
    # Получаем все эпохи, отсортированные по году
    all_eras = HistoricalEra.objects.all()
    context = {
        'eras': all_eras
    }
    return render(request, 'weapons/history.html', context)

def contacts_page(request):
    """Отображает статичную страницу 'Контакты'."""
    return render(request, 'weapons/contacts.html')

# ▼▼▼ ЗАМЕНИ СЛОЖНУЮ news_list_page НА ЭТУ ПРОСТУЮ ВЕРСИЮ ▼▼▼
def news_list_page(request):
    """Отображает страницу со списком всех новостей."""
    articles = NewsArticle.objects.all()
    context = {
        'articles': articles
    }
    return render(request, 'weapons/news_list.html', context)

def news_detail_page(request, slug):
    """Отображает детальную страницу для одной новости."""
    article = get_object_or_404(NewsArticle, slug=slug)
    context = {
        'article': article
    }
    return render(request, 'weapons/news_detail.html', context)

# ▼▼▼ ДОБАВЬ ЭТУ НОВУЮ ФУНКЦИЮ ▼▼▼
def weapon_list_page(request):
    """Отображает страницу-каталог всего оружия."""
    all_weapons = Weapon.objects.all().order_by('name')
    all_types = WeaponType.objects.all()
    context = {
        'weapons': all_weapons,
        'weapon_types': all_types,
    }
    return render(request, 'weapons/weapon_list.html', context)

def tank_detail_page(request, tank_id):
    """Отображает детальную страницу для одного танка."""
    tank = get_object_or_404(Tank, pk=tank_id)
    context = {
        'tank': tank
    }
    return render(request, 'weapons/tank_detail.html', context)

def vehicle_list_page(request):
    """Отображает единую страницу для всей техники (танки, авиация)."""
    all_tanks = Tank.objects.all().order_by('name')
    all_aircrafts = Aircraft.objects.all().order_by('name')
    context = {
        'tanks': all_tanks,
        'aircrafts': all_aircrafts,
    }
    return render(request, 'weapons/vehicle_list.html', context)

def aircraft_detail_page(request, aircraft_id):
    """Отображает детальную страницу для одного летательного аппарата."""
    aircraft = get_object_or_404(Aircraft, pk=aircraft_id)
    context = {
        'aircraft': aircraft
    }
    return render(request, 'weapons/aircraft_detail.html', context)
# --- ViewSet для API ---

class WeaponViewSet(viewsets.ReadOnlyModelViewSet):
    """API эндпоинт, который позволяет просматривать оружие."""
    queryset = Weapon.objects.all().order_by('name')
    serializer_class = WeaponSerializer