from rest_framework import viewsets
from .models import Users, Questions, Quizzes, Type
from .serializers import UsersSerializer, QuizzesSerializer, QuestionsSerializer, TypeSerializer

class UsersViewSet(viewsets.ModelViewSet):
	queryset = Users.objects.all()
	serializer_class = UsersSerializer

class QuizzesViewSet(viewsets.ModelViewSet):
	queryset = Quizzes.objects.all()
	serializer_class = QuizzesSerializer

class QuestionsViewSet(viewsets.ModelViewSet):
	queryset = Questions.objects.all()
	serializer_class = QuestionsSerializer

class TypeViewSet(viewsets.ModelViewSet):
	queryset = Type.objects.all()
	serializer_class = TypeSerializer