import base64
import os
import requests

class OAuth2Handler:

    api_url = "https://api.twitter.com/oauth2/token"

    def __init__(self, consumer_key, consumer_secret_key):
        self.consumer_key = consumer_key
        self.consumer_secret_key = consumer_secret_key
        credentials = '{}:{}'.format(self.consumer_key, self.consumer_secret_key).encode()
        self.credentialsEncoded = base64.b64encode(credentials).decode()
    
    def getToken(self):
        header = self.getHeaders()

        response = requests.post(self.api_url, headers=header, data='grant_type=client_credentials')
        status_code = response.status_code
        response = response.json()

        if status_code != 200:
            return

        return response['access_token']

    def getHeaders(self):
        header = {
        'Authorization': 'Basic {}'.format(self.credentialsEncoded),
        'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'
        }
        return header

