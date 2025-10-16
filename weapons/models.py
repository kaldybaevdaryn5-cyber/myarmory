# weapons/models.py
#
from django.db import models

class WeaponType(models.Model):
    name = models.CharField(max_length=100, verbose_name="Тип оружия") # Это поле у тебя уже есть
    
    # --- ВОТ ЭТИ ДВА ПОЛЯ НУЖНО ДОБАВИТЬ ---
    description = models.TextField(verbose_name="Краткое описание", blank=True)
    icon_filename = models.CharField(max_length=50, verbose_name="Имя файла иконки (из static/images/)", default='icon-rifle.svg')
    slug = models.SlugField(max_length=100, unique=True, db_index=True, verbose_name="URL (slug)", default='default-slug')    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Тип оружия"
        verbose_name_plural = "Типы оружия"

class Manufacturer(models.Model):
    name = models.CharField(max_length=100, verbose_name="Производитель") 
    country = models.CharField(max_length=100, verbose_name="Страна")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Производитель"
        verbose_name_plural = "Производители"

class Weapon(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, related_name="weapons", verbose_name="Производитель")
    weapon_type = models.ForeignKey(WeaponType, on_delete=models.PROTECT, related_name="weapons", verbose_name="Тип оружия")
    caliber = models.CharField(max_length=50, verbose_name="Калибр")
    fire_rate = models.PositiveIntegerField(verbose_name="Скорострельность (выстр/мин)")
    effective_range = models.PositiveIntegerField(verbose_name="Эффективная дальность (м)")
    #image = models.ImageField(upload_to='weapons_images/', verbose_name="Изображение оружия")
    #bullet_image = models.ImageField(upload_to='bullets_images/', verbose_name="Изображение патрона", blank=True, null=True)
    model_path = models.CharField(max_length=200, blank=True, null=True, verbose_name="Путь к 3D модели (от папки static)")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Оружие"
        verbose_name_plural = "Оружие"
# weapons/models.py

# ... (модели WeaponType, Manufacturer, Weapon остаются без изменений) ...


# ▼▼▼ ДОБАВЬ ЭТИ ДВА НОВЫХ КЛАССА В КОНЕЦ ФАЙЛА ▼▼▼

class HistoricalEra(models.Model):
    """Модель для исторической эпохи (узла на временной шкале)."""
    year = models.CharField(max_length=50, verbose_name="Год или период (напр., 'XV век')")
    title = models.CharField(max_length=200, verbose_name="Название эпохи")
    description = models.TextField(verbose_name="Описание эпохи")
    #era_image = models.ImageField(upload_to='history_images/', blank=True, null=True, verbose_name="Фоновое изображение для карточки")
    
     # ▼▼▼ ДОБАВЬ ЭТО НОВОЕ ПОЛЕ ▼▼▼
    sort_order = models.IntegerField(default=0, verbose_name="Порядок сортировки (чем меньше, тем раньше)")

    class Meta:
        verbose_name = "Историческая эпоха"
        verbose_name_plural = "Исторические эпохи"
        # ▼▼▼ И ИЗМЕНИ СОРТИРОВКУ ЗДЕСЬ ▼▼▼
        ordering = ['sort_order'] # Теперь сортируем по числовому полю
    def __str__(self):
        return self.title

class HistoricalWeapon(models.Model):
    """Модель для конкретного оружия внутри исторической эпохи."""
    era = models.ForeignKey(HistoricalEra, on_delete=models.CASCADE, related_name="historical_weapons", verbose_name="Эпоха")
    name = models.CharField(max_length=200, verbose_name="Название оружия")
    description = models.TextField(verbose_name="Краткая история")
    #weapon_image = models.ImageField(upload_to='history_images/', verbose_name="Изображение оружия")

    class Meta:
        verbose_name = "Историческое оружие"
        verbose_name_plural = "Историческое оружие"

    def __str__(self):
        return self.name

# ▼▼▼ ДОБАВЬ ЭТОТ НОВЫЙ КЛАСС В КОНЕЦ ФАЙЛА ▼▼▼

class NewsArticle(models.Model):
    """Модель для новостной статьи."""
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    slug = models.SlugField(max_length=200, unique=True, verbose_name="URL (slug)")
    content = models.TextField(verbose_name="Содержание статьи")
    published_date = models.DateTimeField(auto_now_add=True, verbose_name="Дата публикации")
    #image = models.ImageField(upload_to='news_images/', blank=True, null=True, verbose_name="Изображение")

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"
        ordering = ['-published_date'] # Сортировка: новые новости сверху

    def __str__(self):
        return self.title

# ▼▼▼ ДОБАВЬ ЭТИ НОВЫЕ КЛАССЫ В КОНЕЦ ФАЙЛА ▼▼▼

class Tank(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    country = models.CharField(max_length=100, verbose_name="Страна")
    
    main_armament = models.CharField(max_length=100, verbose_name="Основное вооружение")
    armor = models.CharField(max_length=100, verbose_name="Броня (мм)")
    max_speed = models.PositiveIntegerField(verbose_name="Макс. скорость (км/ч)")
    
    #image = models.ImageField(upload_to='tanks_images/', verbose_name="Изображение")
    model_path = models.CharField(max_length=200, blank=True, null=True, verbose_name="Путь к 3D модели (от папки static)")
    
    class Meta:
        verbose_name = "Танк"
        verbose_name_plural = "Танки"

    def __str__(self):
        return self.name

class Aircraft(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    country = models.CharField(max_length=100, verbose_name="Страна")

    armament = models.TextField(verbose_name="Вооружение")
    max_speed = models.PositiveIntegerField(verbose_name="Макс. скорость (км/ч)")
    ceiling = models.PositiveIntegerField(verbose_name="Практический потолок (м)") # Высота

    #image = models.ImageField(upload_to='aircraft_images/', verbose_name="Изображение")
    model_path = models.CharField(max_length=200, blank=True, null=True, verbose_name="Путь к 3D модели (от папки static)")

    class Meta:
        verbose_name = "Летательный аппарат"
        verbose_name_plural = "Летательные аппараты"

    def __str__(self):
        return self.name
####