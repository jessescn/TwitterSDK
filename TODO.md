### Follow, search and get users

List of methods in this [Twitter API session page](https://developer.twitter.com/en/docs/accounts-and-users/follow-search-get-users/api-reference/get-users-lookup).

* [x] GET friends/ids
* [x] GET friends/list
* [x] GET followers/ids
* [x] GET followers/list
* [ ] GET friendships/incoming (user context only)
* [ ] GET friendships/lookup (user context only)
* [ ] GET friendships/no_retweets/ids (user context only)
* [ ] GET friendships/outgoing (user context only)
* [ ] GET friendships/show (user context only)
* [x] GET users/lookup
* [ ] GET users/search (user context only)
* [x] GET users/show
* [ ] POST friendships/create (user context only)
* [ ] POST friendships/destroy (user context only)
* [ ] POST friendships/update (user context only)

* (user context only) - Only available using user Third-Party Auth

### Tweets

List of methods in this [Twitter API session page](https://developer.twitter.com/en/docs/tweets/timelines/overview).

- Tweets
* [x] GET statuses/user_timeline
* [ ] GET statuses/home_timeline
* [ ] GET statuses/mentions_timeline
* [ ] POST statuses/update]
* [ ] POST statuses/destroy/:id
* [ ] GET statuses/show/:id
* [ ] GET statuses/oembed
* [ ] GET statuses/lookup

- Retweets
* [ ] POST statuses/retweet/:id
* [ ] POST statueses/unretweet/:id
* [ ] GET statuses/retweets/:id
* [ ] GET statuses/retweets_of_me
* [ ] GET statuses/retweets/ids

- Likes (formely favorites)
* [ ] POST favorites/create/:id
* [ ] POST favorites/destroy/:id
* [x] GET favorites/list