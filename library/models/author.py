from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

GENRE_CHOICES = [
    ('fiction','Fiction'),
    ('non_fiction','Non Fiction'),
    ('science_fiction','Science Fiction'),
    ('fantasy','Fantasy'),
    ('mystery','Mystery'),
    ('biography','Biography'),
    ('other', 'Other')
]


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
        validators=[MinValueValidator(1), MaxValueValidator(10)],
        verbose_name='Рейтинг автора'
    )

    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=100)
    author = models.ForeignKey(
        'Author', null=True,
        on_delete=models.SET_NULL,
        related_name='books'
    )
    publish_date = models.DateField(auto_now_add=True)
    description = models.TextField(null=True, blank=True)
    genres = models.CharField(max_length=50, choices=GENRE_CHOICES, default='other')
    pages = models.PositiveSmallIntegerField(
        validators=[MaxValueValidator(10000)],
        null=True,
        blank=True)

    publisher = models.ForeignKey(
        'Publisher',
        on_delete=models.SET_NULL,
        related_name='books',
        null=True
    )
    category = models.ForeignKey(
        'Category',
        null=True,
        on_delete=models.SET_NULL,
        related_name='books'
    )

    def __str__(self):
        return self.name
