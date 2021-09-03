"""Test for get todos function"""

# Standard library imports...
from unittest.mock import Mock, patch

# Third-party imports...
from nose.tools import assert_is_none, assert_list_equal

# Local imports...
from project.services import get_users

class TestTodos:
    """Placeholder"""

    @classmethod
    def setup_class(cls):
        """Placeholder"""
        cls.mock_get_patcher = patch('project.services.requests.get')
        cls.mock_get = cls.mock_get_patcher.start()

    @classmethod
    def teardown_class(cls):
        """Placeholder"""
        cls.mock_get_patcher.stop()

    def test_getting_todos_when_response_is_ok(self):
        """Test if todo() can return non empty response"""
        # Configure the mock to return a response with an OK status code.
        self.mock_get.return_value.ok = True

        todos = [{
            'userId': 1,
            'id': 1,
            'title': 'Make the bed',
            'completed': False
        }]

        self.mock_get.return_value = Mock()
        self.mock_get.return_value.json.return_value = todos

        # Call the service, which will send a request to the server.
        response = get_users()

        # If the request is sent successfully, then I expect a response to be returned.
        assert_list_equal(response.json(), todos)

    def test_getting_todos_when_response_is_not_ok(self):
        """Test output of todo() if response is not correct"""
        # Configure the mock to not return a response with an OK status code.
        self.mock_get.return_value.ok = False

        # Call the service, which will send a request to the server.
        response = get_users()

        # If the response contains an error, I should get no todos.
        assert_is_none(response)

    def test_getting_todos_when_response_404(self):
        """Test how todo() behaves for not found page"""
        # Configure the mock to not return a response with an OK status code.

        self.mock_get.return_value.ok = False
        self.mock_get.return_value.status_code.return_value = 404

        # Call the service, which will send a request to the server.
        response = get_users()

        # If the response contains an error, I should get no todos.
        assert_is_none(response)
