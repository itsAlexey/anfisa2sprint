from django.db import models


class PublishedModel(models.Model):
    """Абстрактная модель. Добвляет флаг is_published."""
    is_published = models.BooleanField(default=True, verbose_name='Опубликованно')

    class Meta:
        abstract = True
