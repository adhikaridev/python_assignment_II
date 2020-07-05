# 4. Create a list. Append the names of your colleagues and friends to it.
# Has the id of the list changed? Sort the list. What is the first item on
# the list? What is the second item on the list?

list1 = []
print("Initial id of list: ", id(list1))
while True:
    friend_name = input("Enter your friend's name. Enter 0 when done: ")
    if friend_name == "0":
        break
    else:
        list1.append(friend_name)
        print("Appended list: ", list1)
        print("Id of the list: ", id(list1))
print("Sorted list: ", sorted(list1))
