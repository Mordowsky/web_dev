from django.http import HttpResponse
from django.urls import reverse
from django.views import View
from django.views.generic import DetailView
from .models import BugReport, FeatureRequest


class IndexView(View):
    def get(self, request, *args, **kwargs):
        bugs_page_url = reverse('quality_control:bugs_page')
        features_page_url = reverse('quality_control:features_list')
        html = f"<h1>Система контроля качества</h1><a href='{bugs_page_url}'>Список всех багов</a><br><a href='{features_page_url}'>Запросы на улучшение</a>"
        return HttpResponse(html)    


def index(request):
    bugs_list_url = reverse('quality_control:bugs_list')
    features_page_url = reverse('quality_control:features_list')
    html = f"<h1>Система контроля качества</h1><a href='{bugs_list_url}'>Список всех багов</a><br><a href='{features_page_url}'>Запросы на улучшение</a>"
    return HttpResponse(html)


def bug_detail(request, bug_id):
    html_bug_detail = f'Детали бага {bug_id}'
    return HttpResponse(html_bug_detail)


def feature_id_detail (request, feature_id):
    html_feature_detail = f'Детали улучшения {feature_id}'
    return HttpResponse(html_feature_detail)

def bug_list(request):
    bugs = BugReport.objects.all()
    bug_html = '<h1>Cписок отчетов об ошибках<h1><ul>'
    for bug in bugs:
        bug_html += f'<li><a href="{bug.id}/">{bug.title}</a> &ensp; {bug.status}</li>'
    bug_html += '</ul>'
    return HttpResponse(bug_html)

def feature_list(request):
    features = FeatureRequest.objects.all()
    feature_html = '<h1>Список запросов на улучшение<h1><ul>'
    for feature in features:
        feature_html += f'<li><a href="{feature.id}/">{feature.title}</a> &ensp; {feature.status}</li>'
    feature_html += '</ul>'
    return HttpResponse(feature_html)

class BugView(DetailView):
    model = BugReport
    pk_url_kwarg='bug_id'
    
    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        bug = self.object
        response_html = f'<h1>{bug.title}</h1><p>Description: {bug.description}</p><br>'
        response_html += f'Status - {bug.status}, Priority - {bug.priority}'
        return HttpResponse(response_html)
    
class FeatureView(DetailView):
    model = FeatureRequest
    pk_url_kwarg='feature_id'
    
    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        feature = self.object
        response_html = f'<h1>{feature.title}</h1><p>Description: {feature.description}</p><br>'
        response_html += f'Status - {feature.status}, Priority - {feature.priority}'
        return HttpResponse(response_html)