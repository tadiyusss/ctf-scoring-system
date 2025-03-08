from django.contrib import admin
from .models import *

class LevelsAdmin(admin.ModelAdmin):
    list_display = ("name", "points", "description")
    search_fields = ("name",)
    list_filter = ("points",)

class QuestionsAdmin(admin.ModelAdmin):
    list_display = ("level", "question", "answer")
    search_fields = ("question", "answer")

class SolvedAdmin(admin.ModelAdmin):
    list_display = ("user", "question", "timestamp", "ip_address")
    search_fields = ("user",)

class SubmissionAdmin(admin.ModelAdmin):
    list_display = ("user", "flag", "timestamp", "ip_address")
    search_fields = ("user",)

admin.site.register(Level, LevelsAdmin)
admin.site.register(Question, QuestionsAdmin)
admin.site.register(Solved, SolvedAdmin)
admin.site.register(Submission, SubmissionAdmin)
