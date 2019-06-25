import pandas as pd 
import numpy as np 
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer, TfidfTransformer
from sklearn.model_selection import train_test_split
from sklearn import metrics
import pickle
class Navie_Bayes():
    def __init__(self,file_name1):
        self.file_name1=file_name1
        self.clasifier()

    def get_File(self,file_name1):
        df = pd.read_csv(file_name1)
        df.dropna(inplace=True)
        return df
    def new_file(self,file_name2):
        new=pd.read_csv(file_name2)
        new.dropna(inplace=True)
        return new
    def Vectorization(self,df):
        
        # create the transform
        count_vect = CountVectorizer()
        # tokenize and build vocab
        train_count = count_vect.fit_transform(df['tweets'])
        print(train_count.shape)
        return train_count
    def Tf_transformer(self,train_count):
        tf_transform = TfidfTransformer(use_idf=False).fit(train_count)
        train_tf = tf_transform.transform(train_count)
        print(train_tf.shape)
        return train_tf
    def clasifier(self):
        df=self.get_File(self.file_name1)
        train_count=self.Vectorization(df)
        train_tf=self.Tf_transformer(train_count)
        X = train_tf
        y = df['sentiment']
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20)
        self.clf = MultinomialNB().fit(X_train, y_train)
        pred = self.clf.predict(X_test)
        print(metrics.classification_report(y_test, pred))
        print(metrics.confusion_matrix(y_test, pred))
        print(np.mean(pred == y_test))
        '''

        save_classifier=open("naviebayes.pickle","wb")
        pickle.dump(self.clf,save_classifier)
        save_classifier.close()
        '''
    def classification(self,file_name2):
        self.file_name2=file_name2
        new=self.new_file(self.file_name2)
        train_count1=self.Vectorization(new)
        train_tf1=self.Tf_transformer(train_count1)
        '''
        # create the transform
        count_vect1 = CountVectorizer()
        # tokenize and build vocab
        train_count1 = count_vect.fit_transform(new['tweets'])
        print(train_count1.shape)
        tf_transformer1 = TfidfTransformer(use_idf=False).fit(train_count1)
        train_tf1 = tf_transformer.transform(train_count1)
        print(train_tf1.shape)
        '''
        sentiments = self.clf.predict(train_tf1)
        '''
        classifier_f=open("naviebayes.pickle","rb")
        classifier=pickle.load(classifier_f)
        classifier_f.close()
        sentiments=classifier.predict(train_tf1)
        '''
        new['sentiments'] = sentiments
        new.to_csv('new.csv')

if __name__=='__main__':
    file_name2='cleanedtweets.csv'
    file_name1='trainset.csv'
    nb=Navie_Bayes(file_name1)
    nb.classification(file_name2)
    

    


