### code to save tweets in json###
import sys
import tweepy
import json

access_key = "934902398-uJ7g8VFm249EpjHZrhRpTtKeH8DAFX4uLAFNzBV5"
access_secret = "Po6mBech7v07mNqHrDtFmE68x09LKtwLmM56D9K0K3c8D"
consumer_key = "uXn1P4xkJKcpu3hLRGtD0qfAA"
consumer_secret = "qO2v6tR3kU2U9NTjnAETNTfx4j23GgM0JNYNi76DZJXnqR6oBn"


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)
file = open('today.txt', 'a')

tweets=[]

save_file = open('raw_tweets.json', 'a')

class CustomStreamListener(tweepy.StreamListener):
    def __init__(self, api):
        self.api = api
        super(tweepy.StreamListener, self).__init__()
        self.save_file = tweets

    def on_data(self, tweet):
        self.save_file.append(json.loads(tweet))
        print tweet
        save_file.write(str(tweet))

    def on_status(self, status):
        print status.text

    # def on_data(self, data):
    #     json_data = json.loads(data)
    #     file.write(str(json_data))

    def on_error(self, status_code):
        print >> sys.stderr, 'Encountered error with status code:', status_code
        return True # Don't kill the stream

    def on_timeout(self):
        print >> sys.stderr, 'Timeout...'
        return True # Don't kill the stream

sapi = tweepy.streaming.Stream(auth, CustomStreamListener(tweepy.StreamListener))
sapi.filter(track=['Hilary', '#USelection2016', 'US', 'election'])