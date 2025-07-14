from django.urls import path
from .views import UsersViewSet

urlpatterns = [
    path('register/', UsersViewSet.as_view({'get': 'list'}), name='users'),
]