from django.http import HttpResponse
from rest_framework import viewsets, generics
from .models import (
    Access, Announcement, Courses, Enrollment, Form, Gradesheet,
    Materials, Receive, Section, Upload, Users, View, Visibility,
    Consultation, ConsultationMessage
)
from .serializers import (
    AccessSerializer, AnnouncementSerializer, CoursesSerializer, EnrollmentSerializer,
    FormSerializer, GradesheetSerializer, MaterialsSerializer, ReceiveSerializer,
    SectionSerializer, UploadSerializer, UsersSerializer, ViewSerializer,
    VisibilitySerializer, ConsultationSerializer, ConsultationMessageSerializer
)


def home(request):
    return HttpResponse("Welcome to UniPortal API")


# Generic ViewSets for all tables
class AccessViewSet(viewsets.ModelViewSet):
    queryset = Access.objects.all()
    serializer_class = AccessSerializer


class AnnouncementViewSet(viewsets.ModelViewSet):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer


class CoursesViewSet(viewsets.ModelViewSet):
    queryset = Courses.objects.all()
    serializer_class = CoursesSerializer


class EnrollmentViewSet(viewsets.ModelViewSet):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer


class FormViewSet(viewsets.ModelViewSet):
    queryset = Form.objects.all()
    serializer_class = FormSerializer


class GradesheetViewSet(viewsets.ModelViewSet):
    queryset = Gradesheet.objects.all()
    serializer_class = GradesheetSerializer


class MaterialsViewSet(viewsets.ModelViewSet):
    queryset = Materials.objects.all()
    serializer_class = MaterialsSerializer


class ReceiveViewSet(viewsets.ModelViewSet):
    queryset = Receive.objects.all()
    serializer_class = ReceiveSerializer


class SectionViewSet(viewsets.ModelViewSet):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer


class UploadViewSet(viewsets.ModelViewSet):
    queryset = Upload.objects.all()
    serializer_class = UploadSerializer


class UsersViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer


class ViewViewSet(viewsets.ModelViewSet):
    queryset = View.objects.all()
    serializer_class = ViewSerializer


class VisibilityViewSet(viewsets.ModelViewSet):
    queryset = Visibility.objects.all()
    serializer_class = VisibilitySerializer


class ConsultationViewSet(viewsets.ModelViewSet):
    queryset = Consultation.objects.all()
    serializer_class = ConsultationSerializer


class ConsultationMessageViewSet(viewsets.ModelViewSet):
    queryset = ConsultationMessage.objects.all()
    serializer_class = ConsultationMessageSerializer
