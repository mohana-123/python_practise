'''
import requests

base_url = 'https://pokeapi.co/api/v2/'
def get_pokemon_info(name):
    url = f"{base_url}/pokemon/{name}"
    response = requests.get(url)
    print(response.ok)

    if response.status_code == 200:
        poke_data = response.json()
        return poke_data
    else:
        print(f"Failed to retrive! {response.status_code}")

pokemon_name = input()
pokemon_info = get_pokemon_info(pokemon_name)

if pokemon_info:
    print(f"Name: {pokemon_info['name']}")
    print(f"ID: {pokemon_info['id']}")
    print(f"Height: {pokemon_info['height']}")
    print(f"Weight: {pokemon_info['weight']}")
'''


import requests

# url = 'https://reqres.in/api/users'
url = 'https://jsonplaceholder.typicode.com/posts'
# params = {"page" : 2}
payload = {
    "title" : "Hello from python",
    "body" : "This is a test post",
    "userId" : 1
}

response = requests.post(url, json=payload)
# print(response.ok)
print(response.status_code)
# print(f"final url : {response.url}")



# response.raise_for_status()

data = response.json()
# print("post tile:", data['title'])
print(data)
# for user in data:
#     print(user['title'])