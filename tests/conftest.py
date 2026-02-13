import pytest
from django.test import Client


@pytest.fixture
def client():
    """Fixture for Django test client."""
    return Client()