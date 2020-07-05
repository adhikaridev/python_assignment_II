# 10. Write a function that takes camel-cased strings (i.e.
# ThisIsCamelCased), and converts them to snake case (i.e.
# this_is_camel_cased). Modify the function by adding an argument,
# separator, so it will also convert to the kebab case
# (i.e.this-is-camel-case) as well.

def to_snake_or_kebab(camel, separator):
    converted = ""
    start = 0
    for i in range(1, len(camel), 1):
        if camel[i].isupper():
            converted = converted + camel[start:i] + separator
            start = i
    converted = converted + camel[start:]
    return converted.lower()


camel = input("Enter a camel-cased string: ")
snake = to_snake_or_kebab(camel, "_")
kebab = to_snake_or_kebab(camel, "-")
print("Snake-cased: ", snake)
print("Kebab-cased: ", kebab)
