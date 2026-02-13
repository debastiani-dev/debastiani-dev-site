import pytest
from django.urls import reverse
from apps.portfolio.views.projects import Project
from model_bakery import baker

@pytest.mark.django_db
class TestProjectViews:
    """Test ProjectListView and ProjectDetailView"""

    def test_project_list_view(self, client):
        """Test that ProjectListView returns active projects in context."""
        
        baker.make(Project, is_featured=True, _quantity=4)  # Create 4 active projects
        baker.make(Project, is_featured=False, _quantity=2)  # Create 2 inactive projects

        assert Project.objects.all().count() == 6  # Ensure all projects are created

        response = client.get(reverse("portfolio:list"))
        assert response.status_code == 200
        assert "projects" in response.context
        projects = response.context["projects"]
        assert len(projects) == 6  # Should return all projects (active and inactive)

    def test_project_detail_view(self, client):
        """Test that ProjectDetailView returns the correct project."""
        
        project = baker.make(Project, is_featured=True)  # Create a single featured project

        response = client.get(reverse("portfolio:detail", kwargs={"pk": project.pk}))
        assert response.status_code == 200
        assert "project" in response.context
        detail_project = response.context["project"]
        assert detail_project.pk == project.pk  # Should return the correct project