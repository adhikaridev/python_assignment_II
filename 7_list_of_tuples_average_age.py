# 7. Create a list of tuples of first name, last name, and age for your
# friends and colleagues. If you don't know the age, put in None.
# Calculate the average age, skipping over any None values. Print out
# each name, followed by old or young if they are above or below the
# average age.

friends = []
print("Initial list: ", friends)
while True:
    print("Enter your friend's details. Enter 0 when you are done. Enter -1 if you don't know your friend's age.")
    f_name = input("First Name: ")
    l_name = input("Last Name: ")
    age = int(input("Age: "))
    if f_name == "0" or f_name == "0" or age == 0:
        break
    else:
        if age == -1:
            age = None
        tup1 = (f_name, l_name, age)
        friends.append(tup1)
        print("Appended list: ", friends)
sum = 0
for friend in friends:
    if friend[2] != None:
        sum += friend[2]
avg = sum/len(friends)
print("Average of ages: ", avg)
for friend in friends:
    if friend[2] <= avg:
        looks = "Young"
    else:
        looks = "Old"
    print("{} {}\t{}".format(friend[0], friend[1], looks))
