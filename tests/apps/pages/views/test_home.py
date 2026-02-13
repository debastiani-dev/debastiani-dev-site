import pytest
from django.urls import reverse
from apps.pages.views.home import Project
from model_bakery import baker

@pytest.mark.django_db
class TestHomeView:
    """Test HomeView context data"""

    def test_home_view_context(self, client):
        """Test that HomeView provides featured projects in context."""
        
        baker.make(Project, is_featured=True, _quantity=3)  # Create 3 featured projects
        baker.make(Project, is_featured=False, _quantity=2)  # Create 2 non-featured projects

        assert Project.objects.all().count() == 5  # Ensure all projects are created

        response = client.get(reverse("pages:home"))
        assert response.status_code == 200
        assert "featured_projects" in response.context
        featured_projects = response.context["featured_projects"]
        assert len(featured_projects) == 3  # Should only return 3 featured projects