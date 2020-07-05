# 6. Create a list with the names of friends and colleagues. Search for the
# name ‘John’ using a for a loop. Print ‘not found’ if you didn't find it.

friends = []
print("Initial list: ", friends)
while True:
    friend_name = input("Enter your friend's name. Enter 0 when done: ")
    if friend_name == "0":
        break
    else:
        friends.append(friend_name)
        print("Appended list: ", friends)
f = False
for item in friends:
    if item == "John":
        f = True
        break
if f:
    print("Name found.")
else:
    print("Not found")
