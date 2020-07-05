# 9. Write a binary search function. It should take a sorted sequence and
# the item it is looking for. It should return the index of the item if found.
# It should return -1 if the item is not found.

def binary_search(seq, search_item, low, high):    #Here we are using recursion
    mid = int(low + (high - low) / 2)               # low, high and mid are indices
    mid_item = seq[mid]
    if high < low:                                  # high is less than low when the search item is not found
        return -1
    if search_item == mid_item:
        return mid
    else:
        if search_item < mid_item:
            high = mid - 1
            return binary_search(seq, search_item, low, high)
        if search_item > mid_item:
            low = mid + 1
            return binary_search(seq, search_item, low, high)


n = int(input("Enter the number of items in the list:"))
print("Enter integer items: ")
seq = []
for x in range(n):
    item = int(input())
    seq.append(item)
print("Entered list: ", seq)
search_item = int(input("Enter integer item to be searched in the list: "))
search_item_index = binary_search(seq, search_item, 0, len(seq) - 1)
print("Returned: ", search_item_index)
