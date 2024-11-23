from rest_framework import serializers
from participantes.models import Participante

class ParticipantesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participante # nome do modelo
        fields = '__all__' # lista de campos

