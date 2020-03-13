import requests
from .utils import createQuery, handleShouldBeList

class ManageUsers():

    def __init__(self, header, api_url):
        self.header = header
        self.api_url = api_url

    # GET Followers/ids and GET followers/list
    def getFollowers(self, **kwargs):
        """
        Get info about user followers
        """
        screen_name = kwargs.get('screen_name', None)
        user_id = kwargs.get('user_id', None)
        return_type = kwargs.get('return_type', "id") # Could be 'id' or 'list'

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

        uri = self.api_url + '/followers/'

        query = "ids.json" if return_type == "id" else "list.json"
        query += createQuery(params)

        response = requests.get(uri + query, headers=self.header).json()
        return response
 
    # GET friends/ids and GET friends/list
    def getFriends(self, **kwargs):
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

        uri = self.api_url + '/friends/'

        query = "ids.json" if return_type == "id" else "list.json"
        query += createQuery(params)
    
        response = requests.get(uri + query, headers=self.header).json()
        return response

    # GET users/lookup
    def getUsersLookup(self, **kwargs):
        """
        Get info about one or more users by screen_name or user_id
        """
        screen_name = handleShouldBeList(kwargs.get('screen_name', None))
        user_id = handleShouldBeList(kwargs.get('user_id', None))

        params = {
            'include_entities': kwargs.get('include_entities', None),
            'tweet_mode': kwargs.get('tweet_mode', None)
        }

        if screen_name:
            params['screen_name'] = ','.join(screen_name)

        if user_id:
            params['user_id'] = ','.join(str(uid) for uid in user_id)
        
        query = createQuery(params)
        uri = self.api_url + '/users/lookup.json'

        response = requests.post(uri + query, headers=self.header).json()
        return response

    # GET users/show
    def getUserShow(self, **kwargs):
        """
        Get a lookup of a specific user 
        """
        screen_name = kwargs.get('screen_name')
        user_id = kwargs.get('user_id')
        include_entities = kwargs.get('include_entities')
        
        return self.getUsersLookup(screen_name=screen_name, user_id=user_id, include_entities=include_entities)

