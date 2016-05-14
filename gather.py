#!/usr/bin/env python

'''
current working one using tweepy
should fix timeout errors using rate-limt or timeout exceptions
'''

### code to save tweets in json###
import sys
import tweepy
import json, time
# from http.client import IncompleteRead   # For error handling, reconnect if error 

# to force utf-8 encoding on entire program
reload(sys)  
sys.setdefaultencoding('utf8')


access_key = "934902398-uJ7g8VFm249EpjHZrhRpTtKeH8DAFX4uLAFNzBV5"
access_secret = "Po6mBech7v07mNqHrDtFmE68x09LKtwLmM56D9K0K3c8D"
consumer_key = "uXn1P4xkJKcpu3hLRGtD0qfAA"
consumer_secret = "qO2v6tR3kU2U9NTjnAETNTfx4j23GgM0JNYNi76DZJXnqR6oBn"


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)
file = open('keywords.txt', 'r')
queries = file.readlines()
tweets= []


saveFile = open('tweets_stream.json', 'a')
saveFile.write('[')

class CustomStreamListener(tweepy.StreamListener):
    def __init__(self, api):
        self.api = api
        super(tweepy.StreamListener, self).__init__()
        self.saveFile = tweets

    def on_data(self, data):
        self.saveFile.append(json.loads(data))
        print "tracking tweets from twitter.."
        while True:
            try:
                tweet = json.loads(data)
                time = tweet['created_at']
                user_name = tweet['user']['name']
                user_location = tweet['user']['location']
                text = tweet['text']
                retweet = tweet['retweet_count']
                place = tweet['place']
                coord = tweet['coordinates']
                saveFile.write('{')
                saveFile.write('"timestamp":"' +time+'",')
                saveFile.write('"name":"' +user_name+'",')
                saveFile.write('"tweet":"' +text+'",')
                saveFile.write('"user_location":"' +str(user_location)+'",')
                saveFile.write('"place":"' +str(place)+'",')
                saveFile.write('"coordinates":"' +str(coord)+'",')
                saveFile.write('"re-tweet count":"' +str(retweet)+'"')
                saveFile.write('},')
                saveFile.write('\n')
                # saveFile.close()
                return True

            except BaseException, e:
                print 'failed ondata,', str(e)
                time.sleep(5)
                continue
        print "finished saving it in json file......"
        exit()


    def on_status(self, status):
        print status.text

    def on_error(self, status_code):
        print >> sys.stderr, 'Encountered error with status code:', status_code
        return True # error handling

    def on_timeout(self):
        print "timeout error...."
        print >> sys.stderr, 'Timeout...'
        return True  # Error handling
sapi = tweepy.streaming.Stream(auth, CustomStreamListener(tweepy.StreamListener))
sapi.filter(track=queries, languages=['en']);

# while True:
#     try: # error handling
#         sapi = tweepy.streaming.Stream(auth, CustomStreamListener(tweepy.StreamListener))
#         sapi.filter(track=queries, languages=['en']);

#     except:
#         # continue to try on error
#         print "Error Handled! Going to Sleep.."
#         time.sleep(5)
#         print "Run again.."
#         continue
saveFile.write(']')

# stream.Filter ( track = queries, locations = [-122.75,36.8,-121.75,37.8] )