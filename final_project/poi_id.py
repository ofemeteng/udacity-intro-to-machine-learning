#!/usr/bin/python
from __future__ import division
import sys
import pickle
import numpy as np
sys.path.append("../tools/")

from feature_format import featureFormat, targetFeatureSplit
from tester import dump_classifier_and_data

### Task 1: Select what features you'll use.
### features_list is a list of strings, each of which is a feature name.
### The first feature must be "poi".
features_list = ['poi','salary','deferral_payments','total_payments','exercised_stock_options','shared_receipt_with_poi','bonus','expenses','long_term_incentive',
	'total_stock_value'
]
# features_list with my generated features: bonus_salary_ratio, total_stock_total_payment_ratio
# features_list = ['poi','deferral_payments','exercised_stock_options','shared_receipt_with_poi','expenses','long_term_incentive','bonus_salary_ratio',
# 	'total_stock_total_payment_ratio'
# ] #You will need to use more features

### Load the dictionary containing the dataset
with open("final_project_dataset.pkl", "r") as data_file:
    data_dict = pickle.load(data_file)

# data exploration
print('There are {} data points'.format(len(data_dict)))
print('First 5 data points')
for i, record in enumerate(data_dict):
	print(record)
	print(data_dict[record])
	if i == 4:
		break

# number of POI
num_of_poi = 1
for name, record in data_dict.items():
	if record['poi'] == 1:
		num_of_poi += 1
print('There are {} POI in the dataset'.format(num_of_poi))

### Task 2: Remove outliers
data_dict.pop('TOTAL')
### Task 3: Create new feature(s)
from sklearn.preprocessing import MinMaxScaler
min_max_scaler = MinMaxScaler(feature_range=(0, 1))

bonus = []
salary = []
total_stock_value = []
total_payments = []
for name, record in data_dict.items():
	if record['bonus'] == 'NaN' or record['salary'] =='NaN' or record['total_stock_value'] == 'NaN' or record['total_payments'] == 'NaN':
		bonus.append(0.)
		salary.append(0.)
		total_stock_value.append(0.)
		total_payments.append(0.)

	else:
		bonus.append(record['bonus'])
		salary.append(record['salary'])
		total_stock_value.append(record['total_stock_value'])
		total_payments.append(record['total_payments'])

bonus = np.array(bonus).reshape((-1, 1))
salary = np.array(salary).reshape((-1, 1))
total_stock_value = np.array(total_stock_value).reshape((-1, 1))
total_payments = np.array(total_payments).reshape((-1, 1))

bonus_minmax = min_max_scaler.fit_transform(bonus)
salary_minmax = min_max_scaler.fit_transform(salary)
total_stock_value_minmax = min_max_scaler.fit_transform(total_stock_value)
total_payments_minmax = min_max_scaler.fit_transform(total_payments)

j = 0
for name, record in data_dict.items():
	if bonus_minmax[j][0] == 0. or salary_minmax[j][0] == 0. or total_stock_value_minmax[j][0] == 0. or total_payments_minmax[j][0] == 0.:
		record['bonus_salary_ratio'] = 0.
		record['total_stock_total_payment_ratio'] = 0.
	else:
		record['bonus_salary_ratio'] = bonus_minmax[j][0] / salary_minmax[j][0]
		record['total_stock_total_payment_ratio'] = total_stock_value_minmax[j][0] / total_payments_minmax[j][0]
	j += 1

### Store to my_dataset for easy export below.
my_dataset = data_dict

### Extract features and labels from dataset for local testing
data = featureFormat(my_dataset, features_list, sort_keys = True)
labels, features = targetFeatureSplit(data)

### Task 4: Try a varity of classifiers
### Please name your classifier clf for easy export below.
### Note that if you want to do PCA or other multi-stage operations,
### you'll need to use Pipelines. For more info:
### http://scikit-learn.org/stable/modules/pipeline.html

# Provided to give you a starting point. Try a variety of classifiers.
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import RandomForestClassifier

from sklearn.pipeline import Pipeline
from sklearn.decomposition import PCA

# clf = SVC()
# clf = DecisionTreeClassifier()
# clf = RandomForestClassifier()
# clf = GaussianNB()
# clf = LogisticRegression()
# clf = KNeighborsClassifier()


clf = AdaBoostClassifier(base_estimator=DecisionTreeClassifier(), n_estimators=50)
estimators = [('reduce_dim', PCA(n_components=5)), ('clf', clf)]
pipe = Pipeline(estimators)

### Task 5: Tune your classifier to achieve better than .3 precision and recall 
### using our testing script. Check the tester.py script in the final project
### folder for details on the evaluation method, especially the test_classifier
### function. Because of the small size of the dataset, the script uses
### stratified shuffle split cross validation. For more info: 
### http://scikit-learn.org/stable/modules/generated/sklearn.cross_validation.StratifiedShuffleSplit.html

# Example starting point. Try investigating other evaluation techniques!
from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = \
    train_test_split(features, labels, test_size=0.3, random_state=42)

# cross validation using KFold
# from sklearn.model_selection import KFold
# kf = KFold(n_splits=2)
# for train_index, test_index in kf.split(features):
# # 	print('TRAIN: ', train_index, 'TEST: ', test_index)
# 	features_train = []
# 	features_test = []
# 	labels_train = []
# 	labels_test = []

# 	for ii in train_index:
# 		features_train.append(features[ii])
# 		labels_train.append(labels[ii])
# 	for jj in test_index:
# 		features_test.append(features[jj])
# 		labels_test.append(labels[jj])

def fit_and_print_metrics(clf, features_train, features_test, labels_train, labels_test):
	from sklearn.metrics import accuracy_score, precision_score, recall_score
	clf.fit(features_train, labels_train)
	pred = clf.predict(features_test)
	accuracy = accuracy_score(labels_test, pred)
	precision = precision_score(labels_test, pred)
	recall = recall_score(labels_test, pred)
	print('Classifier: {}'.format(clf))
	print('The accuracy of model is: {}'.format(accuracy))
	print('The precision of model is: {}'.format(precision))
	print('The recall of model is: {}'.format(recall))
	print('')

fit_and_print_metrics(pipe, features_train, features_test, labels_train, labels_test)

### Task 6: Dump your classifier, dataset, and features_list so anyone can
### check your results. You do not need to change anything below, but make sure
### that the version of poi_id.py that you submit can be run on its own and
### generates the necessary .pkl files for validating your results.

dump_classifier_and_data(clf, my_dataset, features_list)