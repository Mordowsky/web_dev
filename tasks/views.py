from .models import Project, Task
from django.shortcuts import get_object_or_404
from django.shortcuts import render

def index(request):
    return render(request, 'tasks/index.html')

# def index2(request):
#     projects_list_url = reverse('tasks:projects_list')
#     quality_page_url = reverse('tasks:quality_control_page')
#     html = f'''<h1>Страница приложения tasks</h1><a href='{projects_list_url}'>Список проектов</a><br>
#     <a href='{quality_page_url}'>Страница приложения качества</a>'''
#     return HttpResponse(html)

def projects_list(request):
    projects = Project.objects.all()
    return render(request, 'tasks/projects_list.html', {'project_list': projects})

def project_detail(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    return render(request, 'tasks/project_detail.html', {'project': project})

def task_detail(request, project_id, task_id):
    task = get_object_or_404(Task, id=task_id, project_id=project_id)
    return render(request, 'tasks/task_detail.html', {'task': task})