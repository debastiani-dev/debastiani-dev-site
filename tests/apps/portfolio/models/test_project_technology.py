import pytest
from model_bakery import baker

from apps.portfolio.models.projects import ProjectCategory, ProjectTechnology


@pytest.mark.django_db
class TestProjectTechnologyModelField:
    """Test for ProjectTechnology model field existence"""

    def test_project_category_fields(self):
        """Test ProjectCategory required fields."""

        baker.make(ProjectCategory)

        field = {f.name for f in ProjectTechnology._meta.fields}

        required_fields = {
            "name",
        }

        assert required_fields.issubset(field), (
            f"ProjectTechnology model missing required fields: "
            f"{required_fields - field}"
        )

    def test_str_method(self):
        """Test __str__ method of ProjectTechnology model."""
        instance = baker.make(ProjectTechnology, name="Test ProjectTechnology")
        assert str(instance) == "Test ProjectTechnology"
