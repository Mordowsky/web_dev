from django.contrib import admin
from .models import BugReport, FeatureRequest

# Inline класс для модели Task
class BugInline(admin.TabularInline):
    model = BugReport
    extra = 0
    fields = ('title', 'description','priority', 'status', 'created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')
    can_delete = True
    show_change_link = True

# Inline класс для модели Task
class FeatureInline(admin.TabularInline):
    model = FeatureRequest
    extra = 0
    fields = ('title', 'description','priority', 'status', 'created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')
    can_delete = True
    show_change_link = True



@admin.register(BugReport)
class BugReportAdmin(admin.ModelAdmin):
    list_display = ('title','status','priority','created_at','updated_at')
    search_fields = ('title', 'description')
    list_filter = ('status', 'task', 'project')



@admin.register(FeatureRequest)
class FeatureRequestAdmin(admin.ModelAdmin):
    list_display = ('title','status','priority','created_at','updated_at')
    search_fields = ('title', 'description')
    list_filter = ('status', 'task', 'project')


# Register your models here.
