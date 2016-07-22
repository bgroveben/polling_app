from django.contrib import admin

from .models import Question

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Question Information', {'fields': ['question_text']}),
        ('Date Information',     {'fields': ['pub_date']}),
    ]

admin.site.register(Question, QuestionAdmin)
