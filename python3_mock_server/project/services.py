"""Main service module"""

# Standard library imports...
from urllib.parse import urljoin

# Third-party imports...
import requests

# Local imports...
from project.constants import BASE_URL

USERS_URL = urljoin(BASE_URL, 'users')


def get_users():
    """Function to get list of users from API"""
    response = requests.get(USERS_URL)

    if not response.ok:
        response = None
    return response
