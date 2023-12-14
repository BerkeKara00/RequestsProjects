import requests

def get_pokemon_info(pokemon_name):
    base_url = "https://pokeapi.co/api/v2/pokemon/"
    url = f"{base_url}{pokemon_name.lower()}/"

    response = requests.get(url)

    if response.status_code == 200:
        pokemon_data = response.json()

        # İlgili bilgileri çıkartabilirsiniz
        pokemon_name = pokemon_data['name']
        pokemon_id = pokemon_data['id']
        pokemon_types = [t['type']['name'] for t in pokemon_data['types']]
        pokemon_stats = {stat['stat']['name']: stat['base_stat'] for stat in pokemon_data['stats']}

        # Örneğin, ekrana bazı bilgileri yazdıralım
        print(f"Pokemon Name: {pokemon_name}")
        print(f"Pokemon ID: {pokemon_id}")
        print(f"Pokemon Types: {', '.join(pokemon_types)}")
        print("Pokemon Stats:")
        for stat, value in pokemon_stats.items():
            print(f"  {stat}: {value}")

    else:
        print(f"Error: Could not retrieve data for {pokemon_name}")

if __name__ == "__main__":
    pokemon_name = input("Enter the name of the Pokemon: ")
    get_pokemon_info(pokemon_name)
