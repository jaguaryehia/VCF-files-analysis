# import numpy as np
#
# newdata = np.random.random((50, 4))
# np.savetxt('newdata.csv', newdata, fmt="%.2f", delimiter=",", header='H1,H2,H3,H4')
# read = np.loadtxt('newdata.csv', delimiter=",")
# print(read[:4,:])

# import pickle
#
# order = {"first": 1, "second": 2, "third": 3, "fourth": 4, "fifth": 5}
# pickle.dump(order, open('new.pkl', "wb"))
# pick = pickle.load(open('new.pkl', "rb"))
# print(pick)

import json

college = {"college": "Engineering College",
           "objectives": "Mastering Electrical and Computer Engineering",
           "department": {
               "dep1": "Electrical",
               "dep2": "Computer"
           },
           "years": ["year1", "year2", "year3", "year4"],
           "number": [1, 2, 3, 4],
           "ID": [10, 20, 30, 40]
}
json.dump(college,open("college.json","w"))
new_college = json.load(open("college.json","r"))
print(new_college)