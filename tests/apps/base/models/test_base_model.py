import pytest

from tests.apps.base.utils.models_list import DEBASTIANI_BASE_MODELS


class TestBaseModelFields:
    """Test basic field functionality of BaseModel"""

    @pytest.mark.parametrize("model", DEBASTIANI_BASE_MODELS)
    def test_base_model_fields(self, db, model):
        """Test required base fields"""
        instance = model()
        fields = {f.name for f in instance._meta.fields}

        required_fields = {
            "id",
            "created_at",
            "modified_at",
            "is_deleted",
            "uuid",
        }

        assert required_fields.issubset(
            fields
        ), f"Model {model.__name__} missing required base fields: {required_fields - fields}"
