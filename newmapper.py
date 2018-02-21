#!/usr/bin/python

from twitter import *
from datetime import datetime
import sys
import csv
import pandas as pd
import json
reload(sys)
sys.setdefaultencoding('utf-8')
def Main():
  read_data_from_json()
  tweetrate()
  realtionship_between_twousers()
  timeline()
  retweets()
def read_data_from_json():
  tweets_data = []
  for line in sys.stdin:  
    try:
        tweet = json.loads(line)
        tweets_data.append(tweet)
    except:
        continue
  tweets = pd.DataFrame()
  tweets['text'] = [tweet.get('text','') for tweet in tweets_data]
  tweets['lang'] = [tweet.get('lang','') for tweet in tweets_data]
  tweets['country'] = [tweet.get('country','') for tweet in tweets_data]
  for i in tweets['text']:
    print("{0}\t{1}".format("Finding0###",i))
  for i in tweets['lang']:
    print("{0}\t{1}".format("Finding1###",i))
  for i in tweets['country']:
    print("{0}\t{1}".format("Finding2###",i))

def tweetrate():
  created_at_format = '%a %b %d %H:%M:%S +0000 %Y'
  config = {}
  execfile("config.py", config)
  twitter = Twitter(auth = OAuth(config["atoken"], config["asecret"],
         config["ckey"], config["csecret"]))
  
  terms = "pink elephants"
  query = twitter.search.tweets(q = terms)
  results = query["statuses"]
  first_timestamp = datetime.strptime(results[0]["created_at"], created_at_format)
  last_timestamp = datetime.strptime(results[-1]["created_at"], created_at_format)
  mean = (first_timestamp - last_timestamp).total_seconds()
  length = len(results)
     #print("{0}\t{1}".format("firsttimestamp",first_timestamp))
  print("{0}\t{1}".format("Finding7###",mean))
  print("{0}\t{1}".format("Finding7###",len(results)))


def  realtionship_between_twousers():
  config = {}
  execfile("config.py", config)
  twitter = Twitter(auth = OAuth(config["atoken"], config["asecret"], config["ckey"], config["csecret"]))
  source = "modi"
  target = "nstomar"
  result = twitter.friendships.show(source_screen_name = source,target_screen_name = target)
  following = result["relationship"]["target"]["following"]
  follows   = result["relationship"]["target"]["followed_by"]
  print("{0}\t{1}".format("Finding8###",source))
  print("{0}\t{1}".format("Finding8###",target))
  print("{0}\t{1}".format("Finding8###",follows))
  print("{0}\t{1}".format("Finding8###",following))
  

def timeline():
  config = {}
  execfile("config.py", config)
  twitter = Twitter(auth = OAuth(config["atoken"], config["asecret"], config["ckey"], config["csecret"]))
  user = "modi"
  results = twitter.statuses.user_timeline(screen_name = user)
    #print("{0}\t{1}".format("finding8###result",results))
  for status in results:
    data = (status["created_at"], status["text"])
        #print data
    print("{0}\t{1}".format("Finding9###",data))

def retweets():
  user = "jaspritb1"
  config = {}
  execfile("config.py", config)
  twitter = Twitter(auth = OAuth(config["atoken"], config["asecret"], config["ckey"], config["csecret"]))
  results = twitter.statuses.user_timeline(screen_name = user)
  for status in results:
    retweets = twitter.statuses.retweets._id(_id = status["id"])
    for retweet in retweets:
      print("{0}\t{1}".format("Finding10###",(retweet["user"]["screen_name"])))

Main()
