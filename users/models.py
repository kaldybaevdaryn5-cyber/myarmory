from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # ▼▼▼ ИЗМЕНИ ЭТУ СТРОЧКУ, ДОБАВИВ blank=True ▼▼▼
    image = models.ImageField(default='profile_pics/default.jpg', upload_to='profile_pics', verbose_name="Аватар", blank=True)

    def __str__(self):
        return f'Профиль пользователя {self.user.username}'