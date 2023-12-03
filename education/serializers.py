from rest_framework import serializers

from education.models import Subject, Material, Branch


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'


class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = '__all__'


class BranchSerializer(serializers.ModelSerializer):
    materials_count = serializers.IntegerField(source='material_set.all.count', read_only=True)

    class Meta:
        model = Branch
        fields = '__all__'
