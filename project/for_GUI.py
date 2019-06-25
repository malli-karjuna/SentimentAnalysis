from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import real_time_processing as rt
import json
consumer_key="mByIO5OAkU6Gm9LO56fu9jeS8"
consumer_secret="YUr2qAQbPUHliNEadFm85Llp6xiSzjFZR9VkFleYmCw64noZd1"
access_token="989446264281616384-glTetE8r7cIoPFykS6CLs5BNDhjIzqM"
access_token_secret="qRFcRFJDlWw4zlttZLv5tGFdvsitrGFJFFgIJ34Z1g4AM"


class TwitterListener(StreamListener):
    def __init__(self, file_name):
        self.file_name = file_name

    def on_data(self, data):
        try:
            all_data = json.loads(data)
            tweet = all_data['text']
            rt.processing(tweet)
            with open(self.file_name, 'a') as f:
                f.write(tweet)
            return True
        except BaseException as e:
            print("error on_data: %s" % str(e))
        return True

    def on_error(self, status):
        if status == 420:
            return False
        print(status)


def stream_tweets(tag_list, file_name):
    l = TwitterListener(file_name)
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)
    stream.filter(track=tag_list, languages=["en"])


if __name__ == "__main__":
    stream_tweets("python", "textt.csv")
