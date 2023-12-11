from rest_framework import serializers

from education.models import Subject, Material, Branch


class SubjectSerializer(serializers.ModelSerializer):
    """Сериализатор предмета"""
    class Meta:
        model = Subject
        fields = '__all__'


class MaterialSerializer(serializers.ModelSerializer):
    """Сериализатор материала"""
    quiz_count = serializers.IntegerField(source='quiz_set.all.count', read_only=True)

    class Meta:
        model = Material
        fields = '__all__'


class BranchSerializer(serializers.ModelSerializer):
    """Сериализатор раздела"""
    materials_count = serializers.IntegerField(source='material_set.all.count', read_only=True)

    class Meta:
        model = Branch
        fields = '__all__'


class SubjectDetailSerializer(serializers.ModelSerializer):
    """Сериализатор предмета детальный"""
    branches = BranchSerializer(source='branch_set.all', many=True, read_only=True)

    class Meta:
        model = Subject
        fields = '__all__'


class MaterialCutSerializer(serializers.ModelSerializer):
    """Сериализатор материала упрощенный"""
    class Meta:
        model = Material
        fields = ('pk', 'title',)


class BranchDetailSerializer(serializers.ModelSerializer):
    """Сериализатор раздела детальный"""
    materials_count = serializers.IntegerField(source='material_set.all.count', read_only=True)
    materials = MaterialCutSerializer(source='material_set.all', many=True, read_only=True)

    class Meta:
        model = Branch
        fields = '__all__'
