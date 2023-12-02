from django.db import models

from users.models import User

NULLABLE = {'null': True, 'blank': True}


class Subject(models.Model):
    title = models.CharField(max_length=150, unique=True, verbose_name='Название')
    description = models.TextField(verbose_name='Описание', **NULLABLE)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Предмет'
        verbose_name_plural = 'Предметы'


class Branch(models.Model):
    title = models.CharField(max_length=150,unique=True, verbose_name='Название')
    description = models.TextField(verbose_name='Описание', **NULLABLE)

    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, verbose_name='Предмет', **NULLABLE)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Раздел'
        verbose_name_plural = 'Разделы'


class Materials(models.Model):
    title = models.CharField(max_length=300, verbose_name='Название')
    link = models.URLField(max_length=300, verbose_name='Ссылка на видео', **NULLABLE)
    text = models.TextField(verbose_name='Текст статьи', **NULLABLE)
    date_of_last_modification = models.DateField(auto_now=True, verbose_name='Дата последнего изменения', **NULLABLE)

    branch = models.ForeignKey(Branch, on_delete=models.SET_NULL, verbose_name='Раздел', **NULLABLE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Владелец', **NULLABLE)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Материалы'
        verbose_name_plural = 'Материалы'
