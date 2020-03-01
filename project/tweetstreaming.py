from tweepy import API
from tweepy import Cursor
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from textblob import TextBlob
import pandas as pd
import numpy as np
import json
import re
consumer_key="########################################"
consumer_secret="##########################################"
access_token="###################################################"
access_token_secret="############################################"

class TwitterClient():
    def __init__(self, twitter_user=None):
        self.auth = TwitterAuthenticator().authenticate_Twitter()
        self.twitter_client = API(self.auth)
        self.twitter_user = twitter_user

    def get_twitter_client_api(self):
        return self.twitter_client
    
class TwitterAuthenticator():

    def authenticate_Twitter(self):
        auth = OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        return auth

class TwitterStreamer():

    def __init__(self):
        self.twitter_authenticator=TwitterAuthenticator()

    def Stream_tweets(self,fetched_tweets_filename,Tag_list):
        listener=TwitterListener(fetched_tweets_filename)
        auth = self.twitter_authenticator.authenticate_Twitter() 
        stream=Stream(auth,listener)
        stream.filter(track=tag_list,languages=["en"])
        

class TwitterListener(StreamListener):

    def __init__(self,fetched_tweets_filename):
        self.fetched_tweets_filename=fetched_tweets_filename
    
    def on_data(self,data):
        try:
            all_data=json.loads(data)
            tweets=all_data['text']
            '''
            with open(self.fetched_tweets_filename,'a') as tf:
                tf.write(data)
            '''
            return True
        except BaseException as e:
            print("error on_data: %s" % str(e))
        return True

    def on_error(self,status):
        if status == 420:
            return False
        
        print(Status)

class TweetAnalyzer():
    def clean_tweet(self, tweet):
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())

    def analyze_sentiment(self, tweet):
        analysis = TextBlob(self.clean_tweet(tweet))
        
        if analysis.sentiment.polarity > 0:
            return 1
        elif analysis.sentiment.polarity == 0:
            return 0
        else:
            return -1

    def tweets_to_data_frame(self, tweets):
        df = pd.DataFrame(data=[tweet.text for tweet in tweets], columns=['tweets'])

        df['id'] = np.array([tweet.id for tweet in tweets])
        df['len'] = np.array([len(tweet.text) for tweet in tweets])
        df['date'] = np.array([tweet.created_at for tweet in tweets])
        df['source'] = np.array([tweet.source for tweet in tweets])
        df['likes'] = np.array([tweet.favorite_count for tweet in tweets])
        df['retweets'] = np.array([tweet.retweet_count for tweet in tweets])

        return df
    
if __name__=="__main__":

    
    tag_list=["pixel 3"]
    fetched_tweets_filename="tweets1.txt"

    twitter_streamer=TwitterStreamer()
    tweets=twitter_streamer.Stream_tweets(fetched_tweets_filename,tag_list)
    print(tweets['text'])

    '''

    twitter_client = TwitterClient()
    tweet_analyzer = TweetAnalyzer()

    api = twitter_client.get_twitter_client_api()
    tweets = api.user_timeline(screen_name="realDonaldTrump", count=200)
    


    df = tweet_analyzer.tweets_to_data_frame(tweets)
    df['sentiment'] = np.array([tweet_analyzer.analyze_sentiment(tweet) for tweet in df['tweets']])

    print(df.head(10))
    '''



    








    
    
