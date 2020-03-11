import requests
from TwitterSDK.utils import getAuthHeaders, createQuery

class Twitter:
    
    api_url = "https://api.twitter.com/1.1"

    def __init__(self, auth):
        self.token = auth.getToken()
        self.header = getAuthHeaders(self.token)

    def getUserTimeline(self, **kwargs):
        """
        Get the last user timelines tweets 
        """
        uri = self.api_url + "/statuses/user_timeline.json?"

        screen_name = kwargs.get('screen_name', None)
        user_id = kwargs.get('user_id', None)

        if not screen_name and not user_id:
            return {}

        params = {
            'screen_name': screen_name,
            'user_id': user_id,
            'count': kwargs.get('count', None),
            'trim_user': kwargs.get('trim_user', None),
            'exclude_replies': kwargs.get('exclude_replies', None),
            'include_rts': kwargs.get('include_rts', None)
        }

        query = createQuery(params)

        response = requests.get(uri + query, headers=self.header).json()
        return response

    def getUsersInfo(self, **kwargs):
        """
        Get info about one or more users by screen_name or user_id
        """
        uri = self.api_url + "/users/lookup.json?"

        screen_name = kwargs.get('screen_name', None)
        user_id = kwargs.get('user_id', None)

        params = {
            'include_entities': kwargs.get('include_entities', None),
            'tweet_mode': kwargs.get('tweet_mode', None)
        }

        if screen_name:
            params['screen_name'] = ','.join(screen_name)

        if user_id:
            params['user_id'] = ','.join(str(uid) for uid in user_id)
        
        query = createQuery(params)

        response = requests.post(uri + query, headers=self.header).json()
        return response

    def getUserFollowers(self, **kwargs):
        """
        Get info about user followers
        """
        screen_name = kwargs.get('screen_name', None)
        user_id = kwargs.get('user_id', None)
        return_type = kwargs.get('return_type', "id")

        if not screen_name and not user_id:
            return {}
        
        params = {
            'screen_name': screen_name,
            'user_id': user_id,
            'cursor': kwargs.get('cursor', None),
            'count': kwargs.get('count', None),
            'skip_status': kwargs.get('skip_status', None),
            'include_user_entities': kwargs.get('include_user_entities', None)
        }

        uri = self.api_url + "/followers/"

        query = "ids.json?" if return_type == "id" else "list.json?"
        query += createQuery(params)

        response = requests.get(uri + query, headers=self.header).json()
        return response
 
    # Refact to recycle code
    def getUsersFriends(self, **kwargs):
        """
        Get info about specific user friends
        """
        screen_name = kwargs.get('screen_name', None)
        user_id = kwargs.get('user_id', None)
        return_type = kwargs.get('return_type', "id")

        if not screen_name and not user_id:
            return {}

        params = {
            'screen_name': screen_name,
            'user_id': user_id,
            'cursor': kwargs.get('cursor', None),
            'count': kwargs.get('count', None),
            'stringify_ids': kwargs.get('stringify_ids', None)
        }

        uri = self.api_url + "/friends/"

        query = "ids.json?" if return_type == "id" else "list.json?"
        query += createQuery(params)
    
        response = requests.get(uri + query, headers=self.header).json()
        return response