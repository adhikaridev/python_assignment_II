# 13. Write a function to write a comma-separated value (CSV) file. It
# should accept a filename and a list of tuples as parameters. The
# tuples should have a name, address, and age. The file should create
# a header row followed by a row for each tuple. If the following list of
# tuples was passed in:
# [('George', '4312 Abbey Road', 22), ('John', '54 Love Ave', 21)]
# it should write the following in the file:
# name,address,age
# George,4312 Abbey Road,22
# John,54 Love Ave,21

import csv

def write_csv(file_name, list_of_tuples):
    file_name = file_name + ".csv"
    with open(file_name, 'w') as file_obj:
        writer = csv.writer(file_obj)       # writer object is created using csv.writer()
        writer.writerow(["name", "address", "age"])
        for tupl in list_of_tuples:
            name, address, age = tupl       # tuple unpacking
            writer.writerow([name, address, age])


file_name = input("Enter a file name without extension: ")
list_of_tuples = []
n = int(input("Enter the number of people you want to add to the list: "))
for x in range(n):
    print("Enter details of person {}:".format(x+1))
    p_name = input("Enter name: ")
    p_address = input("Enter address: ")
    p_age = int(input("Enter age: "))
    list_of_tuples.append((p_name, p_address, p_age))
write_csv(file_name, list_of_tuples)
