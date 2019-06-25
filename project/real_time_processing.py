import re
import pandas as pd
import numpy as np
import nltk
from textblob import TextBlob
from textblob import Word

def processing(tweet):
    tweet=" ".join(tweet.lower() for tweet in tweet.split())
    tweet=' '.join(re.sub("(@[\w]*)", " ", tweet).split())
    #print(tweet)
    ht=hashtag_extract(tweet)
    ht=sum(ht,[])
    #print(ht)
    sentiment=analyze_sentiment(tweet)
    #print("sentiment:",sentiment)
    return tweet,ht,sentiment
def hashtag_extract(x):
    hashtags = []
    for i in x.split():
        ht = re.findall(r'#(\w+)', i)
        hashtags.append(ht)

    return hashtags

def analyze_sentiment(tweet):
        analysis=TextBlob(tweet).sentiment[0]
        
        if analysis > 0:
            return 1
        elif analysis==0:
            return 0
        else:
            return -1
        
        return analysis
