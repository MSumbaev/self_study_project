from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from education.models import Subject, Branch, Material
from education.paginators import MaterialsPaginator
from education.serializers import SubjectSerializer, BranchSerializer, MaterialSerializer


# --------------------Subject--------------------
class SubjectListAPIView(generics.ListAPIView):
    serializer_class = SubjectSerializer
    queryset = Subject.objects.all()
    permission_classes = [IsAuthenticated]


class SubjectRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = SubjectSerializer
    queryset = Subject.objects.all()
    permission_classes = [IsAuthenticated]


# --------------------Branch--------------------
class BranchListAPIView(generics.ListAPIView):
    serializer_class = BranchSerializer
    queryset = Branch.objects.all()
    permission_classes = [IsAuthenticated]


class BranchRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = BranchSerializer
    queryset = Branch.objects.all()
    permission_classes = [IsAuthenticated]


# --------------------Material--------------------
class MaterialCreateAPIView(generics.CreateAPIView):
    serializer_class = MaterialSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        material = serializer.save()
        material.owner = self.request.user
        material.save()


class MaterialListAPIView(generics.ListAPIView):
    serializer_class = MaterialSerializer
    queryset = Material.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = MaterialsPaginator


class MaterialRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = MaterialSerializer
    queryset = Material.objects.all()
    permission_classes = [IsAuthenticated]


class MaterialUpdateAPIView(generics.UpdateAPIView):
    serializer_class = MaterialSerializer
    queryset = Material.objects.all()
    permission_classes = [IsAuthenticated]


class MaterialDestroyAPIView(generics.DestroyAPIView):
    queryset = Material.objects.all()
    permission_classes = [IsAuthenticated]
