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

fig, ax = plt.subplots()
ax.tick_params(axis='x', labelsize=15)
ax.tick_params(axis='y', labelsize=10)
ax.set_xlabel('Countries', fontsize=15)
ax.set_ylabel('Number of tweets' , fontsize=15)
ax.set_title('Top 5 countries', fontsize=15, fontweight='bold')
tweets_by_country[:5].plot(ax=ax, kind='bar', color='blue')

"""Specific word identification"""
import re
def word_in_text(word, text):
    word = word.lower()
    text = text.lower()
    match = re.search(word, text)
    if match:
        return True
    return False
tweets['MODI'] = tweets['text'].apply(lambda tweet: word_in_text('india', tweet))
tweets['Obama'] = tweets['text'].apply(lambda tweet: word_in_text('modi', tweet))
tweets['Trump'] = tweets['text'].apply(lambda tweet: word_in_text('people', tweet))

print tweets['MODI'].value_counts()[True]
print tweets['Obama'].value_counts()[True]
print tweets['Trump'].value_counts()[True]

prg_langs = ['MODI', 'Obama', 'Trump']
tweets_by_prg_lang = [tweets['MODI'].value_counts()[True], tweets['Obama'].value_counts()[True], tweets['Trump'].value_counts()[True]]

x_pos = list(range(len(prg_langs)))
width = 0.8
fig, ax = plt.subplots()
plt.bar(x_pos, tweets_by_prg_lang, width, alpha=1, color='g')

# Setting axis labels and ticks
ax.set_ylabel('Number of tweets', fontsize=15)
ax.set_title('Number of tweets talking', fontsize=10, fontweight='bold')
ax.set_xticks([p + 0.4 * width for p in x_pos])
ax.set_xticklabels(prg_langs)
plt.grid()

"""Targetting relevant tweets"""
tweets['MODI'] = tweets['text'].apply(lambda tweet: word_in_text('usa', tweet))
tweets['Obama'] = tweets['text'].apply(lambda tweet: word_in_text('india', tweet))
tweets['relevant'] = tweets['text'].apply(lambda tweet: word_in_text('usa', tweet) or word_in_text('india', tweet))

print tweets['MODI'].value_counts()[True]
print tweets['Obama'].value_counts()[True]
print tweets['relevant'].value_counts()[True]

print tweets[tweets['relevant'] == True]['MODI'].value_counts()[True]
print tweets[tweets['relevant'] == True]['Obama'].value_counts()[True]
print tweets[tweets['relevant'] == True]['Trump'].value_counts()[True]

tweets_by_prg_lang = [tweets[tweets['relevant'] == True]['MODI'].value_counts()[True], 
                      tweets[tweets['relevant'] == True]['Obama'].value_counts()[True], 
                      tweets[tweets['relevant'] == True]['Trump'].value_counts()[True]]
x_pos = list(range(len(prg_langs)))
width = 0.8
fig, ax = plt.subplots()
plt.bar(x_pos, tweets_by_prg_lang, width,alpha=1,color='g')
ax.set_ylabel('Number of tweets', fontsize=15)
ax.set_title('Ranking: MODI vs Obama vs Trump (Relevant data)', fontsize=10, fontweight='bold')
ax.set_xticks([p + 0.4 * width for p in x_pos])
ax.set_xticklabels(prg_langs)
plt.grid()

"""Extracting links from tweets"""

def extract_link(text):
    regex = r'https?://[^\s<>"]+|www\.[^\s<>"]+'
    match = re.search(regex, text)
    if match:
        return match.group()
    return ''

tweets['link'] = tweets['text'].apply(lambda tweet: extract_link(tweet))
tweets_relevant = tweets[tweets['relevant'] == True]
tweets_relevant_with_link = tweets_relevant[tweets_relevant['link'] != '']

print tweets_relevant_with_link[tweets_relevant_with_link['MODI'] == True]['link']
print tweets_relevant_with_link[tweets_relevant_with_link['Obama'] == True]['link']
print tweets_relevant_with_link[tweets_relevant_with_link['Trump'] == True]['link']

plt.show()
