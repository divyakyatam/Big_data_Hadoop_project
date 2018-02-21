#!/usr/bin/python
import json
import matplotlib.pyplot as plt
import operator
import sys
import pandas as pd
import re

def Main():
  data = read_mapper_output()
  number_Of_Tweets(data)
  top_five_langs(data)
  top_five_countries(data)
  specific_word(data)
  target_relevant_tweets(data)
  plt.show()


def read_mapper_output():
  data = []
  for line in sys.stdin:
    data.append(line)
  return data

def number_Of_Tweets(data):
  tweets = []
  for row in data:
    val = row.split("\t")
    if val[0] == 'Finding0###':
      tweets.append(val[1].strip('\n'))
  print("{0}\t{1}".format("Findingres0###",len(tweets)))


def top_five_langs(data):
  lang = []
  for row in data:
    val = row.split("\t")
    if val[0] == 'Finding1###':
      lang.append(val[1].strip('\n'))
  tweets = pd.DataFrame()
  tweets['lang'] = [tweet for tweet in lang]
  tweets_by_lang = tweets['lang'].value_counts()
  ##Plotting
  fig, ax = plt.subplots()
  ax.tick_params(axis='x', labelsize=15)
  ax.tick_params(axis='y', labelsize=10)
  ax.set_xlabel('Languages', fontsize=15)
  ax.set_ylabel('Number of tweets' , fontsize=15)
  ax.set_title('Top 5 languages', fontsize=15, fontweight='bold')
  tweets_by_lang[:5].plot(ax=ax, kind='bar', color='red')
  print("{0}\t{1}".format("Findingres1###",tweets_by_lang))



def top_five_countries(data):
  cont = []
  for row in data:
    val = row.split("\t")
    if val[0] == 'Finding2###':
      cont.append(val[1].strip('\n'))
  tweets = pd.DataFrame()
  tweets['country'] = [tweet for tweet in cont]
  tweets_by_country = tweets['country'].value_counts()
##plotting
  fig, ax = plt.subplots()
  ax.tick_params(axis='x', labelsize=15)
  ax.tick_params(axis='y', labelsize=10)
  ax.set_xlabel('Countries', fontsize=15)
  ax.set_ylabel('Number of tweets' , fontsize=15)
  ax.set_title('Top 5 countries', fontsize=15, fontweight='bold')
  tweets_by_country[:5].plot(ax=ax, kind='bar', color='blue')
  print("{0}\t{1}".format("Findingres2###",tweets_by_country))


prg_langs = ['India', 'NarenderModi', 'People']
def specific_word(data):
  tweet = []
  for row in data:
    val = row.split("\t")
    if val[0] == 'Finding0###':
      tweet.append(val[1].strip('\n'))
  tweets = pd.DataFrame()
  tweets['text'] = [tweet for tweet in tweet]
  tweets['India'] = tweets['text'].apply(lambda tweet: word_in_text('india', tweet))
  tweets['NarenderModi'] = tweets['text'].apply(lambda tweet: word_in_text('modi', tweet))
  tweets['People'] = tweets['text'].apply(lambda tweet: word_in_text('people', tweet))

  print("{0}\t{1}".format("Findingres3###",tweets['India'].value_counts()[True]))
  print("{0}\t{1}".format("Findingres3###",tweets['NarenderModi'].value_counts()[True]))
  print("{0}\t{1}".format("Findingres3###",tweets['People'].value_counts()[True]))

#  prg_langs = ['India', 'NarenderModi', 'People']
  tweets_by_prg_lang = [tweets['India'].value_counts()[True], tweets['NarenderModi'].value_counts()[True], tweets['People'].value_counts()[True]]
  x_pos = list(range(len(prg_langs)))
  width = 0.8
  fig, ax = plt.subplots()
  plt.bar(x_pos, tweets_by_prg_lang, width, alpha=1, color='g')

  # Setting axis labels and ticks
  ax.set_ylabel('Number of tweets', fontsize=15)
  ax.set_title('Number of tweets by specific words like India,NarenderModi,People', fontsize=10, fontweight='bold')
  ax.set_xticks([p + 0.4 * width for p in x_pos])
  ax.set_xticklabels(prg_langs)
  plt.grid()

def word_in_text(word, text):
    word = word.lower()
    text = text.lower()
    match = re.search(word, text)
    if match:
        return True
    return False



def target_relevant_tweets(data):
  tweet = []
  for row in data:
    val = row.split("\t")
    if val[0] == 'Finding0###':
      tweet.append(val[1].strip('\n'))
  tweets = pd.DataFrame()
  tweets['text'] = [tweet for tweet in tweet]
  tweets['NarenderModi'] = tweets['text'].apply(lambda tweet: word_in_text('usa', tweet))
  tweets['BarackObama'] = tweets['text'].apply(lambda tweet: word_in_text('india', tweet))
  tweets['DonaldTrump'] = tweets['text'].apply(lambda tweet: word_in_text('people', tweet))
  tweets['relevant'] = tweets['text'].apply(lambda tweet: word_in_text('usa', tweet) or word_in_text('india', tweet))

  print("{0}\t{1}".format("Findingres4###",tweets['NarenderModi'].value_counts()[True]))
  print("{0}\t{1}".format("Findingres4###",tweets['BarackObama'].value_counts()[True]))
  print("{0}\t{1}".format("Findingres4###",tweets['relevant'].value_counts()[True]))

  print("{0}\t{1}".format("Findingres4###",tweets[tweets['relevant'] == True]['NarenderModi'].value_counts()[True]))
  print("{0}\t{1}".format("Findingres4###",tweets[tweets['relevant'] == True]['BarackObama'].value_counts()[True]))
  print("{0}\t{1}".format("Findingres4###",tweets[tweets['relevant'] == True]['DonaldTrump'].value_counts()[True]))

  tweets_by_prg_lang = [tweets[tweets['relevant'] == True]['NarenderModi'].value_counts()[True],
                      tweets[tweets['relevant'] == True]['BarackObama'].value_counts()[True],
                      tweets[tweets['relevant'] == True]['DonaldTrump'].value_counts()[True]]
  x_pos = list(range(len(prg_langs)))
  width = 0.8
  fig, ax = plt.subplots()
  plt.bar(x_pos, tweets_by_prg_lang, width,alpha=1,color='g')
  ax.set_ylabel('Number of tweets', fontsize=15)
  ax.set_title('Ranking: MODI vs Obama vs Trump (Relevant data)', fontsize=10, fontweight='bold')
  ax.set_xticks([p + 0.4 * width for p in x_pos])
  ax.set_xticklabels(prg_langs)
  plt.grid()
  

  tweets['link'] = tweets['text'].apply(lambda tweet: extract_link(tweet))
  tweets_relevant = tweets[tweets['relevant'] == True]
  tweets_relevant_with_link = tweets_relevant[tweets_relevant['link'] != '']
  print("Number of Relevant tweets and links")
  print("{0}\t{1}".format("Findingres5###",tweets_relevant_with_link[tweets_relevant_with_link['NarenderModi'] == True]['link']))
  print("{0}\t{1}".format("Findingres5###",tweets_relevant_with_link[tweets_relevant_with_link['BarackObama'] == True]['link']))
  print("{0}\t{1}".format("Findingres5###",tweets_relevant_with_link[tweets_relevant_with_link['DonaldTrump'] == True]['link']))

"""Extracting links from tweets"""

def extract_link(text):
    regex = r'https?://[^\s<>"]+|www\.[^\s<>"]+'
    match = re.search(regex, text)
    if match:
        return match.group()
    return ''


Main()
