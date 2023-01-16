from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

def test_get_completed():
    response = client.get("/comleted/37cb79f5-baa9-4617-8388-aee408cd613f")
    assert response.status_code == 200
    assert response.json == [
  {
    "time": 10800,
    "t_guid": "64ab1c2f-fee2-47be-aa32-d5b6516c5dc3",
    "name": "Задача 3045"
  },
  {
    "time": 14400,
    "t_guid": "6a7a0871-224f-478b-b945-af8bd7651ecc",
    "name": "Задача 6430"
  },
  {
    "time": 7200,
    "t_guid": "b5ab1cd8-2270-4e73-9c99-49f818ddf5c9",
    "name": "Задача 6252"
  },
  {
    "time": 14400,
    "t_guid": "6a7a0871-224f-478b-b945-af8bd7651ecc",
    "name": "Задача 6430"
  }
]

def test_get_tours():
    response = client.get("/tours")
    assert response.status_code == 200

def test_get_teams():
    response = client.get("/teams/2e7cf118-bd0e-4dfd-9d6a-058807310667")
    assert response.status_code == 200
    assert response.json == {
  "name": "команда 4082",
  "users": [
    {
      "name": "Evelyn Restivo"
    },
    {
      "name": "Bradley Smith"
    },
    {
      "name": "James Slane"
    },
    {
      "name": "Norma Parker"
    },
    {
      "name": "David Lopez"
    }
  ]
}