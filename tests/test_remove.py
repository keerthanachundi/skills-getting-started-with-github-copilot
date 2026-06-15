def test_remove_success(client):
    email = "toremove@example.com"
    # add then remove
    client.post("/activities/Soccer Team/signup", params={"email": email})
    res = client.delete(f"/activities/Soccer Team/participants/{email}")
    assert res.status_code == 200
    data = res.json()
    assert "message" in data


def test_remove_nonexistent_participant_returns_404(client):
    res = client.delete("/activities/Chess Club/participants/nope@example.com")
    assert res.status_code == 404
    data = res.json()
    assert "detail" in data


def test_remove_from_nonexistent_activity_returns_404(client):
    res = client.delete("/activities/NoActivity/participants/x@example.com")
    assert res.status_code == 404
    data = res.json()
    assert "detail" in data


def test_remove_updates_participants_list(client):
    email = "toremove2@example.com"
    client.post("/activities/Drama Club/signup", params={"email": email})
    client.delete(f"/activities/Drama Club/participants/{email}")
    res = client.get("/activities")
    data = res.json()
    assert email not in data["Drama Club"]["participants"]
