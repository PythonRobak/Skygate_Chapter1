from .views import ExamSheetRudView, ExamSheetAPIView, CompletedExaminationSheetAPIView, \
    CompletedExaminationSheetRudView
from django.conf.urls import url

urlpatterns = [
    url(r'^$', ExamSheetAPIView.as_view(), name='exam-sheet-create'),
    url(r'^(?P<pk>\d+)/$', ExamSheetRudView.as_view(), name='exam-sheet-rud'),
    url(r'^exam/$', CompletedExaminationSheetAPIView.as_view(), name='answers-sheet-create'),
    url(r'^exam/(?P<pk>\d+)/$', CompletedExaminationSheetRudView.as_view(), name='answers-sheet-rud'),
]
