from django.contrib import admin

from .models import Choice, Question
# Register your models here.
class QuestionAdmin(admin.ModelAdmin):
  fieldsets = [
    (None,     {'fields': ['pub_date', 'question_text']})
    ('Date information', {'fields': ['pub_date']})
  ]

admin.site.register(Question)
admin.site.register(Choice)