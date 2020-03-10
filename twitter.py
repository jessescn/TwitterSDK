import requests

class Twitter:

    api_url = "https://api.twitter.com/1.1"

    def __init__(self, auth):
        self.token = auth.getToken()
        self.header = self.getAuthHeaders()

    def getUserTimeline(self, userIdentifier, count=10, trim_user=False, exclude_replies=False, include_rts=True):
        query = self.api_url + "/statuses/user_timeline.json?screen_name={}&count={}&exclude_replies={}&include_rts={}&trim_user={}".format(
            userIdentifier, count, exclude_replies, include_rts, trim_user)

        response = requests.get(query, headers=self.header).json()
        return response

    def getUsersInfo(self, screen_name=[], user_id=[], include_entities=False, tweet_mode=False):
        query = self.api_url + "/users/lookup.json"
        if screen_name != []:
            query += "?screen_name={}".format(','.join(screen_name))

        if user_id != []:
            query += "?user_id={}".format(','.join(str(uid) for uid in user_id))
        
        query += '&include_entities={}&tweet_mode={}'.format(include_entities, tweet_mode)

        response = requests.post(query, headers=self.header).json()
        return response

    def getUserFollowers(self, screen_name="", user_id="", return_type="id", cursor="-1", count="20", skip_status=False, include_user_entities=True):
        if screen_name == "" and user_id == "":
            return {}
        query = self.api_url + "/followers/"

        returned_type = "ids.json?" if return_type == "id" else "list.json?"
        query += returned_type

        search_by = "screen_name={}".format(screen_name) if screen_name != "" else "?user_id={}".format(user_id)
        query += search_by

        query += "&cursor={}&count={}&skip_status={}&include_user_entities={}".format(cursor, count, skip_status, include_user_entities)

        response = requests.get(query, headers=self.header).json()
        return response
 
    # Refact to recycle code
    def getUsersFriends(self, screen_name="", user_id="", return_type="id", cursor="-1", stringify_ids=False, count=None):
        if screen_name == "" and user_id == "":
            return {}

        query = self.api_url + "/friends/"

        returned_type = "ids.json?" if return_type == "id" else "list.json?"
        query += returned_type

        search_by = "screen_name={}".format(screen_name) if screen_name != "" else "?user_id={}".format(user_id)
        query += search_by

        query += "&cursor={}&stringify_ids={}".format(cursor, stringify_ids)
        query += "&count={}".format(count) if count else ""

        response = requests.get(query, headers=self.header).json()
        return response

    def getAuthHeaders(self):
        header = {
            'authorization': 'Bearer ' + self.token
        }
        return header

    

    
