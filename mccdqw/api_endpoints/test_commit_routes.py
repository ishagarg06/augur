def test_committer_data(metrics):
    response = requests.get('http://localhost:5000/api/unstable/repo-groups/20/committer-data', timeout=(10, 120))
    data = response.json()
    assert response.status_code == 200
    assert len(data) >= 1