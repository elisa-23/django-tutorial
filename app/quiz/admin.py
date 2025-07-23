from django.contrib import admin
from .models import CustomUser
from .models import Quiz
from .models import Question

admin.site.register(CustomUser)
admin.site.register(Quiz)
admin.site.register(Question)