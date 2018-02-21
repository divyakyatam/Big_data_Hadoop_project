#!/usr/bin/python

import sys
import csv
import pandas as pd
import json
reload(sys)
sys.setdefaultencoding('utf-8')
def Main():
  read_data_from_json()

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
  
Main()
