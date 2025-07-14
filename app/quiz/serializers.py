from rest_framework import serializers
from .models import Users, Questions, Quizzes, Type

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['id', 'role', 'username', 'email', 'password']

class QuestionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questions
        fields = ['uuid_id', 'question', 'answer', 'incorect', 'quiz']

class QuizzesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quizzes
        fields = ['uuid_id', 'title', 'types', 'creator']

class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = ['id', 'get_id_display']
