# serializers convert model instances to JSON so that the frontend can work with the received data

from rest_framework import serializers
from .models import Post, Deinosti, Step, Gallery, Certificate, Phase, Contact

class DeinostiSerializer(serializers.ModelSerializer):

    class Meta:
        model = Deinosti
        fields = ("title", "description")

class StepSerializer(serializers.ModelSerializer):

    class Meta:
        model = Step
        fields = ("title", "description", "image")

class GallerySerializer(serializers.ModelSerializer):

    class Meta:
        model = Gallery
        fields = ("url",)

class CertificateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Certificate
        fields = ("title", "url")

class PhaseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Phase
        fields = ("title", "description", "ref", "btn_text", "image")

class PostSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Post
        fields = ("id", "title", "slug", "updated_on", "content", "created_on", "image")
        lookup_field = 'slug'


class ContactSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contact
        fields = ("name", "phone", "email", "subject", "message")