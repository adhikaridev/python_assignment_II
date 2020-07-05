# 14. Write a function that reads a CSV file. It should return a list of
# dictionaries, using the first row as key names, and each subsequent
# row as values for those keys.
# For the data in the previous example it would return:
# [{'name': 'George', 'address': '4312 Abbey Road', 'age': 22}, {'name':
# 'John', 'address': '54 Love Ave', 'age': 21}]

import csv

def read_csv(file_name):
    file_name = file_name + ".csv"
    try:
        with open(file_name) as file_obj:
            reader = csv.reader(file_obj)
            header = next(reader)
            list_of_dict = []
            for row in reader:
                dict1 = {}
                for j, item in enumerate(header):
                    dict1[item] = row[j]
                list_of_dict.append(dict1)
            return list_of_dict
    except FileNotFoundError as e:
        exit("File not found.")


file_name = input("Enter file name without extension: ")
list_of_dict = read_csv(file_name)
print("List of dictionaries: ", list_of_dict)
