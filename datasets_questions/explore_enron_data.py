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
import math

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))



#print (enron_data["SKILLING JEFFREY K"])
#print (enron_data["FASTOW ANDREW S"])
#print (enron_data["LAY KENNETH L"])
#print (len(enron_data["METTS MARK"]))
e = 0
s = 0
for u in enron_data:
	#print enron_data[u]["email_address"]
	if enron_data[u]["salary"]!='NaN':
		s = s+1

	if enron_data[u]["email_address"]!='NaN':
		e = e+1


print s
print e