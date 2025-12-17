import pytest
import uuid

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

    @pytest.mark.parametrize("model", DEBASTIANI_BASE_MODELS)
    def test_uuid_is_set_on_creation(self, db, model):
        """Test UUID field is set on creation"""
        instance = model.objects.create()
        assert instance.uuid is not None
        assert isinstance(instance.uuid, uuid.UUID) 

    @pytest.mark.parametrize("model", DEBASTIANI_BASE_MODELS)
    def test_is_deleted_is_set_on_creation(self, db, model):
        """Test is_deleted field is set to False on creation"""
        instance = model.objects.create()
        assert instance.is_deleted is False
        assert isinstance(instance.is_deleted, bool)
