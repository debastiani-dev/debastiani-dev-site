import pytest
from django.contrib.auth import get_user_model
User = get_user_model()

@pytest.mark.django_db
class TestUserManager:
    """Test UserManager functionality"""
    def test_create_user(self):
        user = User.objects.create_user(
            email="test@example.com",
            first_name="Test",
            last_name="User",
            password="testpassword"
        )
        assert user.email == "test@example.com"
        assert user.first_name == "Test"
        assert user.last_name == "User"
        assert user.is_active is True
        assert user.is_admin is False

    def test_create_user_no_email(self):
        with pytest.raises(ValueError, match="Users must have an email address") as excinfo:
            User.objects.create_user(
                email="",
                first_name="Test",
                last_name="User",
                password="testpassword"
            )        

    def test_create_superuser(self):
        user = User.objects.create_superuser(
            email="test@example.com",
            first_name="Test",
            last_name="User",
            password="testpassword"
        )
        assert user.is_admin is True
        assert user.is_superuser is True

    