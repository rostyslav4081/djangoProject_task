from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView, RetrieveAPIView
from rest_framework.response import Response
from .models import DomainModel
from .serializers import DomainSerializer
# Create your views here.
class DomainLView(ListAPIView):
    serializer_class = DomainSerializer
    queryset = DomainModel.objects.all()


    def list(self, request, *args, **kwargs):
        qs = self.get_queryset().filter(DeletionDate = None)
        return Response(DomainSerializer(qs, many=True).data)

class DomainRUDViewSpecial(RetrieveUpdateDestroyAPIView):
    serializer_class = DomainSerializer
    queryset = DomainModel.objects.all()

