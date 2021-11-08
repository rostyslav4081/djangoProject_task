# Generated by Django 3.2.8 on 2021-11-05 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DomainModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FQDN', models.CharField(max_length=255)),
                ('CreateDate', models.DateTimeField(auto_now_add=True)),
                ('ExpirationDate', models.DateTimeField()),
                ('DeletionDate', models.DateTimeField()),
            ],
        ),
    ]
