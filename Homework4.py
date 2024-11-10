"""
Group 36
Micaela Arleo-Gil (U95656807)
Tiffany Whitsett (U90321785)
"""

"""
    Write your main code for each question in the specified functions
    as they will be used for unit testing. You can define other functions
    to modularize your code but remember that the following functions are the
    ones that are called by our tester.

    ** Do not change the name of the file to anything else.
"""

class Stack:
    """
        Create Stack object:
            stack_obj = Stack()

        Iterate through the stack:
            for ele in stack_obj:
                stack_obj.push(ele)
                       or
                stack_obj.pop(ele)

        Access top of the stack:
            print(stack_obj.peek())
    """
    def __init__(self):
     self.items = list()

    def is_empty(self):
        return self.items == []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[len(self.items)-1]
    def size(self):
        return len(self.items)


def question4(string):
    """
        You are given a string, return true if the string is palindrome, otherwise, return false.
        Use class of Stack for the implementation.
    """
    s = Stack()
    palin = True
    nonpalin = False

    for char in string:
        s.push(char)

    for char in string:
        if char != s.pop():
            return nonpalin
        
    return palin


