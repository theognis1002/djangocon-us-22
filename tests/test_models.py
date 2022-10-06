import pytest
from django.apps import apps

User = apps.get_model("users", "User")


pytestmark = pytest.mark.django_db


def test_simple_test():
    assert True
