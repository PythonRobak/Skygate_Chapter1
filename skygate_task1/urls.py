from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView

from exam_sheets.views import CreateExamSheet, Exam, Check

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    url(r'^createexamsheet/$', CreateExamSheet.as_view(), name="createexamsheet"),
    url(r'^api/examsheets/', include('exam_sheets.api.urls')),
    url(r'^exams/$', Exam.as_view(), name="exams"),
    url(r'^check/$', Check.as_view(), name="check"),


]
