from django.urls import path
from tasks import views
from quality_control import views as c_views


app_name = 'tasks'

urlpatterns = [
    path('', views.index, name='index'),
    path('projects/', views.projects_list, name='projects_list'),
    path('projects/<int:project_id>/', views.project_detail, name='project_detail'),
    path('projects/<int:project_id>/tasks/<int:task_id>/', views.task_detail, name='task_detail'),
    path('quality_control/', c_views.index, name='quality_control_page'),  # новый маршрут
    path('feedback/', views.feedback_view, name='feedback'),
    path('project/new/', views.create_project, name='create_project'),
    path('project/<int:project_id>/add_task/', views.add_task_to_project, name='add_task_to_project'),
    path('project/<int:project_id>/update/', views.update_project, name='update_project'),
    path('project/<int:project_id>/task/<int:task_id>/update/', views.update_task, name='update_task'),
    path('project/<int:project_id>/delete/', views.delete_project, name='delete_project'),
    path('project/<int:project_id>/tasks/<int:task_id>/delete/', views.delete_task, name='delete_task'),
]