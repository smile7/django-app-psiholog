from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, DeinostiViewSet, StepViewSet, GalleryViewSet, CertificateViewSet, PhaseViewSet, ContactViewSet

router = DefaultRouter()
router.register(r'deinosti', DeinostiViewSet)
router.register(r'step', StepViewSet)
router.register(r'gallery', GalleryViewSet)
router.register(r'certificate', CertificateViewSet)
router.register(r'phase', PhaseViewSet)
router.register(r'post', PostViewSet)
router.register(r'contact', ContactViewSet)

urlpatterns = [
    path("", include(router.urls))
]