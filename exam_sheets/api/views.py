from rest_framework import generics, mixins, status
from rest_framework.response import Response

from django.db.models import Q

from exam_sheets.api.filters import ExamSheetFilter
from exam_sheets.models import ExamSheet, CompletedExaminationSheet, Role
from .permissions import IsOwnerOrReadOnly
from .serializers import ExamSheetSerializer, CompletedExaminationSheetSerializer, \
    CompletedExaminationSheetSerializerAdmin, CompletedExaminationSheetSerializerStudent, \
    CompletedExaminationSheetSerializerTeacherCreate, \
    CompletedExaminationSheetSerializerTeacherRud


class ExamSheetAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'pk'

    serializer_class = ExamSheetSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get_queryset(self):

        qs = ExamSheet.objects.all().order_by('pk')
        title = self.request.GET.get("title")
        author = self.request.GET.get("author")

        if title is not None:
            qs = qs.filter(Q(exam_sheet_title__icontains=title)).distinct()
            # print("case1 - title without ordering")

        if author is not None:
            qs = qs.filter(Q(author__username__icontains=author)).distinct()
            # print("case2 - author without ordering")

        return qs

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ExamSheetRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'

    serializer_class = ExamSheetSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get_queryset(self):
        return ExamSheet.objects.all()

    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}


class CompletedExaminationSheetAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'pk'
    queryset = CompletedExaminationSheet.objects.all().order_by('pk')

    filterset_class = ExamSheetFilter

    def get_serializer_class(self):

        logged_user_id = self.request.user.pk
        role = Role.objects.get(user_id=logged_user_id)
        role_int = role.role_name

        if role_int == 1:
            return CompletedExaminationSheetSerializerAdmin

        if role_int == 2:
            return CompletedExaminationSheetSerializerStudent

        if role_int == 3:
            return CompletedExaminationSheetSerializerTeacherCreate

        return CompletedExaminationSheetSerializer

    def perform_create(self, serializer):

        logged_user_id = self.request.user.pk
        role = Role.objects.get(user_id=logged_user_id)
        role_int = role.role_name

        if role_int == 1:
            serializer.save(author=self.request.user)
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

        if role_int == 2:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

        if role_int == 3:
            serializer.save(author=self.request.user)

    def post(self, request, *args, **kwargs):

        logged_user_id = self.request.user.pk
        role = Role.objects.get(user_id=logged_user_id)
        role_int = role.role_name

        if role_int == 1:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

        if role_int == 2:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

        if role_int == 3:
            return self.create(request, *args, **kwargs)


class CompletedExaminationSheetRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    http_method_names = ['get', 'put', 'delete']

    def delete(self, request, *args, **kwargs):

        logged_user_id = self.request.user.pk
        role = Role.objects.get(user_id=logged_user_id)
        role_int = role.role_name

        if role_int == 1:
            instance = self.get_object()
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)

        if role_int == 2:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

        if role_int == 3:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def get_serializer_class(self):

        logged_user_id = self.request.user.pk
        role = Role.objects.get(user_id=logged_user_id)
        role_int = role.role_name

        if role_int == 1:
            return CompletedExaminationSheetSerializerAdmin

        if role_int == 2:
            return CompletedExaminationSheetSerializerStudent

        if role_int == 3:
            return CompletedExaminationSheetSerializerTeacherRud

    def get_queryset(self):
        return CompletedExaminationSheet.objects.all()

    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}
