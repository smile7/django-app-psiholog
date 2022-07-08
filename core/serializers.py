# serializers convert model instances to JSON so that the frontend can work with the received data

from rest_framework import serializers
from .models import Post, Deinosti, Step, Gallery, Certificate, Phase

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
        fields = ("image",)

class CertificateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Certificate
        fields = ("title", "image")

class PhaseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Phase
        fields = ("title", "description", "ref", "btn_text", "image")

class PostSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Post
        fields = ("title", "slug", "updated_on", "content", "created_on", "image")