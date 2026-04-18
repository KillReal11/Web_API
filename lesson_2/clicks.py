import requests
import json
from dotenv import load_dotenv
import os


def shorten_link(token, long_url):
    url = 'https://clc.li/api/url/add'
    headers = {
        'Authorization': token,
        'Content-Type': 'application/json'
    }
    data = {
        'url': long_url,
        "status": "public"
    }
    response = requests.post(url, headers=headers, json=data)
    response.raise_for_status()
    answer = response.json()
    error = answer.get('error')
    if error == 1:
        return None
    else:
        short_url_full = answer.get('shorturl')
    return short_url_full


def count_clicks(token, long_url):
    url = 'https://clc.li/api/urls?limit=2&page=1&order=date'
    headers = {
        'Authorization': token,
        'Content-Type': 'application/json'
    }
    params = {
        'q': long_url
    }
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    answer = response.json()
    data = answer.get('data')
    urls = data.get('urls')
    for link in urls:
        if link.get('longurl') == long_url:
            overall_clicks = link.get('clicks')
            unique_clicks = link.get('uniqueclicks')
            return overall_clicks, unique_clicks
        else:
            return None


def is_bitlink(token, long_url):
    url = 'https://clc.li/api/urls?limit=2&page=1&order=date'
    headers = {
        'Authorization': token,
        'Content-Type': 'application/json'
    }
    params = {
        'q': long_url
    }
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    answer = response.json()
    data = answer.get('data')
    urls = data.get('urls')
    if urls:
        return True
    else:
        return False


def main():
    load_dotenv()
    token = os.getenv('token')
    long_url = input('Введите ссылку, которую хотите сократить:')
    if is_bitlink(token, long_url):
        clicks_number = count_clicks(token, long_url=long_url)
        print('Всего кликов:', clicks_number[0])
        print('Уникальных кликов:', clicks_number[1])
    else:
        short_url = shorten_link(token, long_url)
        if short_url:
            print('Новая короткая ссылка -->', short_url)
        else:
            print('Вы ввели некорректную ссылку!')


if __name__ == '__main__':
    main()
