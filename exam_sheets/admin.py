from django.contrib import admin
from exam_sheets.models import ExamSheet, CompletedExaminationSheet, Role

admin.site.register(ExamSheet)
admin.site.register(CompletedExaminationSheet)
admin.site.register(Role)
