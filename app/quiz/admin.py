from django.contrib import admin
from .models import Users
from .models import Quizzes
from .models import Questions

admin.site.register(Users)
admin.site.register(Quizzes)
admin.site.register(Questions)