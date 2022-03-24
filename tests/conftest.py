""" Pytest configuration tests fixtures and other helper methods """
import random

import pytest
from example.web.rest import Web


@pytest.fixture(scope="module")
def random_num():
    """Random int number

    Yields:
        int: return a random number from 1 to 9
    """
    yield random.randint(1, 9)


@pytest.fixture()
def client():
    """Get a web client"""
    yield Web()
