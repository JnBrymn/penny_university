import pytest

from rest_framework.test import APIClient

from users.models import User
from users.tokens import verification_token


@pytest.mark.django_db
def test_register_user(test_social_profile, mocker):
    client = APIClient()
    data = {
        'email': 'test@profile.com',
        'password': 'password',
        'first_name': 'test',
        'last_name': 'profile',
    }
    with mocker.patch.object(User, 'send_verification_email'):
        response = client.post('/api/auth/register/', data=data, format='json')
    assert response.status_code == 204
    user = User.objects.get(email='test@profile.com')
    assert not user.is_verified
    assert user.has_usable_password()
    assert user.first_name == 'test' and user.last_name == 'profile'


@pytest.mark.django_db
def test_verify_email(test_user):
    client = APIClient()
    test_user.save()
    data = {
        'token': verification_token.make_token(test_user),
        'email': test_user.email,
    }
    response = client.post('/api/auth/verify/', data=data, format='json')
    test_user.refresh_from_db()
    assert response.status_code == 204
    assert test_user.is_verified


@pytest.mark.django_db
def test_verify_email__invalid_token(test_user):
    client = APIClient()
    other_user = User.objects.create_user(
        username='other@test.com',
        email='other@test.com',
        password='password',
    )
    data = {
        'token': verification_token.make_token(other_user),
        'email': test_user.email
    }
    response = client.post('/api/auth/verify/', data=data, format='json')
    assert response.status_code == 400


@pytest.mark.django_db
def test_checking_user_exists(test_user):
    client = APIClient()
    data_does_exist = {
        'email': 'test@profile.com',
    }
    data_does_not_exist = {
        'email': 'fail@profile.com',
    }
    response = client.post('/api/auth/exists/', data_does_exist, format='json')
    assert response.status_code == 200

    response = client.post('/api/auth/exists/', data_does_not_exist, format='json')
    assert response.status_code == 400


@pytest.mark.django_db
def test_user_log_in__verified_and_protected_request(test_social_profile, test_user):
    client = APIClient()
    test_user.is_verified = True
    test_user.save()
    test_social_profile.user = test_user
    test_social_profile.save()
    data = {
        'email': 'test@profile.com',
        'password': 'password'
    }
    response = client.post('/api/auth/login/', data=data, format='json')
    assert response.status_code == 200
    client.credentials(HTTP_AUTHORIZATION='Token ' + response.data['key'])
    data = {
        'title': 'Create Chat',
        'description': 'Testing creating a chat',
        'date': '2020-01-01T00:00'
    }
    response = client.post('/api/chats/', data=data, format='json')
    assert response.status_code == 201


@pytest.mark.django_db
def test_user_log_in__not_verified(test_user):
    client = APIClient()
    data = {
        'email': 'test@profile.com',
        'password': 'password'
    }
    response = client.post('/api/auth/login/', data=data, format='json')
    assert response.status_code == 400


@pytest.mark.django_db
def test_user_detail(test_user):
    client = APIClient()
    response = client.get(f'/api/users/{test_user.id}/')
    assert response.data['email'] == 'test@profile.com'
