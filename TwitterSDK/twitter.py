from .utils import getAuthHeaders
from .manage_users import ManageUsers
from .manipulate_tweets import ManipulateTweets

class Twitter:
    
    api_url = "https://api.twitter.com/1.1"

    def __init__(self, session):
        self.manageUsers = ManageUsers(session, self.api_url)
        self.manipulateTweets = ManipulateTweets(session, self.api_url)

    def getUserTimeline(self, screen_name=None, user_id=None, count=None, trim_user=None, exclude_replies=None, include_rts=None):
        """
        GET statuses/user_timeline
        """
        return self.manipulateTweets.getUserTimeline(screen_name=screen_name, user_id=user_id, count=count, trim_user=trim_user, exclude_replies=exclude_replies, include_rts=include_rts)

    def getUserHomeTimeline(self, count=None, since_id=None, max_id=None, trim_user=None, exclude_replies=None, include_entities=None):
        """
        GET statuses/home_timeline
        """
        return self.manipulateTweets.getHomeTimeline(count=count, since_id=since_id, max_id=max_id, trim_user=trim_user, exclude_replies=exclude_replies, include_entities=include_entities)

    def getMentionsTimeline(self, count=None, since_id=None, max_id=None, trim_user=None, include_entities=None):
        """
        GET statuses/mentions_timeline
        """
        return self.manipulateTweets.getMentionsTimeline(count=count, since_id=since_id, max_id=max_id, trim_user=trim_user, include_entities=include_entities)

    def getUsersLookup(self, screen_name=None, user_id=None, include_entities=None, tweet_mode=None):
        """
        GET users/lookup
        """
        return self.manageUsers.getUsersLookup(screen_name=screen_name, user_id=user_id, include_entities=include_entities, tweet_mode=tweet_mode)

    def getUserShow(self, screen_name=None, user_id=None, include_entities=None):
        """
        GET users/show
        """
        return self.manageUsers.getUserShow(screen_name=screen_name, user_id=user_id, include_entities=include_entities)

    def getUserFollowers(self, return_type, screen_name=None, user_id=None, cursor=-1, count=None, skip_status=False, include_user_entities=False):
        """
        GET Followers/ids and GET followers/list
        """
        return self.manageUsers.getFollowers(return_type=return_type, screen_name=screen_name, user_id=user_id, cursor=cursor, count=count, skip_status=skip_status, include_user_entities=include_user_entities)
 
    def getUsersFriends(self, return_type, screen_name=None, user_id=None, cursor=-1, count=20, stringify_ids=False):
        """
        GET friends/ids and GET friends/list
        """
        return self.manageUsers.getFriends(return_type=return_type, screen_name=screen_name, user_id=user_id, cursor=cursor, count=count, stringify_ids=stringify_ids)

    def getFavorites(self, screen_name=None, user_id=None, count=20, since_id=None, max_id=None, include_entities=None):
        """
        GET favorites/list
        """
        return self.manipulateTweets.getFavorites(screen_name=screen_name, user_id=user_id, count=count, since_id=since_id, max_id=max_id, include_entities=include_entities)