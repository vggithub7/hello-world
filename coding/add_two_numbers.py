#program To add two numbers in python

def add_two_num(a,b):
    return a+b
a,b=[int(x) for x in input("enter two number :").split()]
print(add_two_num(a,b))