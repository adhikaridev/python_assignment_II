# 5. Create a tuple with your first name, last name, and age. Create a list,
# people, and append your tuple to it. Make more tuples with the
# corresponding information from your friends and append them to the
# list. Sort the list. When you learn about sort method, you can use the
# key parameter to sort by any field in the tuple, first name, last name,
# or age.

get_third_item = lambda data: data[2]      #sorting according to the third item of tuple


tup1 = ('Dev', 'Adhikari', 26)
print("Initially, tuple: ", tup1)
people = []
print("Initially, list: ", people)
people.append(tup1)
print("List after appending tuple: ", people)

while True:
    friend_first_name = input("Enter your friend's first name. Enter 0 when done: ")
    friend_last_name = input("Enter your friend's last name. Enter 0 when done: ")
    friend_age = int(input("Enter your friend's age. Enter 0 when done: "))
    if friend_first_name == "0" or friend_last_name == "0" or friend_age == 0:
        break
    else:
        tup2 = (friend_first_name, friend_last_name, friend_age)
        people.append(tup2)
        print("List after appending friend: ", people)

people.sort(key=get_third_item)
print("Sorted list according to the third item of tuple: ", people)
