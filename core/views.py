# views provide methods to handle CRUD operations

from rest_framework import viewsets
from .serializers import PostSerializer, DeinostiSerializer, StepSerializer, GallerySerializer, CertificateSerializer, PhaseSerializer
from .models import Post, Deinosti, Step, Gallery, Certificate, Phase

class DeinostiViewSet(viewsets.ModelViewSet):
    serializer_class = DeinostiSerializer
    queryset = Deinosti.objects.all()

class StepViewSet(viewsets.ModelViewSet):
    serializer_class = StepSerializer
    queryset = Step.objects.all()

class GalleryViewSet(viewsets.ModelViewSet):
    serializer_class = GallerySerializer
    queryset = Gallery.objects.all()

class CertificateViewSet(viewsets.ModelViewSet):
    serializer_class = CertificateSerializer
    queryset = Certificate.objects.all()

class PhaseViewSet(viewsets.ModelViewSet):
    serializer_class = PhaseSerializer
    queryset = Phase.objects.all()

class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()