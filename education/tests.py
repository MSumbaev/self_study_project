import datetime

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from education.models import Subject, Branch, Material
from users.models import User


class SubjectListTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(
            email='test@test.com',
            password='test'
        )
        self.subject = Subject.objects.create(
            title='Test subject',
            description='Test description',
        )

    def test_list_subject(self):
        self.client.force_authenticate(user=self.user)

        response = self.client.get(
            reverse('education:subject_list'),
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            [
                {
                    'id': self.subject.pk,
                    'title': 'Test subject',
                    'description': 'Test description',
                }
            ]
        )


class SubjectRetrieveTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(
            email='test@test.com',
            password='test'
        )
        self.subject = Subject.objects.create(
            title='Test subject',
            description='Test description',
        )
        # self.branch = Branch.objects.create(
        #     title='Test branch',
        #     description='Test description',
        #     subject=self.subject.pk
        # )

    def test_subject_retrieve(self):
        self.client.force_authenticate(user=self.user)

        response = self.client.get(
            reverse('education:subject_get',
                    args=[self.subject.id])
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(
            response.json(),
            {
                'id': self.subject.pk,
                'branches': [],
                'title': 'Test subject',
                'description': 'Test description',
            }
        )


class BranchListTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(
            email='test@test.com',
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

    def test_list_branch(self):
        self.client.force_authenticate(user=self.user)

        response = self.client.get(
            reverse('education:branch_list'),
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            [
                {
                    'id': self.branch.pk,
                    'materials_count': 0,
                    'title': 'Test branch',
                    'description': 'Test description',
                    'subject': self.subject.pk
                }
            ]
        )


class BranchRetrieveTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(
            email='test@test.com',
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

    def test_branch_retrieve(self):
        self.client.force_authenticate(user=self.user)

        response = self.client.get(
            reverse('education:branch_get',
                    args=[self.branch.id])
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(
            response.json(),
            {
                'id': self.branch.pk,
                'materials': [],
                'materials_count': 0,
                'title': 'Test branch',
                'description': 'Test description',
                'subject': self.subject.pk
            }
        )


class MaterialCreateTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(
            email='student@lms.com',
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

    def test_create_material(self):
        self.client.force_authenticate(user=self.user)

        data = {
            'title': 'Test material',
            'text': 'Test text',
            'branch': self.branch.pk,
            'owner': self.user.pk
        }

        response = self.client.post(
            reverse('education:material_create'),
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertEqual(
            response.json(),
            {
                'id': 1,
                'quiz_count': 0,
                'title': 'Test material',
                'link': None,
                'text': 'Test text',
                'date_of_last_modification': datetime.date.today().strftime('%Y-%m-%d'),
                'branch': self.branch.pk,
                'owner': self.user.pk
            }
        )


class MaterialDestroyTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(
            email='student@lms.com',
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
            text='Test description',
            branch=self.branch,
            owner=self.user
        )

    def test_material_delete(self):
        self.client.force_authenticate(user=self.user)

        response = self.client.delete(
            reverse('education:material_delete',
                    args=[self.material.id])
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )

        self.assertFalse(Material.objects.filter(id=self.material.id).exists())


class MaterialListTestCase(APITestCase):
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

    def test_list_material(self):
        self.client.force_authenticate(user=self.user)

        response = self.client.get(
            reverse('education:material_list'),
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            {
                'count': 1,
                'next': None,
                'previous': None,
                'results': [
                    {
                        'id': self.material.pk,
                        'quiz_count': 0,
                        'title': 'Test material',
                        'link': None,
                        'text': 'Test text',
                        'date_of_last_modification': datetime.date.today().strftime('%Y-%m-%d'),
                        'branch': self.branch.pk,
                        'owner': self.owner.pk
                    }
                ]
            }
        )


class MaterialRetrieveTestCase(APITestCase):
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

    def test_material_retrieve(self):
        self.client.force_authenticate(user=self.user)

        response = self.client.get(
            reverse('education:material_get',
                    args=[self.material.id])
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(
            response.json(),
            {
                'id': self.material.pk,
                'quiz_count': 0,
                'title': 'Test material',
                'link': None,
                'text': 'Test text',
                'date_of_last_modification': datetime.date.today().strftime('%Y-%m-%d'),
                'branch': self.branch.pk,
                'owner': self.owner.pk
            }
        )


class MaterialUpdateTestCase(APITestCase):
    def setUp(self):
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

    def test_material_update(self):
        self.client.force_authenticate(user=self.owner)

        data = {
            'title': 'Material update',
            'text': 'text update test',
            'link': 'https://www.youtube.com/watch_test_update'
        }

        response = self.client.patch(
            reverse('education:material_update',
                    args=[self.material.id]),
            data=data
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(
            response.json(),
            {
                'id': self.material.pk,
                'quiz_count': 0,
                'title': 'Material update',
                'link': 'https://www.youtube.com/watch_test_update',
                'text': 'text update test',
                'date_of_last_modification': datetime.date.today().strftime('%Y-%m-%d'),
                'branch': self.branch.pk,
                'owner': self.owner.pk
            }
        )
