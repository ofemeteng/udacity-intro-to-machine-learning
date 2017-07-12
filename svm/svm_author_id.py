#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
clf = SVC(kernel='rbf', C=10000.0)

# features_train = features_train[:len(features_train)/100]
# labels_train = labels_train[:len(labels_train)/100]

t0 = time()
clf.fit(features_train, labels_train)
print "training time:", round(time()-t0, 3), "s"

t1 = time()
pred = clf.predict(features_test)
print "predicting time:", round(time()-t1, 3), "s"

# first = pred[10]
# second = pred[26]
# third = pred[50]

chris_total_email = 0
for value in pred:
	if value == 1:
		chris_total_email += 1


# print('Prediction\n 10th: {}, 26th: {}, 50th: {}'.format(first, second, third))
print('Total of Chris email: {}' .format(chris_total_email))

accuracy = accuracy_score(labels_test, pred)

print('Accuracy: {}'.format(accuracy))

#########################################################


