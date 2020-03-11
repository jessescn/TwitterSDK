import requests
from .utils import createQuery

class ManipulateTweets():

    def __init__(self, token, header, api_url):
        self.token = token
        self.header = header
        self.api_url = api_url
        
    # GET statuses/user_timeline
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

