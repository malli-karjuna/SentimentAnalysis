import pandas as pd 
import numpy as np 
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer, TfidfTransformer


df = pd.read_csv('trainset.csv')
df.dropna(inplace=True)
count_vect = CountVectorizer()
train_count = count_vect.fit_transform(df['tweets'])
print(train_count.shape)
'''
tf_transformer = TfidfTransformer(use_idf=False).fit(train_count)
train_tf = tf_transformer.transform(train_count)
print(train_tf.shape)
'''
tfidf_transformer = TfidfTransformer()
train_tfidf= tfidf_transformer.fit_transform(train_count)
print(train_tfidf.shape)
X =train_tfidf
y = df['sentiment']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20)
print(X_train.shape)
print(X_test.shape)
clf = MultinomialNB().fit(X_train, y_train)
pred = clf.predict(X_test)
from sklearn import metrics
print(metrics.classification_report(y_test, pred))
print(metrics.confusion_matrix(y_test, pred))
print(np.mean(pred == y_test))
new= pd.read_csv('cleanedtweets.csv')
new.dropna(inplace=True)
train_count1= count_vect.transform(new['tweets'])
train_tf1 = tfidf_transformer.transform(train_count1)
print(train_tf1.shape)
sentiment=clf.predict(train_tf1)
print(score(sentiment))
new['sentiment']=sentiment
new.to_csv("new.csv")
print("error")
    
