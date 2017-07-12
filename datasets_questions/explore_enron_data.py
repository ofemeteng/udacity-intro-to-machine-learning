#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))
datapoints = len(enron_data)
features = enron_data['SKILLING JEFFREY K']
print('The number of data points (people) are: {}'.format(datapoints))
print('The number of features for each person is: {}'.format(len(features)))

def poi(data):
	num_of_poi = 0
	for name, record in data.items():
		if record['poi']==1:
			num_of_poi += 1
	return num_of_poi

jp_total_stock_value = enron_data['PRENTICE JAMES']['total_stock_value']
wc_to_poi_email = enron_data['COLWELL WESLEY']['from_this_person_to_poi']
jk_stock_options_exercised = enron_data['SKILLING JEFFREY K']['exercised_stock_options']

jk_total_payments = enron_data['SKILLING JEFFREY K']['total_payments']
kl_total_payments = enron_data['LAY KENNETH L']['total_payments']
af_total_payments = enron_data['FASTOW ANDREW S']['total_payments']

print('The number of persons of interest are: {}'.format(poi(enron_data)))
print('The total value of the stock belonging to James Prentice is: {}'.format(jp_total_stock_value))
print('The total email messages from Wesley Colwell to persons of interest is: {}'.format(wc_to_poi_email))
print('The value of stock options exercised by Jeffrey K Skilling is: {}'.format(jk_stock_options_exercised))

print('jk_total_payments: {}'.format(jk_total_payments))
print('kl_total_payments: {}'.format(kl_total_payments))
print('af_total_payments: {}'.format(af_total_payments))

def quantifiable(data):
	num_salary = 0
	num_email = 0
	for name, record in data.items():
		if record['salary'] != 'NaN':
			num_salary += 1
		if record['email_address'] != 'NaN':
			num_email += 1
	return dict(num_salary = num_salary, num_email = num_email)
salary, email = quantifiable(enron_data)['num_salary'], quantifiable(enron_data)['num_email']
print('Valid salary fields: {}, Valid email fields: {}'.format(salary, email))

def NaN_tp_percentage(data):
	no_tp = 0
	for name, record in data.items():
		if record['total_payments'] == 'NaN':
			no_tp += 1
	percentage = (no_tp  * 100)/datapoints
	return dict(no_tp = no_tp, percentage = percentage)
no_tp, percentage = NaN_tp_percentage(enron_data)['no_tp'], NaN_tp_percentage(enron_data)['percentage']
print('No total payments: {}, Percentage: {}'.format(no_tp, percentage))

def poi_no_total_payments(data):
	num_of_poi = 0
	for name, record in data.items():
		if record['poi'] == 1 and record['total_payments'] == 'NaN':
			num_of_poi += 1
			print(record['total_payments'])
	return num_of_poi

print('POI with no total payments: {}, Percentage: {}'.format(poi_no_total_payments(enron_data), (poi_no_total_payments(enron_data)  * 100)/18))
print(enron_data)
salary_list = []
for name, record in enron_data.items():
	salary_list.append(record['salary'])
salary_list = sorted(salary_list)
print('Sorted Salary List(ASC)')
print(salary_list)
bonus_list = []
for name, record in enron_data.items():
	bonus_list.append(record['bonus'])
bonus_list = sorted(bonus_list)
print('Sorted Bonus List(ASC)')
print(bonus_list)