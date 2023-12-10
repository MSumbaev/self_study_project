from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated

from education.models import Subject, Branch, Material
from education.paginators import MaterialsPaginator
from education.permissions import IsModerator, IsTeacher, IsNotModerator, IsOwner
from education.serializers import SubjectSerializer, BranchSerializer, MaterialSerializer, SubjectDetailSerializer, \
    BranchDetailSerializer


# --------------------Subject--------------------
class SubjectListAPIView(generics.ListAPIView):
    serializer_class = SubjectSerializer
    queryset = Subject.objects.all()
    permission_classes = [IsAuthenticated]
    filter_backends = [SearchFilter]
    search_fields = ('title', 'description',)


class SubjectRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = SubjectDetailSerializer
    queryset = Subject.objects.all()
    permission_classes = [IsAuthenticated]


# --------------------Branch--------------------
class BranchListAPIView(generics.ListAPIView):
    serializer_class = BranchSerializer
    queryset = Branch.objects.all()
    permission_classes = [IsAuthenticated]
    filter_backends = [SearchFilter, DjangoFilterBackend]
    search_fields = ('title', 'description',)
    filterset_fields = ('subject',)


class BranchRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = BranchDetailSerializer
    queryset = Branch.objects.all()
    permission_classes = [IsAuthenticated]


# --------------------Material--------------------
class MaterialCreateAPIView(generics.CreateAPIView):
    serializer_class = MaterialSerializer
    permission_classes = [IsAuthenticated, IsTeacher | IsNotModerator]

    def perform_create(self, serializer):
        material = serializer.save()
        material.owner = self.request.user
        material.save()


class MaterialListAPIView(generics.ListAPIView):
    serializer_class = MaterialSerializer
    queryset = Material.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = MaterialsPaginator
    filter_backends = [SearchFilter, DjangoFilterBackend, OrderingFilter]
    search_fields = ('title', 'text',)
    filterset_fields = ('branch', 'owner',)
    ordering_fields = ('date_of_last_modification',)


class MaterialRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = MaterialSerializer
    queryset = Material.objects.all()
    permission_classes = [IsAuthenticated]


class MaterialUpdateAPIView(generics.UpdateAPIView):
    serializer_class = MaterialSerializer
    queryset = Material.objects.all()
    permission_classes = [IsAuthenticated, IsOwner | IsModerator]


class MaterialDestroyAPIView(generics.DestroyAPIView):
    queryset = Material.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]
