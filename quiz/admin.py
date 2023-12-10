from django.contrib import admin

from quiz.models import Quiz, Question, Choice, StudentAnswer


@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'material', 'owner', 'created',)
    list_filter = ('material', 'owner',)


class ChoiceInlineModel(admin.TabularInline):
    model = Choice
    fields = ('choice_text', 'is_right')


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    fields = ('quiz', 'question_text',)
    list_display = ('pk', 'quiz', 'question_text',)
    list_filter = ('quiz',)
    inlines = (ChoiceInlineModel,)


@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('choice_text', 'is_right', 'question',)
    list_filter = ('question', 'is_right')


@admin.register(StudentAnswer)
class StudentAnswerAdmin(admin.ModelAdmin):
    list_display = ('pk', 'quiz', 'student', 'question', 'choice',)
    list_filter = ('student', 'quiz', 'question',)
