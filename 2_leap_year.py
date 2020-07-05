# 2. Write an if statement to determine whether a variable holding a year
# is a leap year.

# Things to consider:
# 1. If a year is evenly divisible by 4 means having no remainder then go to next step. If it is not divisible by 4. It is not a leap year. For example: 1997 is not a leap year.
# 2. If a year is divisible by 4, but not by 100. For example: 2012, it is a leap year. If a year is divisible by both 4 and 100, go to next step.
# 3. If a year is divisible by 100, but not by 400. For example: 1900, then it is not a leap year. If a year is divisible by both, then it is a leap year. So 2000 is a leap year.


year1 = int(input("Enter a year: "))
if year1%4 == 0:
    if year1%100 == 0:
        if year1%400 == 0:
            print("{} is a leap year.".format(year1))
        else:
            print("{} is not a leap year.".format(year1))
    else:
        print("{} is a leap year.".format(year1))
else:
    print("{} is not a leap year.".format(year1))
