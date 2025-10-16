# weapons/serializers.py
from rest_framework import serializers
from .models import Weapon, Manufacturer, WeaponType

class WeaponSerializer(serializers.ModelSerializer):
    # Чтобы вместо ID производителя выводилось его имя
    manufacturer_name = serializers.CharField(source='manufacturer.name', read_only=True)
    # Чтобы вместо ID типа оружия выводилось его название
    weapon_type_name = serializers.CharField(source='weapon_type.name', read_only=True)

    class Meta:
        model = Weapon
        # Указываем, какие поля из модели Weapon мы хотим видеть в JSON
        fields = ['id', 'name', 'description', 'caliber', 'fire_rate', 'effective_range', 'image', 'manufacturer_name', 'weapon_type_name']