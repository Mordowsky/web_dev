from django.db import models
from tasks.models import Project
from tasks.models import Task

# Create your models here.

STATUS_BUG = [
        ('New', 'Новая'),
        ('In_progress', 'В работе'),
        ('Completed', 'Завершена'),
    ]
STATUS_FEATURE = [
        ('review',  "Рассмотрение"),
        ('accepted', "Принято"),
        ('denied', "Отклонено"),
    ]

PRIORITY = [('prior1','1'),
            ('prior2','2'),
            ('prior3','3'),
            ('prior4','4'),
            ('prior5','5'),            
            ]

class BugReport (models.Model):
    def __str__(self):
        return self.title
    
    project = models.ForeignKey(
        Project,
        related_name='BugReport',
        on_delete=models.CASCADE,
    )
    task = models.ForeignKey(
        Task,
        related_name='BugReport',
        on_delete=models.SET_NULL,
        null=True,
    )
    title = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(
        max_length=50,
        choices=STATUS_BUG,
        default="Новая",
    )
    priority = models.CharField(max_length=50,
                                choices=PRIORITY,
                                default='1')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class FeatureRequest (models.Model):
    def __str__(self):
        return self.title
    
    title = models.CharField(max_length=100)
    description = models.TextField()
    project = models.ForeignKey(
        Project,
        related_name='FeatureRequest',
        on_delete=models.CASCADE,
    )
    task = models.ForeignKey(
        Task,
        related_name='FeatureRequest',
        on_delete=models.SET_NULL,
        null=True,
    )
    status = models.CharField(
        max_length=50,
        choices=STATUS_FEATURE,
        default="Рассмотрение",
    )
    priority = models.CharField(max_length=50,
                                choices=PRIORITY,
                                default='1')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

