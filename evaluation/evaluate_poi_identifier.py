#!/usr/bin/python


"""
    Starter code for the evaluation mini-project.
    Start by copying your trained/tested POI identifier from
    that which you built in the validation mini-project.

    This is the second step toward building your POI identifier!

    Start by loading/formatting the data...
"""

import pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r") )

### add more features to features_list!
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)



### your code goes here 
print "Number of features: %f" %len(features)

from sklearn import cross_validation  
features_train, features_test, labels_train, labels_test = cross_validation.train_test_split(features, labels, test_size=0.3, random_state=42)
print "Number of test features: %f" %len(features_test)


from sklearn import tree
from sklearn.metrics import accuracy_score

clf = tree.DecisionTreeClassifier()
clf = clf.fit(features_train, labels_train)
prediction = clf.predict(features_test)
print accuracy_score(prediction, labels_test)

from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix

print classification_report(labels_test, prediction)
print confusion_matrix(labels_test, prediction)