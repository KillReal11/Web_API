import requests


def main(locations: list) -> list:
    forecast_data = []
    for location in locations:
        url = f'https://wttr.in/{location}?MTnq&lang=ru'
        response = requests.get(url)
        response.raise_for_status()
        forecast_data.append(response.text)
    return forecast_data


if __name__ == '__main__':
    locations = ["london", "svo", "Череповец"]
    forecast_data = main(locations)
    for location in forecast_data:
        print(location)
