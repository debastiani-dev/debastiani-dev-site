import pytest
from django.urls import reverse

@pytest.mark.django_db
class TestAboutView:
    """Test AboutView response."""

    def test_about_view(self, client):
        """Test that AboutView returns 200."""
        response = client.get(reverse("pages:about"))
        assert response.status_code == 200
