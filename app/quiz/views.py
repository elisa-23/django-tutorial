from rest_framework import viewsets, mixins
from django_filters.rest_framework import DjangoFilterBackend
from .models import CustomUser, Question, Quiz
from .serializers import UserSerializer, QuizSerializer, QuestionSerializer

class UserViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
	queryset = CustomUser.objects.all()
	serializer_class = UserSerializer
	filter_backends = [DjangoFilterBackend]
	filterset_fields = ['id']
	def get_queryset(self):
        # Filter objects to only show those owned by the current user
		return CustomUser.objects.filter(id=self.request.user.id)

class QuizViewSet(viewsets.ModelViewSet):
	queryset = Quiz.objects.all()
	serializer_class = QuizSerializer
	filter_backends = [DjangoFilterBackend]
	filterset_fields = ['id', 'creator']

class QuestionViewSet(viewsets.ModelViewSet):
	queryset = Question.objects.all()
	serializer_class = QuestionSerializer
	filter_backends = [DjangoFilterBackend]
	filterset_fields = ['quiz', 'id']