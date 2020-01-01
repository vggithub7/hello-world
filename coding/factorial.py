"""program: To find factorial of a number"""
def factorial1(num):
    if num==1:
        return 1
    else:
        return num*factorial1(num-1)
num1=(int(input("enter number for factorial :")))
num = factorial1(num1)
print("number {} fact is :".format(num1), num)