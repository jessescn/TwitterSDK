# Twitter SDK :bird:

**Work in Progress...**

SDK to provide an abstract and encapsulated way to comunicate and use Twitter API (in Python).

## Installation

This project is available via PyPi, you just need to run this command above

```
$ pip install twittersdk
```

## Setup

After installation, you can simply import in your Python project.

```python
from twittersdk import Twitter, OAuth2Handler

authenticator = OAuth2Handler(your_consumer_key, your_secret_consumer_key)
twitter = Twitter(authenticator)

```

After that, you can use all twitter API requests just calling `api` functions.

## functions

### GET statuses/user_timeline

Return informations about a specific user timeline tweets, searched by `screen_name` or `user_id`.

```javascript
twitter.getUserTimeline(self, screen_name, user_id, count=None, trim_user=None, exclude_replies=None, include_rts=None)
```

`count`, `trim_user`,`exclude_replies`,`include_rts` are optional arguments. You need to provide a valid `screen_name` or `user_id` to get filter a user timeline.

### GET users/lookup

Get informations about one or more users, searched by `user_id` or `screen_name` 

``` javascript
twitter.getUsersLookup(self, screen_name, user_id, include_entities=None, tweet_mode=None)
```

### GET followers/list and followers/ids

Return a list of user objects or ids representing the user that who follow a specific user. `screen_name` or `user_id` must be provide to search by one of this data, `return_type` is used to set if a return gonna be a list of ids (`search_type="ids`) or user objects(`search_type="list"`).    

```javascript
twitter.getUserFollowers(self, return_type, screen_name, user_id, cursor=-1, count=None, skip_status=False, include_user_entities=False)
```

### GET friends/list and friends/ids

Return a list of user objects or ids representing the user that who a specific user follow. `screen_name` or `user_id` must be provide to search by one of this data, `return_type` is used to set if a return gonna be a list of ids (`search_type="ids`) or user objects(`search_type="list"`).    

```javascript
twitter.getUsersFriends(self, return_type, screen_name, user_id, cursor=-1, count=20, stringify_ids=False)
```

