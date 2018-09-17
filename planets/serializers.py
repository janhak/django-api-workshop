from rest_framework import serializers
from planets.models import Planet


class PlanerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Planet
        fields = '__all__'
