from django.views.generic import TemplateView
from apps.portfolio.models import Project

class HomeView(TemplateView):
    template_name = "pages/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Fetch the 3 most recent FEATURED projects
        context["featured_projects"] = Project.objects.filter(
            is_featured=True
        ).select_related("category").order_by("-started_at")[:3]
        return context