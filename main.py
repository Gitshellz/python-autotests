import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'b6dae5ea77bffb6833aa7f5e6f109929'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}

body_create = {
    "name": "Zorro",
    "photo_id": "15"
}

body_change = {
    "pokemon_id": "",
    "name": "anyname",
    "photo_id": "14"
}

body_addpokeball = {
    "pokemon_id": ""
}

responce_create = requests.post(url=f'{URL}/pokemons', headers = HEADER, json = body_create)
print(responce_create.text)

pokemon_id = responce_create.json().get('id')

if pokemon_id:
    body_change["pokemon_id"] = pokemon_id
    responce_change = requests.put(url=f'{URL}/pokemons', headers = HEADER, json = body_change)
    print(responce_change.text)
    body_addpokeball ["pokemon_id"] = pokemon_id
    responce_addpokeball = requests.post(url=f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_addpokeball)
    print(responce_addpokeball.text)
