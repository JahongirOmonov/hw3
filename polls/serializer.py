from rest_framework.serializers import ModelSerializer
from .models import BemorModel

class BemorSerializer(ModelSerializer):
    class Meta:
        model = BemorModel
        fields=('__all__')