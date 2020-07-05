# 3. Write code that will print out the anagrams (words that use the same
# letters) from a paragraph of text.

# An anagram of a string is another string that contains same characters, only the order of characters can be different. For example, “abcd” and “dabc” are anagram of each other

import re                       # re (regular expression) is for getting a list of words from a sentence
from itertools import islice    # islice is for iterating dictionary from a specific idex


str1 = input("Enter a paragraph of text: ")
# str1 = "abcd silent listen a is \"bca\" dacb how are you?"
print("Original Paragraph: ", str1)
list1 = re.findall(r'\w+', str1)
dict1 = {}
for element in list1:
    dict1[element] = ''.join(sorted(element))
print("Anagrams: ")
j = 0
for key1, value1 in dict1.items():
    list2 = [key1]
    for key2, value2 in islice(dict1.items(), j+1, None):
        if value1 == value2:
            list2.append(key2)
    if len(list2) >= 2:
        print(list2)
    j = j + 1
