from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DeinostiViewSet, StepViewSet

router = DefaultRouter()
router.register(r'deinosti', DeinostiViewSet)
router.register(r'step', StepViewSet)

urlpatterns = [
    path("", include(router.urls))
]