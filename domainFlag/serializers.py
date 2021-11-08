from rest_framework.serializers import ModelSerializer, SerializerMethodField

from .models import DomainFlagModel


class DomainFlagSerializer(ModelSerializer):
    class Meta:
        model = DomainFlagModel
        fields = '__all__'

