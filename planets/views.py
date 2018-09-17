from rest_framework import generics
from planets.serializers import PlanerSerializer
from planets.models import Planet


class PlanetList(generics.ListCreateAPIView):
    queryset = Planet.objects.all()
    serializer_class = PlanerSerializer
