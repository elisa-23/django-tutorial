from rest_framework import serializers
from .models import CustomUser, Question, Quiz
MULTIPLE_CHOICE = 1
BOOLEAN = 2
DROPDOWN = 3
NUMERICAL = 4

TYPE_CHOICES = (
    (MULTIPLE_CHOICE, 'multiple choice'),
    (BOOLEAN, 'boolean'),
    (DROPDOWN, 'dropdown'),
    (NUMERICAL, 'numerical')
)
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'role', 'username', 'email', 'password']

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['id', 'question', 'answer', 'incorect', 'quiz']

class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = ['id', 'title', 'types', 'creator']
    
    def validate_types(self, value):
        valid_choices = [1, 2, 3, 4]
        if not isinstance(value, list):
            raise serializers.ValidationError("Expected 'status' to be a list.")
        if not set(value).issubset(valid_choices):
            raise serializers.ValidationError("Invalid choice in 'status'.")
        results = []
        for n in value:
            results.append(TYPE_CHOICES[n-1][1])

        return results

