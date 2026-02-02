import pytest
from model_bakery import baker

from apps.portfolio.models.projects import ProjectCategory


@pytest.mark.django_db
class TestProjectCategoryModelField:
    """Test for ProjectCategory model field existence"""

    def test_project_category_fields(self):
        """Test ProjectCategory required fields."""
        instance = baker.make(ProjectCategory)

        field = {f.name for f in instance._meta.fields}

        required_fields = {"name"}

        assert required_fields.issubset(
            field
        ), f"ProjectCategory model missing required fields: {required_fields - field}"

    def test_str_method(self):
        instance = baker.make(ProjectCategory, name="Test TestProjectCategory")
        assert str(instance) == "Test TestProjectCategory"
