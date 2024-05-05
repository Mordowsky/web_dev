from django.urls import path
from quality_control import views

app_name = 'quality_control'

urlpatterns = [
    path('quality_control/', views.IndexView.as_view(), name = 'quality_control_page'),
    path('bugs/', views.bug_list, name='bugs_list'),
    path('bugs/<int:bug_id>/', views.BugView.as_view(), name = 'bug_detail'),
    path('bugs/new', views.add_bug, name = 'add_bug'),
    path('features/', views.feature_list, name='features_list'),  
    path('features/new', views.add_feature, name = 'add_feature'),
    path('features/<int:feature_id>/', views.FeatureView.as_view(), name = 'feature_detail'),
    path('bug/<int:bug_id>/update/', views.update_bug, name='bug_update'),
    path('feature/<int:feature_id>/update/', views.update_feature, name='feature_update'),  
    path('bug/<int:bug_id>/delete/', views.delete_bug, name='delete_bug'),
    path('feature/<int:feature_id>/delete/', views.delete_feature, name='delete_feature'),
]