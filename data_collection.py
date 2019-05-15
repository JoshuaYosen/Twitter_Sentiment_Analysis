import tweepy as tw
import pandas as pd
import twitter_credentials

# authentication for twitter api access
auth = tw.OAuthHandler(twitter_credentials.CONSUMER_KEY, twitter_credentials.CONSUMER_SECRET)
auth.set_access_token(twitter_credentials.ACCESS_TOKEN, twitter_credentials.ACCESS_TOKEN_SECRET)

# instantiate twitter api
api = tw.API(auth, wait_on_rate_limit=True)


search_words = '#apple'
filtered_search = search_words + " -filter:retweets"
date_since = '2019-04-20'

# requests tweets from twitter api
tweets = tw.Cursor(api.search,
                   q=filtered_search,
                   lang="en",
                   since=date_since).items(10000)

# defines tweets into text file
tweet_data = [tweet.text for tweet in tweets]
# creates pandas dataframe of tweet.txt
twitter_df = pd.DataFrame(data=tweet_data,
                          columns=['tweet_data'])
print(twitter_df.head(20))

# outputs twitter_data into a csv file
twitter_df.to_csv(r'/home/rhulain/Desktop/Python Projects/Twitter_Sent_Analysis/sent_analysis.py/tweets.csv', index=None, header=True)
