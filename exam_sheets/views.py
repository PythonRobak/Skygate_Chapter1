from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from exam_sheets.forms import CreateExamSheetAdminForm, CreateExamSheetTeacherForm
from exam_sheets.models import ExamSheet, CompletedExaminationSheet, Role


class CreateExamSheet(View):

    def get(self, request):

        logged_user_id = request.user.pk
        role = Role.objects.get(user_id=logged_user_id)
        role_int = role.role_name

        if role_int == 1:

            form = CreateExamSheetAdminForm()
            return render(request, 'create_exam_sheet.html', {'form': form, 'role': role_int})

        elif role_int == 3:

            form = CreateExamSheetTeacherForm
            return render(request, 'create_exam_sheet.html', {'form': form, 'role': role_int})

        elif role_int == 2:

            return HttpResponse("You dont have permissions to create exam sheet")

        else:
            return HttpResponse("You dont have permissions to create exam sheet")

    def post(self, request):

        logged_user_id = request.user.pk
        role = Role.objects.get(user_id=logged_user_id)
        role_int = role.role_name

        if role_int == 1:
            form = CreateExamSheetAdminForm(request.POST)
            if form.is_valid():
                return HttpResponse("Exam sheet archived")

        if role_int == 2:

            form = CreateExamSheetTeacherForm(request.POST)
            if form.is_valid():
                sheet_to_save = ExamSheet.objects.create(
                    exam_sheet_title=form.cleaned_data['exam_sheet_title'],
                    task_01_title=form.cleaned_data['task_01_title'],
                    task_01_description=form.cleaned_data['task_01_description'],
                    task_01_max_points=form.cleaned_data['task_01_max_points'],
                    task_02_title=form.cleaned_data['task_01_title'],
                    task_02_description=form.cleaned_data['task_01_description'],
                    task_02_max_points=form.cleaned_data['task_01_max_points'],
                    task_03_title=form.cleaned_data['task_01_title'],
                    task_03_description=form.cleaned_data['task_01_description'],
                    task_03_max_points=form.cleaned_data['task_01_max_points'],
                    task_04_title=form.cleaned_data['task_01_title'],
                    task_04_description=form.cleaned_data['task_01_description'],
                    task_04_max_points=form.cleaned_data['task_01_max_points'],
                    task_05_title=form.cleaned_data['task_01_title'],
                    task_05_description=form.cleaned_data['task_01_description'],
                    task_05_max_points=form.cleaned_data['task_01_max_points'],
                    author=logged_user

                )
                sheet_to_save.save()
                return HttpResponse("Exam sheet saved by teacher")

            return redirect('users')


class Exam(View):

    def get(self, request):

        logged_user_id = request.user.pk
        role = Role.objects.get(user_id=logged_user_id)
        role_int = role.role_name

        exam_sheet = CompletedExaminationSheet.objects.all().order_by('pk')
        exam_sheet_to_fill = []
        ctx = {'exams': exam_sheet_to_fill, 'role': role_int}

        for element in exam_sheet:

            if element.entrant == None:
                exam_sheet_to_fill.append(element)

            if element.entrant != None:

                if int(element.entrant) != logged_user_id:
                    print(element.entrant)
                    exam_sheet_to_fill.append(element)

        return render(request, 'exam.html', ctx)


class Check(View):

    def get(self, request):

        logged_user_id = request.user.pk
        role = Role.objects.get(user_id=logged_user_id)
        role_int = role.role_name

        if role_int == 3:
            exam_sheet = CompletedExaminationSheet.objects.all().order_by('pk')
            exam_sheet_to_check = []
            ctx = {'exams': exam_sheet_to_check}

            for element in exam_sheet:
                if element.final_rating:
                    pass
                else:
                    exam_sheet_to_check.append(element)

            return render(request, 'check.html', ctx)

        else:
            return HttpResponse("You dont have permissions to check the exam sheets")
