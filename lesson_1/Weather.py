import requests


def main():
    locations = ["london", "svo", "Череповец"]
    params = {
        'M': '',
        'T': '',
        'n': '',
        'q': '',
        'lang': 'ru',
    }
    for location in locations:
        url = f'https://wttr.in/{location}'
        response = requests.get(url, params=params)
        response.raise_for_status()
        print(response.text)


if __name__ == '__main__':
    main()
