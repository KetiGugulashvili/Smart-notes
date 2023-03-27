from django.contrib.auth.models import User
import pytest


def test_home_endpoint_returns_welcome_page(client):
    response = client.get(path='/')
    assert response.status_code == 200
    assert 'Welcome to smartnotes' in str(response.content)


@pytest.mark.django_db
def test_register_endpoint_redirects_authenticated_user(client):
    user = User.objects.create_user('Keti', 'keti@gmail.com', 'password')
    client.login(username=user.username, password='password')
    assert user.is_authenticated

    response = client.get(path='/register', follow=True)
    print(type(response))
    assert response.status_code == 200
    assert 'notes/list.html' in response.template_name

