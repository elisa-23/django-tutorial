"""
URL configuration for app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from quiz.views import UserViewSet, QuizViewSet, QuestionViewSet
from rest_framework_simplejwt import views as jwt_views

router = DefaultRouter()
router.register(r"users", UserViewSet)
router.register(r"quizzes", QuizViewSet)
router.register(r"questions", QuestionViewSet)
# The order of urlpatterns is important; the first match will be used.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', UserViewSet.as_view({'get': 'list'}), name='user'),
    path('quiz/', QuizViewSet.as_view({'get': 'list'}), name='quiz'),
    path('question/', QuestionViewSet.as_view({'get': 'list'}), name='question'),
    path('api/token/',
         jwt_views.TokenObtainPairView.as_view(),
         name ='token_obtain_pair'),
    path('api/token/refresh/',
         jwt_views.TokenRefreshView.as_view(),
         name ='token_refresh'),
    path('api/token/verify/',
         jwt_views.TokenVerifyView.as_view(),
         name ='token_verify'),
    path('api/logout/', 
         jwt_views.TokenBlacklistView.as_view(), 
         name='logout'),
    path('', include(router.urls))
]