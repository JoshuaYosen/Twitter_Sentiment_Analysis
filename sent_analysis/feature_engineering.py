import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from data_cleaning_fun import *

#read csv to panda dataframe
PATH = '/home/rhulain/Desktop/Python_Projects/Twitter_Sent_Analysis/sent_analysis/tweets.csv'
tweets_df = pd.read_csv(PATH)

#instantiate vaderSentiment classifier
analyzer = SentimentIntensityAnalyzer()

#use vaderSentiment to label each tweet with the compound score
i = 0
scores = []
while (i<len(tweets_df)):
    k = analyzer.polarity_scores(tweets_df.iloc[i]['tweet_data'])
    scores.append(k['compound'])
    i += 1

#takes 'scores' array and creates a new column in tweets_df
scores = np.array(scores)
tweets_df['Score'] = scores
tweets_df.head(20)

#defines a function to normalize scores with values [-1, 0, 1]
def normalize_scores(s):
    if s < 0:
        s = -1
    elif s > 0:
        s = 1
    return s

#assigns each compound score to a normalized score
norm_scores = []
for i in range(len(tweets_df.Score - 1)):
    norm_scores.append(normalize_scores(tweets_df.Score[i]))
print(norm_scores)

#replaces old score values with normalized scores
tweets_df['Score'] = norm_scores

#assigns tweets to a series to clean and tokenize data
tweets = tweets_df.loc[:, 'tweet_data']
cleaned_tweets = normalize_corpus(tweets)

#create a new cleaned dataframe for export
cleaned_tweets_df = pd.DataFrame(cleaned_tweets, columns=['Tweets'])
cleaned_tweets_df['Labels'] = tweets_df['Score']
cleaned_tweets_df.head(20)

#export cleaned dataframe
cleaned_tweets_df.to_csv(r'sent_analysis/cleaned_tweets.csv', encoding='utf-8')
