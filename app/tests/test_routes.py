
def test_get_all_cats_with_no_records(client):
    # Act
    response = client.get("/cats")
    response_body = response.get_json()

    # Assert 
    assert response.status_code == 200
    assert response_body == []

def test_post_one_cat_to_database(client):
    # Act
    response = client.get("/cats", json={"name": "shanks", 
                            "breed": "American bobtail", 
                            "personality": "spoiled rotten",
                            "age": 15
                            })
    
    response_body = response.get_data()

    # Assert 
    assert response.status_code == 201
    assert response_body == "Cat Shanks has been successfully created!"
