
def test_get_all_cats_with_no_records(client):
  response = client.get("/cats")
  response_body = response.get_json()
  assert response.status_code == 200
  assert response_body == []

def test_post_one_cat_to_database(client):
  response = client.post("/cats", json={
    "name": "Shanks", 
    "breed": "American Bobtail", 
    "personality": "spoiled rotten",
    "age": 15
    })
  response_body = response.get_data(as_text=True)
  
  assert response.status_code == 201
  assert response_body == "Cat Shanks has been successfully created!"