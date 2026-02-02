import pytest
from model_bakery import baker

from apps.portfolio.models.projects import Project, ProjectTechnology


@pytest.mark.django_db
class TestProjectModelsFields:
    """Tests for Project models fields existence and types."""

    def test_project_models_fields(self):
        """Test Project required fields."""
        technology_instance = baker.make(ProjectTechnology)
        instance = baker.make(Project)
        instance.technologies.add(technology_instance)

        fields = {f.name for f in instance._meta.fields} | {
            f.name for f in instance._meta.many_to_many
        }

        required_fields = {
            "title",
            "category",
            "customer_name",
            "short_description",
            "long_description",
            "cover_image",
            "is_featured",
            "technologies",
            "started_at",
        }

        assert required_fields.issubset(
            fields
        ), f"Project model missing required fields: {required_fields - fields}"

    def test_str_method(self):
        """Test __str__ method of Project model."""
        instance = baker.make(Project, title="Test Project")

        assert str(instance) == "Test Project"
