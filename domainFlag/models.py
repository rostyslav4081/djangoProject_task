from django.db import models

from domain.models import DomainModel
class DomainFlagModel(models.Model):
    class Meta:
        db_table = 'domainFlag'

    domain = models.ForeignKey(DomainModel, on_delete = models.CASCADE, related_name='domainflag')
    Type = models.CharField(max_length = 20)
    ValidFrom = models.DateTimeField()
    ValidUntil = models.DateTimeField(null=True)
# Create your models here.
