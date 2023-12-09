from rest_framework import serializers

from quiz.models import Quiz, Choice, Question, StudentAnswer


class QuizSerializer(serializers.ModelSerializer):
    """Сериализатор модели Quiz"""
    class Meta:
        model = Quiz
        fields = '__all__'


class ChoiceSerializer(serializers.ModelSerializer):
    """Сериализатор модели Choice"""
    class Meta:
        model = Choice
        fields = ['id', 'choice_text',]


class QuestionSerializer(serializers.ModelSerializer):
    """Сериализатор модели Question"""
    choice_set = ChoiceSerializer(many=True, read_only=True, required=False)

    class Meta:
        model = Question
        fields = ['id', 'question_text', 'choice_set']


class StudentAnswerSerializer(serializers.ModelSerializer):
    """Сериализатор модели StudentAnswer"""
    class Meta:
        model = StudentAnswer
        fields = '__all__'


class ReportSerializer(serializers.ModelSerializer):
    num_right_answers = serializers.SerializerMethodField()

    class Meta:
        model = Quiz
        fields = ('title', 'material', 'num_right_answers',)

    def get_num_right_answers(self, instance):
        request = self.context.get('request')
        student = request.user

        questions = instance.question_set.all()
        questions_count = instance.question_set.count()
        if instance.studentanswer_set.filter(student=student.pk):
            student_choices = instance.studentanswer_set.filter(student=student.pk)
        else:
            serializers.ValidationError('Вы не проходили тест!')

        count_right_answr = 0
        for question in questions:
            r_choice = question.choice_set.get(is_right=True)
            for student_choice in student_choices.filter(question=question):
                if student_choice.choice == r_choice:
                    count_right_answr += 1

        return f'Вы ответили правильно на {count_right_answr} вопросов из {questions_count}!'
