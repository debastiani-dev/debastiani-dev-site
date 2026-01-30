import pytest
from django.contrib.auth import get_user_model

User = get_user_model()


@pytest.mark.django_db
class TestUserModelFields:
    """Test basic field functionality of User model"""

    def test_user_model_fields(self):
        """Test required user fields"""
        instance = User()
        fields = {f.name for f in instance._meta.fields}

        required_fields = {
            "email",
            "first_name",
            "last_name",
            "is_active",
            "is_admin",
        }

        assert required_fields.issubset(
            fields
        ), f"User model missing required fields: {required_fields - fields}"

    def test_full_name_property(self):
        """Test full_name property"""
        user = User.objects.create(
            email="test@example.com", first_name="Test", last_name="User"
        )
        assert user.fullname == "Test User"

    def test_is_staff_property(self):
        """Test is_staff property"""
        user = User.objects.create(
            email="test@example.com", first_name="Test", last_name="User", is_admin=True
        )
        assert user.is_staff is True
        assert user.is_staff == user.is_admin

    def test_str_method(self):
        """Test __str__ method"""
        user = User.objects.create(
            email="test@example.com",
            first_name="Test",
            last_name="User",
        )
        assert str(user) == f"test@example.com ({user.uuid})"
