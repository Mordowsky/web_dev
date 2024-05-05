from django.views import View
from django.views.generic import DetailView
from .models import BugReport, FeatureRequest
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from .forms import BugReportForm, FeatureRequestForm

class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'quality_control/index.html')   


def index(request):
    return render(request, 'quality_control/index.html')


def bug_detail(request, bug_id):
    bug = get_object_or_404(BugReport, id=bug_id)
    return render(request, 'quality_control/bug_detail.html', {'bug': bug})


def feature_id_detail (request, feature_id):
    feature = get_object_or_404(FeatureRequest, id=feature_id)
    return render(request, 'quality_control/feature_detail.html', {'feature': feature})

def bug_list(request):
    bugs = BugReport.objects.all()
    return render(request, 'quality_control/bugs_list.html', {'bugs': bugs})


def feature_list(request):
    features = FeatureRequest.objects.all()
    return render(request, 'quality_control/features_list.html', {'features': features})


class BugView(DetailView):
    model = BugReport
    pk_url_kwarg='bug_id'
    template_name = 'quality_control/bug_detail.html'

    
class FeatureView(DetailView):
    model = FeatureRequest
    pk_url_kwarg='feature_id'
    template_name = 'quality_control/feature_detail.html'

def add_bug(request):
    if request.method == 'POST':
        form = BugReportForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('quality_control:bugs_list')
    else:
        form = BugReportForm()
    return render(request, 'quality_control/bug_report_form.html', {'form': form})

def add_feature(request):
    if request.method == 'POST':
        form = FeatureRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('quality_control:features_list')
    else:
        form = FeatureRequestForm()
    return render(request, 'quality_control/feature_request_form.html', {'form': form})