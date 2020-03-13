import requests
from .utils import createQuery, handleShouldBeList

class ManipulateTweets():

    def __init__(self, header, api_url):
        self.header = header
        self.api_url = api_url
        
    # GET statuses/user_timeline
    def getUserTimeline(self, **kwargs):
        """
        Get the last user timelines tweets 
        """
        uri = self.api_url + '/statuses/user_timeline.json'

        screen_name = handleShouldBeList(kwargs.get('screen_name', None))
        user_id = handleShouldBeList(kwargs.get('user_id', None))

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


    def getFavorites(self, **kwargs):


        screen_name = kwargs.get('screen_name')
        user_id = kwargs.get('user_id')

        if not screen_name or user_id:
            return {}

        params = {
            'screen_name': screen_name,
            'user_id': user_id,
            'count': kwargs.get('count'),
            'since_id': kwargs.get('since_id'),
            'max_id': kwargs.get('max_id'),
            'include_entities': kwargs.get('include_entities')
        }

        uri = self.api_url + '/favorites/list.json'
        
        query = createQuery(params)

        response = requests.get(uri + query, headers=self.header).json()
        return response