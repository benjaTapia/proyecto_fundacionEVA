from dataclasses import fields
from core.models import Aporte
from core.models import Aportador
from rest_framework import serializers


class AporteSerializers(serializers.ModelSerializer):
    class Meta:
        model = Aporte
        fields =  ['rutAportador','nombreAportador', 'apellidoAportador','usuarioAportador', 'correoAportador', 'passAportador']

class AportadorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Aportador
        fields = ['username', 'password']