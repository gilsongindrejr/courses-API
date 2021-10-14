import requests
import pytest

from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

from courses.models import Course

pytestmark = pytest.mark.django_db


@pytest.fixture
def headers():
    """
    Creates the header needed for authorization in endpoints that are restrict,
    need a test user with a valid token.
    :return: dict
    """
    return {'Authorization': 'token 1522280f82b2f28aa26e9d073bcce97e4b442d3a'}


@pytest.fixture
def courses_url():
    return 'http://127.0.0.1:8000/api/v2/courses/'


@pytest.fixture
def courses_data():
    return {
        "id": 455,
        "title": "Test course",
        "url": "http://www.tests.com/tests"
    }


# The tests below are tests for anonymous user in courses endpoint
def test_get_courses_anon(courses_url):
    request = requests.get(url=courses_url)
    assert request.status_code == 401


def test_post_courses_anon(courses_url, courses_data):
    request = requests.post(url=courses_url, data=courses_data)
    assert request.status_code == 401


def test_put_courses_anon(courses_url, courses_data):
    request = requests.put(url=f'{courses_url}1/', data=courses_data)
    assert request.status_code == 401


def test_delete_courses_anon(courses_url):
    request = requests.delete(url=f'{courses_url}1/')
    assert request.status_code == 401


# The tests below are tests for authorized user in courses endpoint
def test_get_courses_auth(headers, courses_url):
    request = requests.get(url=courses_url, headers=headers)
    assert request.status_code == 200


def test_post_courses_auth(headers, courses_url, courses_data):
    request = requests.post(url=courses_url, headers=headers, data=courses_data)
    assert request.status_code == 201
