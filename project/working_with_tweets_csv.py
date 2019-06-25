import pandas as pd
import numpy as np
import re
import nltk
from textblob import TextBlob
from textblob import Word
from nltk.corpus import stopwords
from nltk.stem.porter import *
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from sklearn.feature_extraction.text import TfidfVectorizer

class Pre_Processing():
    def __init__(self,file_name):
        self.file_name=file_name
        self.cleaned_tweets_to_csv(self.file_name)

    def get_File(self,file_name):
        train=pd.read_csv(file_name)
        return train
        
    def preprocessing(self,file_name):
        train=self.get_File(file_name)
        train['word_count']=train['tweets'].apply(lambda x: len(str(x).split(" ")))
        train['char_count']=train['tweets'].str.len()
        train['avg_word']=train['tweets'].apply(lambda x: self.avg_word(x))
        train['tweets']=train['tweets'].apply(lambda x:self.clean_tweet(x))
        train['tweets']=train['tweets'].apply(lambda x:" ".join(x.lower() for x in x.split()))
        train['tweets']=train['tweets'].apply(lambda x: self.removing_rt(x))
        train['tweets'] = train['tweets'].str.replace('[^\w\s]','')
        stop = set(stopwords.words('english'))
        train['tweets'] = train['tweets'].apply(lambda x: " ".join(x for x in x.split() if x not in stop))
        stemmer=PorterStemmer()
        #train['tweets']=train['tweets'].apply(lambda x:word_tokenize(x))
        train['tweets']=train['tweets'].apply(lambda x:" ".join([stemmer.stem(i) for i in x.split()]))
        train['tweets'] = train['tweets'].apply(lambda x: " ".join([Word(word).lemmatize() for word in x.split()]))
        train.dropna(inplace=True)
        train['sentiment'] = train['tweets'].apply(lambda x: self.analyze_sentiment(x) )
        normal_words =' '.join([text for text in train['tweets'][train['sentiment'] == 0]])
        wordcloud = WordCloud(width=800, height=500, random_state=21, max_font_size=110).generate(normal_words)
        plt.figure(figsize=(10, 7))
        plt.imshow(wordcloud, interpolation="bilinear")
        plt.axis('off')
        plt.show()

        negative_words = ' '.join([text for text in train['tweets'][train['sentiment'] == -1]])

        wordcloud = WordCloud(width=800, height=500,
        random_state=21, max_font_size=110).generate(negative_words)
        plt.figure(figsize=(10, 7))
        plt.imshow(wordcloud, interpolation="bilinear")
        plt.axis('off')
        plt.show()
    
        return train

    def avg_word(self,sentence):
        words=sentence.split()
        return (sum(len(word) for word in words)/len(words))
 
    def clean_tweet(self,tweet):
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())

    def removing_rt(self,tweet):
        return re.sub(r'(^rt)',r'',tweet)

    def analyze_sentiment(self,tweet):
        analysis=TextBlob(tweet).sentiment[0]
        
        if analysis > 0:
            return 1
        elif analysis==0:
            return 0
        else:
            return -1

    def cleaned_tweets_to_csv(self,file_name):
        train=self.preprocessing(file_name)
        train.to_csv("trainset.csv")







if __name__=='__main__':

    file_name="tweets_from_df.csv"
    pp=Pre_Processing(file_name)
    
    
