from rest_framework import serializers

from quiz.models import Quiz, Choice, Question, StudentAnswer


class QuizSerializer(serializers.ModelSerializer):
    """Сериализатор модели Quiz"""
    class Meta:
        model = Quiz
        fields = '__all__'


class ChoiceSerializer(serializers.ModelSerializer):
    """Сериализатор модели Choice"""
    class Meta:
        model = Choice
        fields = ['id', 'choice_text', 'is_right']


class QuestionSerializer(serializers.ModelSerializer):
    """Сериализатор модели Question"""
    choice_set = ChoiceSerializer(many=True, read_only=True, required=False)

    class Meta:
        model = Question
        fields = ['id', 'question_text', 'question_type', 'choice_set']


class AnswerTrackerSerializer(serializers.ModelSerializer):
    """Сериализатор модели StudentAnswer"""
    class Meta:
        model = StudentAnswer
        fields = '__all__'
