from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView, RetrieveAPIView
from rest_framework.response import Response
from .models import DomainFlagModel
from .serializers import DomainFlagSerializer
import datetime


# Create your views here.
class DomainFlagLView(ListAPIView):
    serializer_class = DomainFlagSerializer
    queryset = DomainFlagModel.objects.all()

    def get_queryset(self):
        req = self.request
        qs = DomainFlagModel.objects.all()
        domain = req.query_params.get('domain')

        if domain:
            return DomainFlagModel.objects.raw('SELECT * FROM domainflag WHERE  ValidFrom < current_time AND  ValidUntil >= current_time')
            # return qs.filter(domain=domain)
        print(qs)
        return qs


