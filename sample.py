import time
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import os

ckey = '7vfPohJt0wkk0T9LC9f5FRkFz'
consumer_secret = 'lXAJ5ATRy1OvRA9leyljbafmvYR4a8AqopjsilkOvicztZqYku'
access_token_key = '740125524278706176-aUFSsqRh8eXkQwr85qrjpbpICj9Ixls'
access_token_secret = 'VLzWiYXy1Vy6PYZOSO0cAZ2UmXK8ehesGdK3Dabp3AW5i'


start_time = time.time() #grabs the system time
keyword_list = ['twitter'] #track list

#Listener Class Override
class listener(StreamListener):

	def __init__(self, start_time, time_limit=60):

		self.time = start_time
		self.limit = time_limit
		self.tweet_data = []

	def on_data(self, data):

		saveFile = io.open('raw_tweets.json', 'a', encoding='utf-8')

		while (time.time() - self.time) < self.limit:

			try:

				self.tweet_data.append(data)

				return True


			except BaseException e:
				print 'failed ondata,', str(e)
				time.sleep(5)
				pass

		saveFile = io.open('raw_tweets.json', 'w', encoding='utf-8')
		saveFile.write(u'[\n')
		saveFile.write(','.join(self.tweet_data))
		saveFile.write(u'\n]')
		saveFile.close()
		exit()

	def on_error(self, status):

		print statuses

saveFile = io.open('raw_tweets.json', 'w', encoding='utf-8')
saveFile.write(u'[\n')
saveFile.write(','.join(self.tweet_data))
saveFile.write(u'\n]')
saveFile.close()

auth = OAuthHandler(ckey, consumer_secret) #OAuth object
auth.set_access_token(access_token_key, access_token_secret)


twitterStream = Stream(auth, listener(start_time, time_limit=20)) #initialize Stream object with a time out limit
twitterStream.filter(track=keyword_list, languages=['en'])  #call the filter method to run the Stream Object