from django.urls import path

from education.apps import EducationConfig
from education.views import SubjectListAPIView, SubjectRetrieveAPIView, BranchListAPIView, BranchRetrieveAPIView, \
    MaterialCreateAPIView, MaterialListAPIView, MaterialRetrieveAPIView, MaterialUpdateAPIView, MaterialDestroyAPIView

app_name = EducationConfig.name

urlpatterns = [
    path('subject_list/', SubjectListAPIView.as_view(), name='subject_list'),
    path('subject/<int:pk>/', SubjectRetrieveAPIView.as_view(), name='subject_get'),

    path('branch_list/', BranchListAPIView.as_view(), name='branch_list'),
    path('branch/<int:pk>/', BranchRetrieveAPIView.as_view(), name='branch_get'),

    path('material_create/', MaterialCreateAPIView.as_view(), name='material_create'),
    path('material_list/', MaterialListAPIView.as_view(), name='material_list'),
    path('material/<int:pk>/', MaterialRetrieveAPIView.as_view(), name='material_get'),
    path('material_update/<int:pk>/', MaterialUpdateAPIView.as_view(), name='material_update'),
    path('material_delete/<int:pk>/', MaterialDestroyAPIView.as_view(), name='material_delete'),
]
