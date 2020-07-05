# 12. Create a function, is_palindrome, to determine if a supplied word is
# the same if the letters are reversed.

def is_palindrome(word):
    reverse = word[::-1]    # Slice that steps backwards by -1
    if word == reverse:
        return True
    else:
        return False

word = input("Enter a word: ")
bool1 = is_palindrome(word)
if bool1:
    print("The word '{}' is a palindrome.".format(word))
else:
    print("The word '{}' is not a palindrome.".format(word))
