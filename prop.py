# Python program to convert
# JSON file to CSV

import json
import csv
import PySimpleGUI as sg

def findLastIndex(str, x):
    index = -1
    for i in range(0, len(str)):
        if str[i] == x:
            index = i
    return index

file_list = sg.popup_get_file('Select or write the path of the file you wish to convert')
x = "/"
str = file_list
ind = findLastIndex(str, x)
new_str = file_list[(ind+1):]
print(new_str)
with open(new_str) as json_file:
    data = json.load(json_file)

employee_data = data['emp_detail']

# now we will open a file for writing
data_file = open('data_file.csv', 'w')

# create the csv writer object
csv_writer = csv.writer(data_file)

# Counter variable used for writing
# headers to the CSV file
count = 0

for emp in employee_data:
    if count == 0:

        # Writing headers of CSV file
        header = emp.keys()
        csv_writer.writerow(header)
        count += 1

    # Writing data of CSV file
    csv_writer.writerow(emp.values())

data_file.close()
