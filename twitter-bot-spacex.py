import tweepy
import time

CONSUMER_KEY = '<jiIB6rc9EygkRVS1HIAWjlA2B>'
CONSUMER_SECRET = '<MDiFHDwSYJswo30gLKAH19LfkWYwLFEKx0AKTYZ1wvWk57nYtH>'
ACCESS_KEY = '<2547591452-mGMwHVAppECW1XfxVKgWt0l7EzAiMljVO8UdiVj>'
ACCESS_SECRET = '<VVLc9OHpeQBlMRPP7PKxcijC1AQ6IwwKmsuzVRKPnGiCi>'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

#Create API object
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
user = api.me()
search = '#spaceX'
numTweet = 500
for tweet in tweepy.Cursor(api.search, search).items(numTweet):
    try:
        print('Tweets Liked')
        tweet.favorite()
        print("Retweet done")
        tweet.retweet()
        time.sleep(10)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break