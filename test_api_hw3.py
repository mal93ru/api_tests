import pytest


@pytest.mark.parametrize('todo_id', [1, 200])
def test_getting_positive(session, base_url, todo_id):
    res = session.get(url=f'{base_url}/{todo_id}')

    assert res.status_code == 200
    assert res.json()['id'] == todo_id


def test_getting_negative(session, base_url, incorrect_todo_id):
    res = session.get(url=f'{base_url}/{incorrect_todo_id}')

    assert res.status_code == 404
    assert len(res.json()) == 0


@pytest.mark.parametrize('todo_index, expected', [(0, 1), (199, 10)])
def test_listing_all(session, base_url, todo_index, expected):
    res = session.get(url=f'{base_url}')
    json = res.json()
    todo = json[todo_index]

    assert todo['userId'] == expected
    assert res.status_code == 200
    assert len(res.json()) == 200


def test_creating(session, base_url):
    title = 'creating new todo!'
    completed = 'false'
    payload = {'userId': 10, 'title': title, 'completed': completed}
    res = session.post(url=f'{base_url}', json=payload)

    assert res.status_code == 201
    assert res.json()['title'] == title
    assert res.json()['userId'] == 10
    assert res.json()['completed'] == completed
    assert res.json()['id'] == 201


def test_updating_with_put_positive(session, base_url):
    title = 'test todo'
    completed = 'true'
    userId = 11
    payload = {'completed': completed, 'userId': userId, 'title': title}
    res = session.put(url=f'{base_url}/1', json=payload)

    assert res.status_code == 200
    assert res.json() == {
        'completed': completed,
        'userId': userId,
        'title': title,
        'id': 1
        }


def test_updating_with_put_negative(session, base_url, incorrect_todo_id):
    payload = {'completed': 'true'}
    res = session.put(url=f'{base_url}/{incorrect_todo_id}', json=payload)

    assert res.status_code == 500


@pytest.mark.parametrize('payload', [
    {'completed': 'true'},
    {'userId': 2},
    {'title': 'new title'}
    ])
def test_updating_with_patch(session, base_url, payload):
    res = session.patch(url=f'{base_url}/1', json=payload)

    assert res.status_code == 200
    print(type(payload))
    print(type(res.json()))
    assert str(payload)[1:-1] in str(res.json())


def test_deleting(session, base_url):
    res = session.delete(url=f'{base_url}/1')

    assert res.status_code == 200
    assert len(res.json()) == 0


@pytest.mark.parametrize('field, value', [
    ("userId", 9),
    ("id", 4),
    ("title", 'vel non beatae est'),
    ("completed", False),
    ("completed", True)
    ])
def test_filtering_positive(session, base_url, field, value):
    # res = session.get(url=f'{base_url}?userId=1&id=1')
    str_val = str(value).lower() if isinstance(value, bool) else str(value)
    res = session.get(url=f'{base_url}', params={field: str_val})

    assert res.status_code == 200
    r_json = res.json()
    assert len(r_json) > 0
    for elem in r_json:
        assert elem[field] == value


@pytest.mark.parametrize('field, value', [
    ("userId", 0),
    ("id", 0),
    ("title", 0),
    ("completed", 0)
    ])
def test_filtering_negative(session, base_url, field, value):
    str_val = str(value).lower() if isinstance(value, bool) else str(value)
    res = session.get(url=f'{base_url}', params={field: str_val})

    assert res.status_code == 200
    assert res.json() == []
