"""program: To print numbers between 2000 and 3200(both included) divisible by 7 but not 5"""

def function(num1,num2):
    list1=[]
    for i in range(num1,num2+1):
        if(i%7==0 and i%5!=0):
            list1.append(i)
    return list1
list=[]
list=function(2000,3200)
print("numbers between 2000 and 3200 div by 7 and not 5 :")
print(list)