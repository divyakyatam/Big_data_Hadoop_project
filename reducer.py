import operator
import sys
import pandas as pd
from twitter import *
from datetime import datetime

def Main():
      data = read_mapper_output()
      print(data)
      tweetrate(data)
      relationship_between_two_users(data)
      time = timeline(data)
      print(data)
      #retweet = 
      retweets(data)
      #retweeter_id(retweet)
def read_mapper_output():
      data = []
      for line in sys.stdin:
        line.split("\t")
        data.append(line)
      return data
def tweetrate(data):
    mean = data[0].split("\t")
    length = data[1].split("\t")
    m = float(mean[1])
    length1 = float(length[1])
    print "finding5###tweet rate ::",m/length1

def relationship_between_two_users(data):
    source = data[2].split("\t")
    target = data[3].split("\t")
    follows = data[4].split("\t")
    following = data[5].split("\t")
    print "finding6#### %s following %s: %s" % (source[1], target[1], follows[1])
    print "finding6#### %s following %s: %s" % (target[1], source[1], following[1])

def timeline(data):
    results = data[6].split("\t")
    results.append(data[7].strip("\t"))
    results.append(data[8].split("\t"))
    results.append(data[9].split("\t"))
    results.append(data[10].split("\t"))
    results.append(data[11].split("\t"))
    results.append(data[12].split("\t"))
    print results
    print "ended"

def retweets(data):
    print "hello"
    tweet = data[15].split("\t")
    print tweet
Main()
    
#def retweeter_id(retweet):
 #    retweets = twitter.statuses.retweets._id(_id = status["id"])
     #count = 0;
  #   for retweet in retweets:
        #count += 1
   #     print " - retweeted by %s" % (retweet["user"]["screen_name"])


