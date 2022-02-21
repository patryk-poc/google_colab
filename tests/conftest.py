""" Pytest configuration tests fixtures and other helper methods """
import random

import pytest
from example.web.rest import Web


@pytest.fixture(scope="module")
def random_num():
    """Test fixture"""
    return random.randint(1, 10)


@pytest.fixture()
def client():
    """Get a web client"""
    yield Web()
