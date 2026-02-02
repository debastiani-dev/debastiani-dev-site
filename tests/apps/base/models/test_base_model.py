import datetime
import uuid

import pytest
from model_bakery import baker

from tests.apps.base.utils.models_list import DEBASTIANI_BASE_MODELS


class TestBaseModelFields:
    """Test basic field functionality of BaseModel"""

    @pytest.mark.parametrize("model", DEBASTIANI_BASE_MODELS)
    def test_base_model_fields(self, db, model):
        """Test required base fields"""
        instance = model()
        fields = {f.name for f in instance._meta.fields}

        required_fields = {
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
        instance = baker.make(model)
        assert instance.uuid is not None
        assert isinstance(instance.uuid, uuid.UUID)

    @pytest.mark.parametrize("model", DEBASTIANI_BASE_MODELS)
    def test_is_deleted_is_set_on_creation(self, db, model):
        """Test is_deleted field is set to False on creation"""
        instance = baker.make(model)
        assert instance.is_deleted is False
        assert isinstance(instance.is_deleted, bool)

    @pytest.mark.parametrize("model", DEBASTIANI_BASE_MODELS)
    def test_created_at_is_set_on_creation(self, db, model):
        """Test created_at field is set on creation"""
        instance = baker.make(model)
        assert instance.created_at is not None
        assert isinstance(instance.created_at, datetime.datetime)

    @pytest.mark.parametrize("model", DEBASTIANI_BASE_MODELS)
    def test_modified_at_is_set_on_creation(self, db, model):
        """Test modified_at field is set on creation"""
        instance = baker.make(model)
        assert instance.modified_at is not None
        assert isinstance(instance.modified_at, datetime.datetime)
