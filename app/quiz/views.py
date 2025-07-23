import django_filters
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .models import CustomUser, Question, Quiz
from .serializers import UserSerializer, QuizSerializer, QuestionSerializer

class UserViewSet(viewsets.ModelViewSet):
	queryset = CustomUser.objects.all()
	serializer_class = UserSerializer
	filter_backends = [DjangoFilterBackend]
	filterset_fields = ['id']

class QuizzesViewSet(viewsets.ModelViewSet):
	queryset = Quiz.objects.all()
	serializer_class = QuizSerializer

class QuestionsViewSet(viewsets.ModelViewSet):
	queryset = Question.objects.all()
	serializer_class = QuestionSerializer