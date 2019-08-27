#!/usr/bin/python3
"""Twitter app, so much fun yay!!!!"""
import requests
from sys import argv
import base64


def doit(apikey, secretkey, search):
    key = "{}:{}".format(apikey, secretkey).encode('ascii')
    key = base64.b64encode(key).decode('ascii')
    auth_headers = {
        'Authorization': 'Basic ' + key,
        'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'
    }
    auth_data = {
        'grant_type': 'client_credentials'
    }
    r = requests.post('https://api.twitter.com/oauth2/token',
                      headers=auth_headers, data=auth_data)
    token = r.json().get('access_token')

    search_headers = {
        'Authorization': 'Bearer ' + token
    }
    search_data = {
        'q': search,
        'result_type': 'recent',
        'count': 10
    }
    r = requests.get('https://api.twitter.com/1.1/search/tweets.json',
                     headers=search_headers, params=search_data)

    for tweet in r.json().get('statuses'):
        print("[{}] {} by {}".format(tweet.get('id'), tweet.get('text'),
                                     tweet.get('user').get('name')))
    return r

if __name__ == "__main__":
    doit(argv[1], argv[2], argv[3])
