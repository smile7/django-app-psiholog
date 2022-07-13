# views provide methods to handle CRUD operations
from rest_framework import viewsets
from .serializers import PostSerializer, DeinostiSerializer, StepSerializer, GallerySerializer, CertificateSerializer, PhaseSerializer, ContactSerializer
from .models import Post, Deinosti, Step, Gallery, Certificate, Phase, Contact
from rest_framework.response import Response
from django.core.mail import send_mail
from django.conf import settings

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

class ContactViewSet(viewsets.ModelViewSet):
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()

    # Overriding create method on post request to send mail with the input data
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        send_mail('Запитване от уебсайта', "Suobshtenieto e: {}".format(request.data), settings.EMAIL_HOST_USER, ["sisitymiteva@yahoo.com"])
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, headers=headers)
