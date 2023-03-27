import pytest
from .factories import UserFactory, NoteFactory


@pytest.fixture
def logged_user(client):
    user = UserFactory()
    client.login(username=user.username, password='password')
    return user


@pytest.mark.django_db
def test_list_endpoint_return_user_notes(client, logged_user):
    note = NoteFactory(user=logged_user)

    response = client.get(path='/smart/notes')
    assert 200 == response.status_code
    assert note.title in str(response.content)


@pytest.mark.django_db
def test_create_endpoint_receives_from_data(client, logged_user):
    form_data = {'title': 'new title', 'text': 'new text'}

    response = client.post(path='/smart/notes/new', data=form_data, follow=True)

    assert 200 == response.status_code
    assert 'notes/list.html' in response.template_name
    assert 1 == logged_user.notes.count()
    assert "new title" == logged_user.notes.first().title

