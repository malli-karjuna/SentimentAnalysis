from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import real_time_processing as rt
import json
consumer_key="##################################"
consumer_secret="################################################"
access_token="####################################################"
access_token_secret="#############################################"


class StdOutListener(StreamListener):

    def on_data(self, data):
        all_data=json.loads(data)
        tweet=all_data['text']
        x = rt.processing(tweet)
        return True
    def on_error(self, status):
        print(status)


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['python'],languages=["en"])

