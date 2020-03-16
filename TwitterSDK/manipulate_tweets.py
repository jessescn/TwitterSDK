from .utils import createQuery, handleShouldBeList

class ManipulateTweets():

    def __init__(self, session, api_url):
        self.session = session
        self.api_url = api_url
        
    # GET statuses/user_timeline
    def getUserTimeline(self, **kwargs):
        """
        Get the last user timelines tweets 
        """

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
        uri = self.api_url + '/statuses/user_timeline.json'

        response = self.session.get(uri + query).json()
        return response

    # GET statuses/home_timeline
    def getHomeTimeline(self, **kwargs):
        """
        Returns the most recents tweets and retweets posted by the authenticating user 
        """

        params = {
            'count': kwargs.get('count'),
            'since_id': kwargs.get('since_id'),
            'max_id': kwargs.get('max_id'),
            'trim_user': kwargs.get('trim_user'),
            'exclude_replies': kwargs.get('exclude_replies'),
            'include_entities': kwargs.get('include_entities')
        }

        uri = self.api_url + '/statuses/home_timeline.json'
        query = createQuery(params)

        response = self.session.get(uri + query).json()
        return response

    # GET statuses/mentions_timeline 
    def getMentionsTimeline(self, **kwargs):
        """
        Returns the most recents mentions of the authenticating user
        """

        params = {
            'count': kwargs.get('count'),
            'since_id': kwargs.get('since_id'),
            'max_id': kwargs.get('max_id'),
            'trim_user': kwargs.get('trim_user'),
            'include_entities': kwargs.get('include_entities')
        }

        uri = self.api_url + '/statuses/mentions_timeline.json'
        query = createQuery(params)

        response = self.session.get(uri + query).json()
        return response
        
    # GET favorites/list 
    def getFavorites(self, **kwargs):
        """
        Returns the most recent favorites (likes) of the authenticating or especified user
        """

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

        response = self.session.get(uri + query).json()
        return response