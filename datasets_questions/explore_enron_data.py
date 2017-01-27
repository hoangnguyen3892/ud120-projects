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

print "Number of people: {0}".format(len(enron_data))
#print enron_data.keys()
print "Number of features: {0}".format(len(enron_data['PAI LOU L']))
print enron_data['PAI LOU L']


# count poi
count = 0
for i in enron_data.keys():
	if enron_data[i]['poi'] == True:
		count += 1

print "POIs in data: {0}".format(count)

# count poi
count = 0
for i in enron_data.keys():
	if enron_data[i]['poi'] == True or enron_data[i]['poi'] == False:
		count += 1

print "POIs in data: {0}".format(count)

# count poi
poi_names = open("../final_project/poi_names.txt").read().split('\n')
poi_y = [name for name in poi_names if "(y)" in name]
poi_n = [name for name in poi_names if "(n)" in name]
print("poi_names_count:", len(poi_y) + len(poi_n))


# Quiz: Query The Dataset 1

print "Total value of the stock belonging to James Prentice: {0}".format(enron_data['PRENTICE JAMES']['total_stock_value'])

# Quiz: Query The Dataset 2

print "email messages from Wesley Colwell to persons of interest: {0}".format(enron_data['COLWELL WESLEY']['from_this_person_to_poi'])

# Quiz: Query The Dataset 2

print "Value of stock exercised by Jeffrey K Skilling: {0}".format(enron_data['SKILLING JEFFREY K']['exercised_stock_options'])

# CEO: Jeffrey skilling
# Chairman: Kenneth Lay
# CFO: Andrew Fastow

# Quiz: Follow the money

print "Total payment CEO: {0}".format(enron_data['SKILLING JEFFREY K']['total_payments'])
print "Total payment CFO: {0}".format(enron_data['FASTOW ANDREW S']['total_payments'])
print "Total payment chairman: {0}".format(enron_data['LAY KENNETH L']['total_payments'])

# Quiz Unfilled features

salary_count = 0
for i in enron_data.keys():
	if enron_data[i]['salary'] != 'NaN':
		salary_count += 1

print "Qualified salary: {0}".format(salary_count)

email_count = 0
for i in enron_data.keys():
	if enron_data[i]['email_address'] != 'NaN':
		email_count += 1

print "Known email: {0}".format(email_count)

# Quiz: Missing POIs 1
payment_count = 0
for i in enron_data.keys():
	if enron_data[i]['total_payments'] == 'NaN':
		payment_count += 1

print "Missing payment: {0}".format(payment_count)
total = len(enron_data.keys())
print total
print "Percentage of missing payment: {0}".format(payment_count*100.0/total)

# Quiz: Missing POIs 2
payment_poi_count = 0
for i in enron_data.keys():
	if enron_data[i]['total_payments'] == 'NaN' and enron_data[i]['poi'] == True:
		payment_poi_count += 1

print "Missing pois payment: {0}".format(payment_poi_count)
total = len(enron_data.keys())
print "Percentage of valid payment: {0}".format(payment_poi_count*100.0/total)