import sys
import tweepy
import datetime
import signal
import json
import csv
import time

#Chunking module
class TweetSerializer:
   out = None
   out2 = None
   first = True
   count = 0

   def __init__(self, hashtag):
       self.hashtag = hashtag

   def start(self):
      self.count += 1
      fname = str(self.hashtag)+"-tweets-"+str(self.count)+".json"
      fname2 = str(self.hashtag)+"-tweetsText-"+str(self.count)+".txt"
      self.out = open(fname,"w")
      self.out2 = open(fname2, "w")
      self.out.write("[\n")
      self.out2.write("[\n")
      self.first = True

   def end(self):
      if self.out is not None:
         self.out.write("\n]\n")
         self.out.close()
         self.out2.write("\n]\n")
         self.out2.close()
      self.out = None
      self.out2 = None

   def write(self,tweet):
      if not self.first:
         self.out.write(",\n")
         self.out2.write(",\n")
      self.first = False
      self.out.write(json.dumps(tweet._json).encode('utf8'))
      self.out2.write(tweet.text.encode('utf8'))


consumer_key = "BPup9lE4iXfPOrkNJsisY4Su7"
consumer_secret = "NaI2hCC4sPgWdkbej0AAgmJxxhMiZtvfkTYfR1ZD0ymHLo5IZz"

access_token = "256653168-s3XsZYzoXQqbSMnTNdy6paVpnxvpm2PsebfHMvjz"
access_token_secret = "6xLv44LDDYuwDGP6ufBHPiTQKxBAYsvQI7QahPLRfDRFV"

#auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
#auth.set_access_token(access_token, access_token_secret)
auth = tweepy.AppAuthHandler(consumer_key, consumer_secret) #Using AppAuth
api = tweepy.API(auth_handler=auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)


def grabTweets(query, serializer):
    ts_1_count = 0
    ts_1_id = None
    searchCursor = tweepy.Cursor(api.search,q=query, since_id = ts_1_id, lang = "en").items()
    while True:
        try:
            tweet = searchCursor.next()
            ts_1_id = tweet.id
            if ts_1_count%1000 == 0:
                serializer.start()
            serializer.write(tweet)
            if ts_1_count%1000 == 999:
                serializer.end()
            ts_1_count += 1
        except tweepy.TweepError as e:
            print "TweepError found sleeping for 900 seconds"
            time.sleep(900)
            searchCursor = tweepy.Cursor(api.search, q1, since_id = ts_1_id, lang = "en").items()
            continue
        except StopIteration:
            break

q1 = "#NBAFinals2015 -#Warriors since:2015-06-13 until:2015-06-14"
q2 = "#Warriors -#NBAFinals2015 since:2015-06-13 until:2015-06-14"
q3 = "#NBAFinals2015 #Warriors since:2015-06-13 until:2015-06-14"

ts1 = TweetSerializer("#NBAFinals2015")
ts2 = TweetSerializer("#Warriors")
ts3 = TweetSerializer("#NBAFinals2015 #Warriors")


grabTweets(query = q1, serializer = ts1)
grabTweets(query = q2, serializer = ts2)
grabTweets(query = q3, serializer = ts3)
