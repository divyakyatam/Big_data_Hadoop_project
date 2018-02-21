from enchant.checker import SpellChecker
import json
import pandas as pd
import matplotlib.pyplot as plt
"""Reading the file"""
tweets_data_path = 'namo.json'

tweets_data = []
tweets_file = open(tweets_data_path, "r")
for line in tweets_file:
    try:
        tweet = json.loads(line)
        tweets_data.append(tweet)
    except:
        continue

"""Tweet data collection from json"""
tweets = pd.DataFrame()
tweets['text'] = [tweet.get('text','') for tweet in tweets_data]
for i in tweets['text']:
    text = i
    chkr = SpellChecker("en_US", text)
    for err in chkr:
        print(err.word + " at position " + str(err.wordpos))  #<----
        err.replace("SPAM")
    print("Text replaced by spam at  wrong spelling or words")
    t = chkr.get_text()
    print("\n" + t)  #<----
