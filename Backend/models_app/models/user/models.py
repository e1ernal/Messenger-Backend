from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from models_app.models.user.manager import CustomUserManager


class User(AbstractUser):
    username_validator = UnicodeUsernameValidator()

    phone_number = models.CharField(max_length=12, verbose_name='Номер телефона', unique=True)
    image = models.ImageField(upload_to='users/', verbose_name='Изображение')
    username = models.CharField(
        _('username'),
        unique=True,
        max_length=150,
        help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[username_validator],
        error_messages={
            'unique': _("A user with that username already exists."),
        },
    )
    public_key = models.CharField(max_length=255, verbose_name='Публичный ключ')

    USERNAME_FIELD = 'phone_number'

    objects = CustomUserManager()

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'users'
        app_label = 'models_app'
        verbose_name = 'User'
        verbose_name_plural = 'Users'
