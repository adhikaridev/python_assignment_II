# 19. Write a Python class to find validity of a string of parentheses, '(',
# ')', '{', '}', '[' and ']. These brackets must be close in the correct order,
# for example "()" and "()[]{}" are valid but "[)", "({[)]" and "{{{" are invalid

class Bracket:
    def __init__(self, brackets):
        self.brackets = brackets

    def check_validity(self):
        stack = []
        opening = ['(', '{', '[']
        closing = [')', '}', ']']
        for b in self.brackets:
            if b in opening:
                stack.append(b)
            if b in closing:
                i = closing.index(b)
                corresponding_of_b = opening[i]
                if stack[-1] == corresponding_of_b:
                    stack.pop()
        size_of_stack = len(stack)
        if size_of_stack == 0:
            print(f"{self.brackets} is valid.")
        else:
            print(f"{self.brackets} is not valid.")

brackets = input("Enter a string of brackets: ")
b1 = Bracket(brackets)
b1.check_validity()
