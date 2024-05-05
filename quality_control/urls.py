from django.urls import path
from quality_control import views

app_name = 'quality_control'

urlpatterns = [
    path('quality_control/', views.IndexView.as_view(), name = 'quality_control_page'),
    path('bugs/', views.BugsListView.as_view(), name='bugs_list'),
    path('bugs/<int:bug_id>/', views.BugView.as_view(), name = 'bug_detail'),
    path('bugs/new', views.BugCreateView.as_view(), name = 'add_bug'),
    path('features/', views.FeaturesListView.as_view(), name='features_list'),  
    path('features/new', views.FeatureCreateView.as_view(), name = 'add_feature'),
    path('features/<int:feature_id>/', views.FeatureView.as_view(), name = 'feature_detail'),
    path('bug/<int:bug_id>/update/', views.BugUpdateView.as_view(), name='bug_update'),
    path('feature/<int:feature_id>/update/', views.FeatureUpdateView.as_view(), name='feature_update'),  
    path('bug/<int:bug_id>/delete/', views.BugDeleteView.as_view(), name='delete_bug'),
    path('feature/<int:feature_id>/delete/', views.FeatureDeleteView.as_view(), name='delete_feature'),
]