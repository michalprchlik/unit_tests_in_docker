"""Placeholder"""

# Standard library imports...
from unittest import skipIf

# Third-party imports...
from nose.tools import assert_dict_contains_subset, assert_is_instance, assert_true

# Local imports...
from project.constants import SKIP_REAL
from project.services import get_users


@skipIf(SKIP_REAL, 'Skipping tests that hit the real API server.')
def test_request_response():
    """Placeholder"""
    response = get_users()

    expected_headers = {'Content-Type': 'application/json; charset=utf-8'}
    assert_dict_contains_subset(expected_headers, response.headers)
    assert_true(response.ok)
    assert_is_instance(response.json(), list)
