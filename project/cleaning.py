import pandas as pd
import numpy as np
import nltk
import re
from nltk.tokenize import word_tokenize
from nltk.stem.porter import *
from nltk.corpus import stopwords
import csv

train=pd.read_csv("train_tweets.csv")
#print(train['tweets'].head(10))

train['tweets']=train['tweets'].apply(lambda x: ' '.join(re.sub("@[\w]*"," ",x).split()))
train['tweets']=train['tweets'].apply(lambda x:" ".join(x.lower() for x in x.split()))
train['tweets'] = train['tweets'].str.replace("[^a-zA-Z#]", " ")
train['tweets'] = train['tweets'].apply(lambda x: ' '.join([w for w in x.split() if len(w)>2]))
stop = set(stopwords.words('english'))
train['tweets'] = train['tweets'].apply(lambda x: " ".join(x for x in x.split() if x not in stop))
stemmer=PorterStemmer()
train['tweets']=train['tweets'].apply(lambda x:" ".join([stemmer.stem(i) for i in x.split()]))
#train['tweets'] = train['tweets'].apply(lambda x: " ".join([Word(word).lemmatize() for word in x.split()]))
train.dropna(inplace=True)

def hashtag_extract(x):
    hashtags = []
    # Loop over the words in the tweet
    for i in x:
        ht = re.findall(r"#(\w+)", i)
        hashtags.append(ht)

    return hashtags
HT=hashtag_extract(train['tweets'])
# extracting hashtags from non racist/sexist tweets

HT_regular = hashtag_extract(train['tweets'][train['sentiment'] >= 0])

# extracting hashtags from racist/sexist tweets
HT_negative = hashtag_extract(train['tweets'][train['sentiment'] == -1])

# unnesting list
HT=sum(HT,[])
HT_regular = sum(HT_regular,[])
HT_negative = sum(HT_negative,[])
h=nltk.FreqDist(HT)
h1=pd.DataFrame({'Hashtag': list(h.keys()),
                  'Count': list(h.values())})
a = nltk.FreqDist(HT_regular)
d = pd.DataFrame({'Hashtag': list(a.keys()),
                  'Count': list(a.values())})
b = nltk.FreqDist(HT_negative)
e = pd.DataFrame({'Hashtag': list(b.keys()), 'Count': list(b.values())})
print(h1.head(10))
h1.to_csv("hastags.csv")
#train['tweets']=train['tweets'].apply(lambda x:word_tokenize(x))


print(train['tweets'].head(10))
