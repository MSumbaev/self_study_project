from django.core.exceptions import ValidationError
from django.db import models

from education.models import Material
from users.models import User

NULLABLE = {'null': True, 'blank': True}


class Quiz(models.Model):
    """Модель теста/опроса"""
    title = models.CharField(max_length=300, verbose_name='Название')
    created = models.DateField(auto_now_add=True, verbose_name='Дата создания')

    material = models.ForeignKey(Material, on_delete=models.CASCADE, verbose_name='Материал', **NULLABLE)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, verbose_name='Владелец', **NULLABLE)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Тест'
        verbose_name_plural = 'Тесты'


class Question(models.Model):
    """Модель вопроса"""
    quiz = models.ForeignKey(Quiz, on_delete=models.SET_NULL, verbose_name='Тест', **NULLABLE)
    question_text = models.CharField(max_length=1000, verbose_name='Текст вопроса')

    def __str__(self):
        return f'{self.question_text}'

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'


class Choice(models.Model):
    """Модель ответа"""
    question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name='Вопрос', **NULLABLE)
    choice_text = models.CharField(max_length=1000, verbose_name='Текст ответа')
    is_right = models.BooleanField(default=False, verbose_name='Правильность ответа')

    def __str__(self):
        return f'{self.choice_text}'

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответ'


class StudentAnswer(models.Model):
    """Модель ответа студента"""
    quiz = models.ForeignKey(Quiz, on_delete=models.SET_NULL, verbose_name='Тест', **NULLABLE)
    student = models.ForeignKey(User, on_delete=models.SET_NULL, verbose_name='Студент', **NULLABLE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name='Вопрос', **NULLABLE)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE, verbose_name='Текст ответа', **NULLABLE)

    def __str__(self):
        return f'{self.student} - {self.question} - {self.choice}'

    class Meta:
        verbose_name = 'Ответ студента'
        verbose_name_plural = 'Ответ студента'
