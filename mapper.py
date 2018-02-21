from twitter import *
from datetime import datetime
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

def main():
    tweetrate()
    realtonship_between_twousers()
    retweets()
    timeline()
#code for finding tweet rate
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
     print("{0}\t{1}".format("finding5###mean",mean))
     print("{0}\t{1}".format("finding5####length",len(results)))

####code for relationship between two users
def  realtonship_between_twousers():
     config = {}
     execfile("config.py", config)
     twitter = Twitter(auth = OAuth(config["atoken"], config["asecret"], config["ckey"], config["csecret"]))
     source = "modi"
     target = "nstomar"
     result = twitter.friendships.show(source_screen_name = source,target_screen_name = target)
     following = result["relationship"]["target"]["following"]
     follows   = result["relationship"]["target"]["followed_by"]
     print("{0}\t{1}".format("finding6###souce",source))
     print("{0}\t{1}".format("finding6###target",target))
     print("{0}\t{1}".format("finding6###follows",follows))
     print("{0}\t{1}".format("finding6###following",following))

#####code for finding retweets

def retweets():
     user = "jaspritb1"
     config = {}
     execfile("config.py", config)
     twitter = Twitter(auth = OAuth(config["atoken"], config["asecret"], config["ckey"], config["csecret"]))
     results = twitter.statuses.user_timeline(screen_name = user)
     for status in results:
        #print("{0}\t{1}".format("finding7###status",status["text"]))
        # print "Finding###status %s" % (status["text"])
         retweets = twitter.statuses.retweets._id(_id = status["id"])
         #count = 0;
         for retweet in retweets:
            #count += 1
            #print " - retweeted by %s" % (retweet["user"]["screen_name"])
            print("{0}\t{1}".format("finding7###status",(retweet["user"]["screen_name"])))


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
        print("{0}\t{1}".format("finding8###data",data))


main()
    
     

