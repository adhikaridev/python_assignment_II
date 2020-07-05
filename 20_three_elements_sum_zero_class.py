# 20. Write a Python class to find the three elements that sum to zero
# from a list of n real numbers.
# Input array : [-25, -10, -7, -3, 2, 4, 8, 10]
# Output : [[-10, 2, 8], [-7, -3, 10]]

import itertools        # for generating combinations

class RealList:
    def __init__(self, list1):
        self.list1 = list1

    def sum_zero_combination(self):
        list2 = []
        combo = list(itertools.combinations(self.list1, 3))    # gives a list of three-element combinations in tuples
        for tupl in combo:
            if sum(tupl) == 0:
                list2.append(list(tupl))
        print(f"List of lists of three elements with sum zero: {list2}")


n = int(input("Enter number of items: "))
l = []
for x in range(n):
    l.append(int(input("Enter number: ")))
rl1 = RealList(l)
rl1.sum_zero_combination()
