from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Author(models.Model):

    name = models.CharField(max_length=100, verbose_name='Имя автора')
    surname = models.CharField(max_length=100, verbose_name='Фамилия автора')
    birth_date = models.DateField(verbose_name='Дата рождения')
    profile = models.URLField(max_length=255, null=True, blank=True, verbose_name='Ссылка на профиль')
    deleted = models.BooleanField(
        default=False,
        verbose_name='Удалено',
        help_text='Если True аккаунт удален, если False аккаунт активен'
    )
    rating = models.FloatField(
        default=1,
        validators=[MinValueValidator(1),MaxValueValidator(10)],
        verbose_name='Рейтинг автора'
    )
