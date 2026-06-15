def test_activities_get_returns_200(client):
    response = client.get("/activities")
    assert response.status_code == 200


def test_activities_get_returns_dict(client):
    response = client.get("/activities")
    data = response.json()
    assert isinstance(data, dict)
    assert len(data) > 0


def test_activities_have_required_fields(client):
    response = client.get("/activities")
    data = response.json()
    required = {"description", "schedule", "max_participants", "participants"}
    for name, details in data.items():
        assert required.issubset(details.keys())
        assert isinstance(details["participants"], list)
