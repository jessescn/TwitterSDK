import base64
import os
import requests

from requests_oauthlib import OAuth1Session

class Auth:

    def post(self, url, data=None, headers=None):
        pass

    def put(self, url, data=None, headers=None):
        pass

    def delete(self, url, headers=None):
        pass

    def get(self, url, headers=None):
        pass

class Oauth1Handler(Auth):

    def __init__(self, cred):
        self.session = OAuth1Session(cred.get('client_key'), cred.get('client_secret_key'), cred.get('access_token'), cred.get('access_token_secret'))

    def post(self, url, data=None, headers=None):
        return self.session.post(url, data=data, headers=headers)

    def put(self, url, data=None, headers=None):
        return self.session.put(url, data=data, headers=headers)

    def delete(self, url, headers=None):
        return self.session.delete(url, headers=headers)

    def get(self, url, headers=None):
        return self.session.get(url, headers=headers)


class OAuth2Handler(Auth):

    api_url = "https://api.twitter.com/oauth2/token"

    def __init__(self, consumer_key, consumer_secret_key):
        credentials = '{}:{}'.format(consumer_key, consumer_secret_key).encode()
        self.credentialsEncoded = base64.b64encode(credentials).decode()
        self.header = self.getAuthHeaders()

    def get(self, url):
        return requests.get(url, headers=self.header)

    def post(self, url, data=None):
        return requests.post(url, data=data, headers=self.header)

    def put(self, url, data=None):
        return requests.put(url, data=data, headers=self.header)

    def delete(self, url):
        return requests.delete(url, headers=self.header)

    def getAuthHeaders(self):
        """
        Receives a token and returns a header dict
        """
        token = self.getToken()
        if not token:
            return None

        header = {
            'authorization': 'Bearer ' + token
        }
        return header


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
