import datetime

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from quiz.models import Quiz, Question, Choice, StudentAnswer
from education.models import Subject, Branch, Material
from users.models import User


class MaterialQuizListTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(
            email='student@lms.com',
            password='test'
        )
        self.owner = User.objects.create(
            email='owner@lms.com',
            password='test'
        )
        self.subject = Subject.objects.create(
            title='Test subject',
            description='Test description',
        )
        self.branch = Branch.objects.create(
            title='Test branch',
            description='Test description',
            subject=self.subject
        )
        self.material = Material.objects.create(
            title='Test material',
            text='Test text',
            branch=self.branch,
            owner=self.owner
        )
        self.quiz = Quiz.objects.create(
            title='Test quiz',
            material=self.material,
            owner=self.owner
        )

    def test_list_quiz(self):
        self.client.force_authenticate(user=self.user)

        response = self.client.get(
            reverse('quiz:quiz_list',
                    args=[self.material.pk])
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            [
                {
                    'id': self.quiz.pk,
                    'title': 'Test quiz',
                    'created': datetime.date.today().strftime('%Y-%m-%d'),
                    'material': self.material.pk,
                    'owner': self.owner.pk
                }
            ]
        )


class QuizQuestionListTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(
            email='student@lms.com',
            password='test'
        )
        self.owner = User.objects.create(
            email='owner@lms.com',
            password='test'
        )
        self.subject = Subject.objects.create(
            title='Test subject',
            description='Test description',
        )
        self.branch = Branch.objects.create(
            title='Test branch',
            description='Test description',
            subject=self.subject
        )
        self.material = Material.objects.create(
            title='Test material',
            text='Test text',
            branch=self.branch,
            owner=self.owner
        )
        self.quiz = Quiz.objects.create(
            title='Test quiz',
            material=self.material,
            owner=self.owner
        )
        self.question = Question.objects.create(
            quiz=self.quiz,
            question_text='Question test',
        )
        self.choice1 = Choice.objects.create(
            question=self.question,
            choice_text='Choice 1',
            is_right=False
        )
        self.choice2 = Choice.objects.create(
            question=self.question,
            choice_text='Choice 1',
            is_right=True
        )

    def test_list_question(self):
        self.client.force_authenticate(user=self.user)

        response = self.client.get(
            reverse('quiz:quiz_detail',
                    args=[self.quiz.pk])
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            [
                {
                    'id': self.question.pk,
                    'question_text': 'Question test',
                    'choice_set': [
                        {
                            'id': self.choice1.pk,
                            'choice_text': 'Choice 1'
                        },
                        {
                            'id': self.choice2.pk,
                            'choice_text': 'Choice 1'
                        }
                    ]
                }
            ]
        )


# class SubmitStudentAnswersTestCase(APITestCase):
#     def setUp(self):
#         self.user = User.objects.create(
#             email='student@lms.com',
#             password='test'
#         )
#         self.owner = User.objects.create(
#             email='owner@lms.com',
#             password='test'
#         )
#         self.subject = Subject.objects.create(
#             title='Test subject',
#             description='Test description',
#         )
#         self.branch = Branch.objects.create(
#             title='Test branch',
#             description='Test description',
#             subject=self.subject
#         )
#         self.material = Material.objects.create(
#             title='Test material',
#             text='Test text',
#             branch=self.branch,
#             owner=self.owner
#         )
#         self.quiz = Quiz.objects.create(
#             title='Test quiz',
#             material=self.material,
#             owner=self.owner
#         )
#         self.question = Question.objects.create(
#             quiz=self.quiz,
#             question_text='Question test',
#         )
#         self.choice1 = Choice.objects.create(
#             question=self.question,
#             choice_text='Choice 1',
#             is_right=False
#         )
#         self.choice2 = Choice.objects.create(
#             question=self.question,
#             choice_text='Choice 1',
#             is_right=True
#         )
#
#     def test_submit_student_answers(self):
#         self.client.force_authenticate(user=self.user)
#
#         data = {
#             "answers": [
#                 {
#                     "id": 2,
#                     "choice": 1
#                 }
#             ]
#         }
#
#         print(Quiz.objects.get(id=self.quiz.pk))
#         print(Question.objects.get(quiz=self.quiz).__dict__)
#
#         response = self.client.post(
#             reverse('quiz:post_answers', args=[self.quiz.pk]),
#             data=data
#         )
#
#         self.assertEqual(
#             response.status_code,
#             status.HTTP_201_CREATED
#         )
#
#         print(response.json())
#
#         self.assertEqual(
#             response.json(),
#             [
#
#             ]
#         )


class ReportDetailTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(
            email='student@lms.com',
            password='test'
        )
        self.owner = User.objects.create(
            email='owner@lms.com',
            password='test'
        )
        self.subject = Subject.objects.create(
            title='Test subject',
            description='Test description',
        )
        self.branch = Branch.objects.create(
            title='Test branch',
            description='Test description',
            subject=self.subject
        )
        self.material = Material.objects.create(
            title='Test material',
            text='Test text',
            branch=self.branch,
            owner=self.owner
        )
        self.quiz = Quiz.objects.create(
            title='Test quiz',
            material=self.material,
            owner=self.owner
        )
        self.question = Question.objects.create(
            quiz=self.quiz,
            question_text='Question test',
        )
        self.choice1 = Choice.objects.create(
            question=self.question,
            choice_text='Choice 1',
            is_right=False
        )
        self.choice2 = Choice.objects.create(
            question=self.question,
            choice_text='Choice 1',
            is_right=True
        )
        self.Student_answer = StudentAnswer.objects.create(
            quiz=self.quiz,
            student=self.user,
            question=self.question,
            choice=self.choice1,
        )

    def test_report_retrieve(self):
        self.client.force_authenticate(user=self.user)

        response = self.client.get(
            reverse('quiz:report',
                    args=[self.quiz.pk])
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(
            response.json(),
            {
                'title': 'Test quiz',
                'material': 8,
                'num_right_answers': 'Вы ответили правильно на 0 вопросов из 1!'
            }
        )
