import tweepy
from textblob import TextBlob

consumer_key = 'JOz5LW2o2G9tsxUlScQlgn2lK'
consumer_key_secret = 'pl1K79XkCe3DSbtsH41YiOVwFPgfWcrxIYnih1MyDCAjpTAfd3'
access_token = '728176699297378306-uBXtafmPf0bgbMCe2R0wZu1GjGEyUnr'
access_token_secret = 'e0cYDly2hVEd2LirWPZyC5esKWyueHOw1q2BBBOKMDJFE'
auth = tweepy.OAuthHandler(consumer_key, consumer_key_secret)

auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('disaster')

for tweet in public_tweets:
print(tweet.text)
analysis = TextBlob(tweet.text)
print(analysis.sentiment)
if analysis.sentiment[0]>0:
    print ('Positive')
else:
    print ('Negative')
print("")

