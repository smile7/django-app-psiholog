# serializers convert model instances to JSON so that the frontend can work with the received data

from rest_framework import serializers
from .models import Deinosti, Step
class DeinostiSerializer(serializers.ModelSerializer):

    class Meta:
        model = Deinosti
        fields = ("title", "description")

class StepSerializer(serializers.ModelSerializer):

    class Meta:
        model = Step
        fields = ("title", "description", "image")