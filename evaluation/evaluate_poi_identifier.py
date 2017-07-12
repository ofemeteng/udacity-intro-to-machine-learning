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
from sklearn.metrics import accuracy_score, precision_score, recall_score
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=0.3, random_state=42)

clf = DecisionTreeClassifier()
clf.fit(features_train, labels_train)
pred = clf.predict(features_test)
print('POIs Prediction')
print(pred)
print('Total number of people in test set: {}'.format(len(features_test)))
biased_pred = [0. for i in range(29)]
accuracy = accuracy_score(labels_test, pred)
print('Accuracy: {}'.format(accuracy))
print('Biased Accuracy: {}'.format(accuracy_score(labels_test, biased_pred)))

# true positive for test set
tp = 0
for predicted, actual in zip(pred, labels_test):
	if predicted == actual and actual == 1.0:
		tp += 1
print('True positives: {}'.format(tp))

precision = precision_score(labels_test, pred)
print('Precision score: {}'.format(precision))

recall = recall_score(labels_test, pred)
print('Recall score: {}'.format(recall))

#quiz
predictions = [0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1]
true_labels = [0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0]

zipped_labels = zip(predictions, true_labels)
tp = 0
for predicted, actual in zipped_labels:
	if predicted == actual and actual == 1:
		tp += 1
print('True positives: {}'.format(tp))

tn = 0
for predicted, actual in zipped_labels:
	if predicted == actual and actual == 0:
		tn += 1
print('True negatives: {}'.format(tn))

fp = 0
for predicted, actual in zipped_labels:
	if predicted == 1 and actual == 0:
		fp += 1
print('False positives: {}'.format(fp))

fn = 0
for predicted, actual in zipped_labels:
	if predicted == 0 and actual == 1:
		fn += 1
print('False negatives: {}'.format(fn))

print('Precision of quiz classifier: {}'.format(precision_score(true_labels, predictions)))
print('Recall of quiz classifier: {}'.format(recall_score(true_labels, predictions)))


