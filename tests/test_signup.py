def test_signup_success(client):
    email = "newstudent@example.com"
    response = client.post("/activities/Chess Club/signup", params={"email": email})
    assert response.status_code == 200
    data = response.json()
    assert "message" in data


def test_signup_duplicate_returns_400(client):
    # michael@mergington.edu is in the initial data
    response = client.post("/activities/Chess Club/signup", params={"email": "michael@mergington.edu"})
    assert response.status_code == 400
    data = response.json()
    assert "detail" in data


def test_signup_nonexistent_activity_returns_404(client):
    response = client.post("/activities/NoSuchActivity/signup", params={"email": "x@x.com"})
    assert response.status_code == 404
    data = response.json()
    assert "detail" in data


def test_signup_updates_participants_list(client):
    email = "ts@example.com"
    client.post("/activities/Programming Class/signup", params={"email": email})
    res = client.get("/activities")
    data = res.json()
    assert email in data["Programming Class"]["participants"]
