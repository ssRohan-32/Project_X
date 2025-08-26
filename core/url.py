from django.urls import path, include
from rest_framework import routers
from .views import (
    AccessViewSet,
    AnnouncementViewSet,
    CoursesViewSet,
    EnrollmentViewSet,
    FormViewSet,
    GradesheetViewSet,
    MaterialsViewSet,
    ReceiveViewSet,
    SectionViewSet,
    UploadViewSet,
    UsersViewSet,
    ViewViewSet,
    VisibilityViewSet,
    ConsultationViewSet,
    ConsultationMessageViewSet,
    home,
)

# Router for all viewsets
router = routers.DefaultRouter()
router.register(r'access', AccessViewSet)
router.register(r'announcement', AnnouncementViewSet)
router.register(r'courses', CoursesViewSet)
router.register(r'enrollment', EnrollmentViewSet)
router.register(r'form', FormViewSet)
router.register(r'gradesheet', GradesheetViewSet)
router.register(r'materials', MaterialsViewSet)
router.register(r'receive', ReceiveViewSet)
router.register(r'sections', SectionViewSet)
router.register(r'upload', UploadViewSet)
router.register(r'users', UsersViewSet)
router.register(r'view', ViewViewSet)
router.register(r'visibility', VisibilityViewSet)
router.register(r'consultations', ConsultationViewSet)
router.register(r'consultation-messages', ConsultationMessageViewSet)

urlpatterns = [
    
    path('', include(router.urls)),
]
