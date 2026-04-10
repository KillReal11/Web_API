import requests


def main():
    locations = ["london", "svo", "Череповец"]
    for loc in locations:
        url = f'https://wttr.in/{loc}?MTnq&lang=ru'
        response = requests.get(url)
        response.raise_for_status()
        print(response.text)


if __name__ == '__main__':
    main()