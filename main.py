import requests

API_TOKEN = 'eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJjYzY2Mjg5YTE2Mjg4OWQxMGE5Njg0YjIxNTlmOGM2MiIsIm5iZiI6MTczMzUyMDk2NS45NSwic3ViIjoiNjc1MzZlNDU4MDJiYWQxNjA5MWFjODA0Iiwic2NvcGVzIjpbImFwaV9yZWFkIl0sInZlcnNpb24iOjF9.YFOgUfBNFcE_15zQxhUSoVj4sIq40kiAEws_368wHIg'

def show_movies(id):
    urls = {
        1: 'now_playing',
        2: 'popular',
        3: 'top_rated',
        4: 'upcoming'
        }
    url = f'https://api.themoviedb.org/3/movie/{urls[id]}?language=en-US&page=1'

    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {API_TOKEN}"
    }

    try:
        response = requests.get(url, headers=headers)
        data = response.json()

        return [movie['title'] for movie in data['results']]
    except requests.exceptions.ConnectionError:
        print("Помилка: неможливо підключитися до сервера.")
    except requests.exceptions.Timeout:
        print("Помилка: сервер не відповідає вчасно.")
    except requests.exceptions.HTTPError as e:
        print(f"HTTP помилка: {e.response.status_code}")
    except KeyError:
        print("Помилка: очікуваний ключ відсутній у даних.")

    return []



def main():
    print('Which type of movies you would like to see?\n')
    print('1. Playing\n2. Popular\n3. Top Rated\n4. Upcoming\n')
    
    while True:
        type_of_movies = input('Enter your choice(1, 2, 3, 4): ')
        print('\n')
        try:
            type_of_movies = int(type_of_movies)
            if type_of_movies in(1,2,3,4):
                result = show_movies(type_of_movies)
                for i, title in enumerate(result, start=1):
                    print(f'{i}) {title}')
                break
            else:
                print('Invalid choice. Please enter 1, 2, 3 or 4.\n')
        except ValueError:
            print('Invalid input. Please enter a number (1, 2, 3 or 4).\n')

while True:
    print('Want to see some movies?\n\n')
    print('1. Yes\n2. No')
    end_or_cont = input('Enter your choice (1 or 2): ')
    if end_or_cont == '1':
        main()
    elif end_or_cont == '2':
        print("Goodbye!")
        break