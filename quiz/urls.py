from django.urls import path

from quiz.apps import QuizConfig
from quiz.views import MaterialQuizListAPIView, QuizQuestionsListAPIView, AnswerTrakerView, \
    ReportDetailAPIView

app_name = QuizConfig.name

urlpatterns = [
    path('<int:material_pk>/quiz_list/', MaterialQuizListAPIView.as_view(), name='quiz_list'),
    path('quiz/<int:quiz_id>/', QuizQuestionsListAPIView.as_view(), name='quiz_detail'),
    path('quiz/<int:quiz_id>/answers/', AnswerTrakerView.as_view(), name='post_answers'),
    path('quiz/<int:pk>/report/', ReportDetailAPIView.as_view(), name='report'),
]
