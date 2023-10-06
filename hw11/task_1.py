import os
import requests


def search_gif(api_key, search_word):
    params = {
        'api_key': api_key,
        'q': search_word,
        'limit': 3
    }
    url = "http://api.giphy.com/v1/gifs/search"
    try:
        resp = requests.get(url, params)
        data = resp.json()
        gifs = data.get('data', [])
        if gifs:
            print('Here are the GIF links:')
            for link in gifs:
                gif_url = link['url']
                print(gif_url)
        else:
            print("No GIFs found for the given search word.")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    api_key = os.environ.get('GIPHY_API_KEY')
    if not api_key:
        raise ValueError("Missing API Key! Ensure the GIPHY_API_KEY environment variable is set.")

    search_word = input("Enter your search word: ")

    if search_word:
        search_gif(api_key, search_word)
