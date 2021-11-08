from django.db import models

class DomainModel(models.Model):
    class Domain:
        db_table = 'domain'

    FQDN = models.CharField(max_length = 255)
    CreateDate = models.DateTimeField(auto_now_add = True)
    ExpirationDate = models.DateTimeField(null=True)
    DeletionDate = models.DateTimeField(null=True)
# Create your models here.
