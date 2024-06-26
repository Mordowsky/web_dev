# Generated by Django 5.0.4 on 2024-04-30 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quality_control', '0003_bugreport_priority_featurerequest_priority'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bugreport',
            name='priority',
            field=models.CharField(choices=[('prior1', '1'), ('prior2', '2'), ('prior3', '3'), ('prior4', '4'), ('prior5', '5')], default='1', max_length=50),
        ),
        migrations.AlterField(
            model_name='featurerequest',
            name='priority',
            field=models.CharField(choices=[('prior1', '1'), ('prior2', '2'), ('prior3', '3'), ('prior4', '4'), ('prior5', '5')], default='1', max_length=50),
        ),
    ]
