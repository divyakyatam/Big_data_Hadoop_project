
from twitter import *

user = "iHrithik"

#-----------------------------------------------------------------------
# load our API credentials 
#-----------------------------------------------------------------------
config = {}
execfile("config.py", config)

#-----------------------------------------------------------------------
# create twitter API object
#-----------------------------------------------------------------------
twitter = Twitter(
		    auth = OAuth(config["atoken"], config["asecret"], config["ckey"], config["csecret"]))

#-----------------------------------------------------------------------
# perform a basic search 
# twitter API docs: https://dev.twitter.com/docs/api/1/get/search
#-----------------------------------------------------------------------
results = twitter.statuses.user_timeline(screen_name = user)

#-----------------------------------------------------------------------
# loop through each of my statuses, and print its content
#-----------------------------------------------------------------------
for status in results:
	print "@%s %s" % (user, status["text"])

	#-----------------------------------------------------------------------
	# do a new query: who has RT'd this tweet?
	#-----------------------------------------------------------------------
	retweets = twitter.statuses.retweets._id(_id = status["id"])
        #count = 0;
	for retweet in retweets:
            #count += 1
	    print " - retweeted by %s" % (retweet["user"]["screen_name"])
            #count += 1
           # print (count)
