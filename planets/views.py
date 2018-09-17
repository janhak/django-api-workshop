from rest_framework import generics
from planets.serializers import PlanetSerializer
from planets.models import Planet


class PlanetList(generics.ListCreateAPIView):
    queryset = Planet.objects.all()
    serializer_class = PlanetSerializer
