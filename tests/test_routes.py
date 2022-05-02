def test_get_all_dogs_with_empty_db_returns_empty_list(client):
    response = client.get('/dogs')

    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == []

def test_get_one_dog_with_populated_db_returns_dog_json(client, two_dogs):
    response = client.get("dogs/1")
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == {
        "id": 1,
        "age": 7,
        "name": "Roscoe"
    }

def test_get_one_dog_with_empty_db_returns_404(client):
    response = client.get("dogs/1")
    assert response.status_code == 404

def test_post_one_dog_creates_dog_in_db(client):
    response = client.post("dogs", json={
        "name": "Julius",
        "age": 5
    })

    response_body = response.get_json()
    assert response.status_code == 201
    assert "id" in response_body
    assert "msg" in response_body