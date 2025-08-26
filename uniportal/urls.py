from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from core import views

router = routers.DefaultRouter()
router.register(r'access', views.AccessViewSet)
router.register(r'announcements', views.AnnouncementViewSet)
router.register(r'courses', views.CoursesViewSet)
router.register(r'enrollments', views.EnrollmentViewSet)
router.register(r'forms', views.FormViewSet)
router.register(r'gradesheets', views.GradesheetViewSet)
router.register(r'materials', views.MaterialsViewSet)
router.register(r'receives', views.ReceiveViewSet)
router.register(r'sections', views.SectionViewSet)
router.register(r'uploads', views.UploadViewSet)
router.register(r'users', views.UsersViewSet)
router.register(r'views', views.ViewViewSet)
router.register(r'visibility', views.VisibilityViewSet)
router.register(r'consultations', views.ConsultationViewSet)
router.register(r'consultation-messages', views.ConsultationMessageViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # keeps your "Welcome" page
    path('api/', include(router.urls)),  # all your API endpoints
]
