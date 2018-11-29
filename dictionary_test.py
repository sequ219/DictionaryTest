"""
Sample dictionary init from CSV
in the simple case of the CSV being
exactly key-value pairs

"""
import os
import csv

my_dir = os.path.dirname(os.path.realpath(__file__))
filename = 'dictionary_test.csv'

my_dict = dict()

with open(my_dir+'/'+filename,'r')as f:

    csv_reader=csv.reader(f)
    for row in csv_reader:
        key=row[0]
        value=row[1]
        my_dict[key] = value

# print(read_data)


    print(my_dict)

# This should print out 'Joe'
# print(my_dict[1])
