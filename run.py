import os
from dotenv import load_dotenv
load_dotenv()

from auth import OAuth2Handler
from twitter import Twitter

def run():
    # Just for testing
    api_key = os.getenv('CONSUMER_KEY')
    api_secret_key = os.getenv('CONSUMER_SECRET_KEY')

    auth = OAuth2Handler(api_key, api_secret_key)
    api = Twitter(auth)

    # Get users/lookup
    # print(api.getUsersInfo(screen_name=[""]))

    # Get users timeline
    # print(api.getUserTimeline(''))

    # Get followers/list and followers/ids
    # print(api.getUserFollowers(screen_name="", return_type="object"))

    # Get friends/ids and friends/list
    # print(api.getUsersFriends(screen_name=""))

if __name__ == "__main__":
    run()
