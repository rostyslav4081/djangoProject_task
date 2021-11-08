from rest_framework.serializers import ModelSerializer, SerializerMethodField

from .models import DomainModel


class DomainSerializer(ModelSerializer):
    class Meta:
        model = DomainModel
        fields = '__all__'

