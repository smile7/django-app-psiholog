# views provide methods to handle CRUD operations

from rest_framework import viewsets
from .serializers import DeinostiSerializer, StepSerializer
from .models import Deinosti, Step

class DeinostiViewSet(viewsets.ModelViewSet):
    serializer_class = DeinostiSerializer
    queryset = Deinosti.objects.all()

class StepViewSet(viewsets.ModelViewSet):
    serializer_class = StepSerializer
    queryset = Step.objects.all()