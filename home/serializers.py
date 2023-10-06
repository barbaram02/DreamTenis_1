from rest_framework import serializers
from home.models import Topico

class TopicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topico
        fields = '__all__'

