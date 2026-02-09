from django.views.generic import ListView, DetailView
from apps.portfolio.models import Project

class ProjectListView(ListView):
    model = Project
    template_name = "portfolio/project_list.html"
    context_object_name = "projects"

    def get_queryset(self):
        # Show only featured/active projects, ordered by most recent
        return Project.objects.select_related("category").prefetch_related("technologies").order_by("-started_at")

class ProjectDetailView(DetailView):
    model = Project
    template_name = "portfolio/project_detail.html"
    context_object_name = "project"
    # NOTE: We use UUID as the primary key
    pk_url_kwarg = "pk" 