#!/usr/bin/python

import pickle
import numpy
numpy.random.seed(42)


### The words (features) and authors (labels), already largely processed.
### These files should have been created from the previous (Lesson 10)
### mini-project.
words_file = "../text_learning/your_word_data.pkl" 
authors_file = "../text_learning/your_email_authors.pkl"
word_data = pickle.load( open(words_file, "r"))
authors = pickle.load( open(authors_file, "r") )



### test_size is the percentage of events assigned to the test set (the
### remainder go into training)
### feature matrices changed to dense representations for compatibility with
### classifier functions in versions 0.15.2 and earlier
from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(word_data, authors, test_size=0.1, random_state=42)

from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer = TfidfVectorizer(sublinear_tf=True, max_df=0.5,
                             stop_words='english')
features_train = vectorizer.fit_transform(features_train)
features_test  = vectorizer.transform(features_test).toarray()


### a classic way to overfit is to use a small number
### of data points and a large number of features;
### train on only 150 events to put ourselves in this regime

features_train = features_train[:150].toarray()
labels_train   = labels_train[:150]
#features_train = features_train.toarray()
#labels_train   = labels_train


### your code goes here

#Quiz: Number Of Features And Overfitting
print "Number of features: %s" %len(features_train)

from sklearn.tree import DecisionTreeClassifier

clf = DecisionTreeClassifier(min_samples_split=40)
clf.fit(features_train, labels_train)

pred = clf.predict(features_test)


#Quiz: Accuracy Of Your Overfit Decision Tree
from sklearn.metrics import accuracy_score

print "Accuracy: %5.4f" %accuracy_score(labels_test, pred)

#Quiz: Identify The Most Powerful Features
#Quiz: Use TfIdf To Get The Most Important Word
importances = clf.feature_importances_
feature_num = 0

for importance in importances:
	if importance >= 0.2:
		print feature_num, importance, vectorizer.get_feature_names()[feature_num]

	feature_num += 1