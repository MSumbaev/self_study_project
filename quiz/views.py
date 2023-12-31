from django.shortcuts import get_list_or_404
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from quiz.models import Quiz, Question, StudentAnswer
from quiz.serializers import QuizSerializer, QuestionSerializer, StudentAnswerSerializer, ReportSerializer


class MaterialQuizListAPIView(generics.ListAPIView):
    """Список тестов относящихся к указанному материалу(необходимо передать его pk)"""
    serializer_class = QuizSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Quiz.objects.filter(material=self.kwargs['material_pk'])
        return queryset


class QuizQuestionsListAPIView(generics.ListAPIView):
    """Список вопросов относящихся к указанному тесту(Quiz)(необходимо передать его pk в url)"""
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = get_list_or_404(Question, quiz=self.kwargs['quiz_id'])
        return queryset


class SubmitStudentAnswers(APIView):
    """Эндпоинт отправки ответов студента на для опроса(Quiz)(необходимо передать его pk в url)."""
    permission_classes = [IsAuthenticated]

    def post(self, request: Request, quiz_id: int):
        """Сохранение ответов студента.

        Пример post-запроса:
        {
            "answers": [
                {
                    "id": 1, # id вопроса
                    "choice": 1 # id ответа
                },
                        {
                    "id": 2, # id вопроса
                    "choice": 5 # id ответа
                },
                        {
                    "id": 3, # id вопроса
                    "choice": 8 # id ответа
                }
            ]
        }
    """
        questions_count = Question.objects.filter(quiz=quiz_id).count()

        if len(request.data['answers']) != questions_count:
            raise ValueError(
                "необходимо ответить на все вопросы!"
            )

        if StudentAnswer.objects.filter(quiz=quiz_id, student=self.request.user.pk):
            StudentAnswer.objects.filter(quiz=quiz_id, student=self.request.user.pk).delete()

        answers_ = self.parse_request(request, quiz_id)
        serialized_answers = StudentAnswerSerializer(data=answers_, many=True)

        if serialized_answers.is_valid(raise_exception=True):
            serialized_answers.save()
            return Response(serialized_answers.data, status=status.HTTP_201_CREATED)
        return Response(serialized_answers.errors, status=status.HTTP_400_BAD_REQUEST)

    def parse_request(self, request: Request, quiz_id: int):
        """Parse answers"""
        parsed_answers = []
        for question in request.data['answers']:
            answer = dict()
            answer['quiz'] = quiz_id
            answer['student'] = self.request.user.pk
            answer['question'] = question['id']
            answer['choice'] = question['choice']
            parsed_answers.append(answer.copy())
        return parsed_answers


class ReportDetailAPIView(generics.RetrieveAPIView):
    """
    Эндпоинт вывода отчета на пройденный опрос.

    Пример ответа на запрос:
    {
        "title": "Фазовые превращения Тест №1",
        "material": 2,
        "num_right_answers": "Вы ответили правильно на 2 вопросов из 3!"
    }
    """
    serializer_class = ReportSerializer
    queryset = Quiz.objects.all()
    permission_classes = [IsAuthenticated]
