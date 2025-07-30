from rest_framework import serializers
from .models import CustomUser, Question, Quiz, Answer

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
    answers = serializers.AnswerSerializer(many=True, read_only=True)
    class Meta:
        model = Question
        fields = ['id', 'question', 'answers', 'quiz', 'question_type']
    
    def get_answers(self, obj):
        return [answer.answer for answer in obj.answers.all()]

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['id', 'question', 'answer', 'correct']

class QuizSerializer(serializers.ModelSerializer):
    creator = serializers.SlugRelatedField(
            slug_field='username',  # The field on the related model to use
            queryset=CustomUser.objects.all() # The queryset for validation
    )
    class Meta:
        model = Quiz
        fields = ['id', 'title', 'creator']
    
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

