from rest_framework import serializers
from .models import (
    Access, Announcement, Courses, Enrollment, Form, Gradesheet,
    Materials, Receive, Section, Upload, Users, View, Visibility,
    Consultation, ConsultationMessage
)


class AccessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Access
        fields = "__all__"


class AnnouncementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Announcement
        fields = "__all__"


class CoursesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courses
        fields = "__all__"


class EnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enrollment
        fields = "__all__"


class FormSerializer(serializers.ModelSerializer):
    class Meta:
        model = Form
        fields = "__all__"


class GradesheetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gradesheet
        fields = "__all__"


class MaterialsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Materials
        fields = "__all__"


class ReceiveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receive
        fields = "__all__"


class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = "__all__"


class UploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Upload
        fields = "__all__"


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = "__all__"


class ViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = View
        fields = "__all__"


class VisibilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Visibility
        fields = "__all__"


class ConsultationMessageSerializer(serializers.ModelSerializer):
    sender_name = serializers.CharField(source="sender.fname", read_only=True)

    class Meta:
        model = ConsultationMessage
        fields = ["id", "consultation", "sender", "sender_name", "message", "timestamp"]


class ConsultationSerializer(serializers.ModelSerializer):
    student_name = serializers.CharField(source="student.fname", read_only=True)
    teacher_name = serializers.CharField(source="teacher.fname", read_only=True)
    messages = ConsultationMessageSerializer(many=True, read_only=True)

    class Meta:
        model = Consultation
        fields = ["id", "student", "teacher", "student_name", "teacher_name", "messages"]
