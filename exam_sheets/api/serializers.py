from rest_framework import serializers
from exam_sheets.models import ExamSheet, CompletedExaminationSheet


class ExamSheetSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExamSheet
        fields = [
            'pk',
            'exam_sheet_title',
            'task_01_title',
            'task_01_description',
            'task_01_max_points',
            'task_02_title',
            'task_02_description',
            'task_02_max_points',
            'task_03_title',
            'task_03_description',
            'task_03_max_points',
            'task_04_title',
            'task_04_description',
            'task_04_max_points',
            'task_05_title',
            'task_05_description',
            'task_05_max_points',

        ]
        read_only_fields = ['pk']


class CompletedExaminationSheetSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompletedExaminationSheet
        fields = [
            'pk',
            'completed_examination_sheet_title',
        ]
        read_only_fields = [
            'pk',
            'completed_examination_sheet_title',
        ]


class CompletedExaminationSheetSerializerAdmin(serializers.ModelSerializer):
    class Meta:
        model = CompletedExaminationSheet
        fields = [
            'pk',
            'completed_examination_sheet_title',
            'archived',
        ]
        read_only_fields = [
            'pk',
            'completed_examination_sheet_title',
        ]


class CompletedExaminationSheetSerializerStudent(serializers.ModelSerializer):
    class Meta:
        model = CompletedExaminationSheet
        fields = [
            'pk',
            'completed_examination_sheet_title',
            'task_01_title',
            'task_01_description',
            'task_01_max_points',
            'answer_01',
            'task_02_title',
            'task_02_description',
            'task_02_max_points',
            'answer_02',
            'task_03_title',
            'task_03_description',
            'task_03_max_points',
            'answer_03',
            'task_04_title',
            'task_04_description',
            'task_04_max_points',
            'answer_04',
            'task_05_title',
            'task_05_description',
            'task_05_max_points',
            'answer_05',
        ]
        read_only_fields = [
            'pk',
            'completed_examination_sheet_title',
            'task_01_title',
            'task_01_description',
            'task_01_max_points',
            'task_02_title',
            'task_02_description',
            'task_02_max_points',
            'task_03_title',
            'task_03_description',
            'task_03_max_points',
            'task_04_title',
            'task_04_description',
            'task_04_max_points',
            'task_05_title',
            'task_05_description',
            'task_05_max_points',
        ]


class CompletedExaminationSheetSerializerTeacherCreate(serializers.ModelSerializer):
    class Meta:
        model = CompletedExaminationSheet
        fields = [
            'pk',
            'completed_examination_sheet_title',
            'entrant',
            'task_01_title',
            'task_01_description',
            'task_01_max_points',
            'answer_01',
            'answer_01_points_earned',
            'task_02_title',
            'task_02_description',
            'task_02_max_points',
            'answer_02',
            'answer_02_points_earned',
            'task_03_title',
            'task_03_description',
            'task_03_max_points',
            'answer_03',
            'answer_03_points_earned',
            'task_04_title',
            'task_04_description',
            'task_04_max_points',
            'answer_04',
            'answer_04_points_earned',
            'task_05_title',
            'task_05_description',
            'task_05_max_points',
            'answer_05',
            'answer_05_points_earned',
            'final_rating'
        ]
        read_only_fields = [
            'pk',
            'entrant',
            'author',
            'answer_01',
            'answer_02',
            'answer_03',
            'answer_04',
            'answer_05',
            'checked',
            'checked_by',
            'answer_01_points_earned',
            'answer_02_points_earned',
            'answer_03_points_earned',
            'answer_04_points_earned',
            'answer_05_points_earned',
            'final_rating'
        ]


class CompletedExaminationSheetSerializerTeacherRud(serializers.ModelSerializer):
    class Meta:
        model = CompletedExaminationSheet
        fields = [
            'pk',
            'completed_examination_sheet_title',
            'entrant',
            'task_01_title',
            'task_01_description',
            'task_01_max_points',
            'answer_01',
            'answer_01_points_earned',
            'task_02_title',
            'task_02_description',
            'task_02_max_points',
            'answer_02',
            'answer_02_points_earned',
            'task_03_title',
            'task_03_description',
            'task_03_max_points',
            'answer_03',
            'answer_03_points_earned',
            'task_04_title',
            'task_04_description',
            'task_04_max_points',
            'answer_04',
            'answer_04_points_earned',
            'task_05_title',
            'task_05_description',
            'task_05_max_points',
            'answer_05',
            'answer_05_points_earned',
            'final_rating'
        ]
        read_only_fields = [
            'pk',
            'entrant',
            'author',
            'answer_01',
            'answer_02',
            'answer_03',
            'answer_04',
            'answer_05',
            'checked',
            'checked_by',
            'task_01_max_points',
            'task_02_max_points',
            'task_03_max_points',
            'task_04_max_points',
            'task_05_max_points',
        ]
