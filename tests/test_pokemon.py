import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'b6dae5ea77bffb6833aa7f5e6f109929'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}
TRAINER_ID = 17982

def test_status_GETtrainers():
    response = requests.get(url =f'{URL}/trainers')
    assert response.status_code == 200

def test_avalivable_id():
    response_get = requests.get(url =f'{URL}/trainers', params= {'trainer_id' : TRAINER_ID})
    assert response_get.json()["data"][0]["id"] == '17982'

