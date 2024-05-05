# Generated by Django 5.0.4 on 2024-04-30 14:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quality_control', '0005_alter_bugreport_task_alter_featurerequest_task'),
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bugreport',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='BugReport', to='tasks.project'),
        ),
        migrations.AlterField(
            model_name='featurerequest',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='FeatureRequest', to='tasks.project'),
        ),
    ]
