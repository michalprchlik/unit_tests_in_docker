"""Placeholder"""

# Third-party imports...
from unittest.mock import patch
from nose.tools import assert_dict_contains_subset, assert_list_equal, assert_true, assert_is_none, assert_equal
import requests

# Local imports...
from project.services import get_users
from project.tests.mocks import get_free_port, start_mock_server


class TestMockServer:
    """Placeholder"""
    @classmethod
    def setup_class(cls):
        """Placeholder"""
        cls.mock_server_port = get_free_port()
        start_mock_server(cls.mock_server_port)

    def test_request_response(self):
        """Test empty response"""
        mock_users_url = 'http://localhost:{port}/users'.format(port=self.mock_server_port)

        # Patch USERS_URL so that the service uses the mock server URL instead of the real URL.
        with patch.dict('project.services.__dict__', {'USERS_URL': mock_users_url}):
            response = get_users()

        expected_header = {'Content-Type': 'application/json; charset=utf-8'}
        assert_dict_contains_subset(expected_header, response.headers)
        assert_true(response.ok)
        assert_list_equal(response.json(), [])

    def test_request_response_sers_id_1(self):
        """Test non empty response"""
        mock_users_url = 'http://localhost:{port}/users/1'.format(port=self.mock_server_port)

        # Patch USERS_URL so that the service uses the mock server URL instead of the real URL.
        with patch.dict('project.services.__dict__', {'USERS_URL': mock_users_url}):
            response = get_users()

        todo1 = [{
            'userId': 1,
            'id': 1,
            'title': 'Make the bed',
            'completed': False
        }]

        expected_header = {'Content-Type': 'application/json; charset=utf-8'}
        assert_dict_contains_subset(expected_header, response.headers)
        assert_true(response.ok)
        assert_equal(response.json(), todo1)

    def test_request_response_404(self):
        """Test page not found"""
        mock_users_url = 'http://localhost:{port}/page_not_found'.format(port=self.mock_server_port)

        # Patch USERS_URL so that the service uses the mock server URL instead of the real URL.
        with patch.dict('project.services.__dict__', {'USERS_URL': mock_users_url}):
            response = get_users()

        assert_is_none(response)

        with patch.dict('project.services.__dict__', {'USERS_URL': mock_users_url}):
            response = requests.get(mock_users_url)

        assert_equal(response.status_code, 404)

    def test_request_response_methods(self):
        """Test invalid HTTP methods"""
        mock_users_url = 'http://localhost:{port}/users'.format(port=self.mock_server_port)

        response = requests.post(mock_users_url)
        assert_equal(response.status_code, 405)

        response = requests.delete(mock_users_url)
        assert_equal(response.status_code, 405)

        response = requests.put(mock_users_url)
        assert_equal(response.status_code, 405)
