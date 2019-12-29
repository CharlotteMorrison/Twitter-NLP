import tweepy as tw
from keys import get_keys
import time


class Tweets:

    def __init__(self):
        self.consumer_key, self.consumer_secret, self.access_key, self.access_secret = get_keys()
        self.auth = tw.OAuthHandler(self.consumer_key, self.consumer_secret)
        self.auth.set_access_token(self.access_key, self.access_secret)
        self.api = tw.API(self.auth)

    def get_user_tweets(self, username, number_of_tweets=200):
        tweets = self.api.user_timeline(screen_name=username, count=number_of_tweets)
        return tweets

    def get_hashtag_tweets(self, tags, start_date='2019-1-1', num=100, filt='n'):
        if filt == 'y':
            tags = tags + " -filter:retweets"
        tweets = tw.Cursor(self.api.search,
                           q=tags,
                           lang='en',
                           since=start_date).items(num)
        return tweets

    def get_followers(self, user_name):
        followers = []
        for page in tw.Cursor(self.api.followers, screen_name=user_name, wait_on_rate_limit=True, count=200).pages():
            try:
                followers.extend(page)
            except tw.TweepError as e:
                print('waiting... ', e)
                time.sleep(60)
        return followers

    # main account tools
    def send_tweet(self, message):
        self.api.update_status(message)

    def get_friends(self):
        friends = tw.Cursor(self.api.friends).items()
        return friends

    def get_home_timeline(self, num=200):
        timeline = tw.Cursor(self.api.home_timeline).items(num)
        return timeline

    def send_dm(self, recipient, message):
        user = self.api.get_user(recipient)
        user_id = user.id
        self.api.send_direct_message(user_id, message)

