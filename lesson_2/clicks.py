import requests
from dotenv import load_dotenv
import os
import json


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
    short_url_full = answer.get('shorturl')
    return short_url_full


def count_clicks(token, long_url):
    url = 'https://clc.li/api/urls'
    headers = {
        'Authorization': token,
        'Content-Type': 'application/json'
    }
    params = {
        'limit': '2',
        'page': '1',
        'order': 'date',
        'q': long_url
    }
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    answer = response.json()
    print(json.dumps(answer, indent=4, ensure_ascii=False))
    main_part = answer.get('data')
    urls = main_part.get('urls')
    for link in urls:
        if link.get('longurl') != long_url:
            return None
        overall_clicks = link.get('clicks')
        unique_clicks = link.get('uniqueclicks')
        return overall_clicks, unique_clicks


def is_bitlink(token, long_url):
    url = 'https://clc.li/api/urls'
    headers = {
        'Authorization': token,
        'Content-Type': 'application/json'
    }
    params = {
        'limit': '2',
        'page': '1',
        'order': 'date',
        'q': long_url
    }
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    answer = response.json()
    response_data = answer.get('data')
    urls = response_data.get('urls')
    return urls[0].get('longurl') == long_url


def main():
    load_dotenv()
    token = os.environ['CLC_API_TOKEN']
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
