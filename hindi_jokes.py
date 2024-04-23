import requests
import json


def get_hindi_joke():
    url = "https://jokes.one/api/joke/"
    headers = {"Content-Type": "application/json"}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        try:
            joke_data = response.json()
            joke_text = joke_data['joke']['text']
            return joke_text
        except json.JSONDecodeError:
            return "Failed to parse JSON response"
    else:
        return "Failed to fetch joke"


def main():
    print("Fetching a Hindi joke...\n")
    joke = get_hindi_joke()
    print("Here's a Hindi joke for you:")
    print(joke)


if __name__ == "__main__":
    main()
