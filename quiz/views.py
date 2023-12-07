from django.shortcuts import render, get_list_or_404
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from quiz.models import Quiz, Question
from quiz.serializers import QuizSerializer, QuestionSerializer


class MaterialQuizListAPIView(generics.ListAPIView):
    """Список тестов относящихся к указанному материалу(необходимо передать его pk)"""
    serializer_class = QuizSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Quiz.objects.filter(material=self.kwargs['pk'])
        return queryset


class QuizQuestionsListAPIView(generics.ListAPIView):
    """Список вопросов относящихся к указанному тесту(Quiz)(необходимо передать его pk)"""
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = get_list_or_404(Question, quiz=self.kwargs['pk'])
        return queryset




