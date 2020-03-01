import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)
import pandas as pd 
import numpy as np 
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer, TfidfTransformer
from sklearn.svm import SVC,LinearSVC ,NuSVC
from sklearn.linear_model import LogisticRegression,SGDClassifier
from sklearn import metrics
from sklearn import svm
import pickle
import matplotlib.pyplot as plt
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

MNB_clf= MultinomialNB().fit(X_train, y_train)
'''
with open('nbmodel.pkl','wb') as f:
    pickle.dump((tfidf_transformer,count_vect,MNB_clf),f)
'''


lreg_clf=LogisticRegression(solver='lbfgs',multi_class='multinomial').fit(X_train,y_train)
'''
with open('lgmodel.pkl','wb') as f:
    pickle.dump((tfidf_transformer,count_vect,MNB_clf),f)
'''
SGD_clf=SGDClassifier(alpha=1e-3).fit(X_train,y_train)
'''
with open('sgdmodel.pkl','wb') as f:
    pickle.dump((tfidf_transformer,count_vect,MNB_clf),f)
'''
SVC_clf=SVC(gamma='scale').fit(X_train,y_train)
'''
with open('svcmodel.pkl','wb') as f:
    pickle.dump((tfidf_transformer,count_vect,MNB_clf),f)
'''
lSVC_clf=LinearSVC().fit(X_train,y_train)
'''
with open('lsvcmodel.pkl','wb') as f:
    pickle.dump((tfidf_transformer,count_vect,MNB_clf),f)
'''
NuSVC_clf=NuSVC(nu=0.15).fit(X_train,y_train)
'''
with open('nsvcmodel.pkl','wb') as f:
    pickle.dump((tfidf_transformer,count_vect,MNB_clf),f)
'''

MNB_pred = MNB_clf.predict(X_test)

lreg_pred=lreg_clf.predict(X_test)

SGD_pred=SGD_clf.predict(X_test)

SVC_pred=SVC_clf.predict(X_test)

lSVC_pred=lSVC_clf.predict(X_test)

NuSVC_pred=NuSVC_clf.predict(X_test)

#print(metrics.classification_report(y_test, MNB_pred))
print(metrics.confusion_matrix(y_test, lreg_pred))


print(metrics.confusion_matrix(y_test, lreg_pred))


print(metrics.confusion_matrix(y_test, SGD_pred))

print("multi nomial navie bayes accuracy")

print(np.mean(MNB_pred == y_test))
print("logistic regression accuracy")

print(np.mean(lreg_pred == y_test))
print("SGD accuracy")

print(np.mean(SGD_pred == y_test))
print("Linear svc accuracy")

print(np.mean(lSVC_pred == y_test))
print("NuSVC accuracy")


print(np.mean(NuSVC_pred == y_test))
print("svc accuracy")

print(np.mean(SVC_pred == y_test))
#----
'''
with open('nbmodel.pkl','rb') as f:
    tfidf_transfomer,count_vect,MNB_clf=pickle.load(f)
'''
new=pd.read_csv('cleanedtweets.csv')
new.dropna(inplace=True)
train_count1= count_vect.transform(new['tweets'])
train_tf1 = tfidf_transformer.transform(train_count1)
#print(train_tf1.shape)
l_reg=lreg_clf.predict(train_tf1)
navie_bayes=MNB_clf.predict(train_tf1)
sgd=SGD_clf.predict(train_tf1)
svc=SVC_clf.predict(train_tf1)
lsvc=lSVC_clf.predict(train_tf1)
nsvc=NuSVC_clf.predict(train_tf1)
new['l_reg']=l_reg
new['navie_bayes']=navie_bayes
new['sgd']=sgd
new['svc']=svc
new['lsvc']=lsvc
new['nsvc']=nsvc
new.to_csv("new.csv")
