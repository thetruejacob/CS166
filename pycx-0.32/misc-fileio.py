# Simple file I/O in Python
#
# Copyright 2008-2012 Hiroki Sayama
# sayama@binghamton.edu

# writing to file

f = open("myfile.txt", "w")

f.write("Hello\n")
f.write("This is a second line\n")
f.write("Bye\n")

f.close()

# reading from file

f = open("myfile.txt", "r")

for row in f:
    print row,
    # The last comma is to prevent automatic line break

f.close()
