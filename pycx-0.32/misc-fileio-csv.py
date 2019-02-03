# Simple file I/O in Python for CSV files
#
# Copyright 2013 Hiroki Sayama
# sayama@binghamton.edu

import csv

data = [["Hello", "World"], [1,2,3], ["The", "last", "row"]]


# writing to file

f = open("myfile.csv", "wb")
fcsv = csv.writer(f)

for row in data:
    fcsv.writerow(row)

f.close()

# reading from file

f = open("myfile.csv", "rb")
fcsv = csv.reader(f)

for row in fcsv:
    print row

f.close()
