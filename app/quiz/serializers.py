from rest_framework import serializers
from .models import CustomUser, Question, Quiz

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'role', 'username', 'email', 'password']
    password = serializers.CharField(write_only=True)
    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password'],
            username=validated_data['username'],
            role=validated_data['role']
        )
        return user

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['id', 'question', 'answer', 'incorect', 'quiz', 'question_type']
    def validate_question_type(self, value):
        valid_choices = ['multiple choice', 'true/false', 'numerical', 'dropdown']
        if value not in valid_choices:
            raise serializers.ValidationError("Invalid choice for 'question_type'.")
        return value

class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = ['id', 'title', 'types', 'creator']
    
    def validate_types(self, value):
        valid_choices = ['multiple choice', 'true/false', 'numerical', 'dropdown']
        if not isinstance(value, list):
            raise serializers.ValidationError("Expected 'status' to be a list.")
        if not set(value).issubset(valid_choices):
            raise serializers.ValidationError("Invalid choice in 'status'.")
        results = []
        for n in value:
            results.append(n)

        return results

