from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import real_time_processing as rt
import json
consumer_key="mByIO5OAkU6Gm9LO56fu9jeS8"
consumer_secret="YUr2qAQbPUHliNEadFm85Llp6xiSzjFZR9VkFleYmCw64noZd1"
access_token="989446264281616384-glTetE8r7cIoPFykS6CLs5BNDhjIzqM"
access_token_secret="qRFcRFJDlWw4zlttZLv5tGFdvsitrGFJFFgIJ34Z1g4AM"


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

