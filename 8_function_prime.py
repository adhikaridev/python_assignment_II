# 8. Write a function, is_prime, that takes an integer and returns True if
# the number is prime and False if the number is not prime.

def is_prime(n):
    a = 0
    for x in range(2, n):
        if n%x == 0:
            a = 1
            break
    if a == 1:
        return False
    else:
        return True

n = int(input("Enter an integer: "))
bool1 = is_prime(n)
if bool1:
    print("{} is prime".format(n))
else:
    print("{} is not prime".format(n))
