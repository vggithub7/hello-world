def multiply_sum(num1,num2):
    if num1*num2>1000:
        return num1+num2
    else:
        return num1*num2
    
a=int(input("enter a number")) 
b=int(input("enter another number"))
c=multiply_sum(a,b)
print(c)