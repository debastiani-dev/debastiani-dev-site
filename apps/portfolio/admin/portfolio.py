from django.contrib import admin

from apps.portfolio.models.projects import Project, ProjectCategory, ProjectTechnology


@admin.register(ProjectCategory)
class ProjectCategoryAdmin(admin.ModelAdmin):
    list_display = ["name"]


@admin.register(ProjectTechnology)
class ProjectTechnologyAdmin(admin.ModelAdmin):
    list_display = ["name"]


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "customer_name",
        "category",
        "started_at",
        "is_featured",
    ]
    list_filter = [
        "is_featured",
        "category",
        "technologies",
    ]
    search_fields = [
        "title",
        "customer_name",
        "short_description",
    ]
    filter_horizontal = ["technologies"]
