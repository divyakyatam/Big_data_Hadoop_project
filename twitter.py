import json
import pandas as pd
import matplotlib.pyplot as plt
"""Reading the file"""
tweets_data_path = 'twitter_data1.txt'

tweets_data = []
tweets_file = open(tweets_data_path, "r")
for line in tweets_file:
    try:
        tweet = json.loads(line)
        tweets_data.append(tweet)
    except:
        continue

"""Tweet data collection from json"""
print("Number of tweets")
print(len(tweets_data))
tweets = pd.DataFrame()
tweets['text'] = [tweet.get('text','') for tweet in tweets_data]#map(lambda tweet: tweet['text'], tweets_data)
tweets['lang'] = [tweet.get('lang','') for tweet in tweets_data]#map(lambda tweet: tweet['lang'], tweets_data)
tweets['country'] = [tweet.get('country','') for tweet in tweets_data]#map(lambda tweet: tweet['place']['country'] if tweet['place'] != None else None, tweets_data)

"""Top 5 Languages"""
tweets_by_lang = tweets['lang'].value_counts()

fig, ax = plt.subplots()
ax.tick_params(axis='x', labelsize=15)
ax.tick_params(axis='y', labelsize=10)
ax.set_xlabel('Languages', fontsize=15)
ax.set_ylabel('Number of tweets' , fontsize=15)
ax.set_title('Top 5 languages', fontsize=15, fontweight='bold')
tweets_by_lang[:5].plot(ax=ax, kind='bar', color='red')

"""Top 5 Countries"""
tweets_by_country = tweets['country'].value_counts()
print(len(tweets_by_country))
fig, ax = plt.subplots()
ax.tick_params(axis='x', labelsize=15)
ax.tick_params(axis='y', labelsize=10)
ax.set_xlabel('Countries', fontsize=15)
ax.set_ylabel('Number of tweets' , fontsize=15)
ax.set_title('Top 5 countries', fontsize=15, fontweight='bold')
tweets_by_country[:5].plot(ax=ax, kind='bar', color='blue')

plt.show()
