from .utils import getAuthHeaders
from .manage_users import ManageUsers
from .manipulate_tweets import ManipulateTweets

class Twitter:
    
    api_url = "https://api.twitter.com/1.1"

    def __init__(self, auth):
        token = auth.getToken()
        header = getAuthHeaders(token)
        self.manageUsers = ManageUsers(token, header, self.api_url)
        self.manipulateTweets = ManipulateTweets(token, header, self.api_url)

    def getUserTimeline(self, screen_name=None, user_id=None, count=None, trim_user=None, exclude_replies=None, include_rts=None):
        """
        GET statuses/user_timeline
        """
        return self.manipulateTweets.getUserTimeline(screen_name=None, user_id=None, count=None, trim_user=None, exclude_replies=None, include_rts=None)

    def getUsersLookup(self, screen_name=None, user_id=None, include_entities=None, tweet_mode=None):
        """
        GET users/lookup
        """
        return self.manageUsers.getUsersLookup(screen_name=screen_name, user_id=user_id, include_entities=include_entities, tweet_mode=tweet_mode)

    def getUserFollowers(self, return_type, screen_name=None, user_id=None, cursor=-1, count=None, skip_status=False, include_user_entities=False):
        """
        GET Followers/ids and GET followers/list
        """
        return self.manageUsers.getFollowers(screen_name=None, user_id=None, cursor=-1, count=None, skip_status=False, include_user_entities=False)
 
    def getUsersFriends(self, return_type, screen_name=None, user_id=None, cursor=-1, count=20, stringify_ids=False):
        """
        GET friends/ids and GET friends/list
        """
        return self.manageUsers.getFriends(return_type, screen_name=None, user_id=None, cursor=-1, count=20, stringify_ids=False)