"""
Program: Find Prime Numbers in a range
"""
import math
def prime_numbers_in_interval(a,b):
    
    list1=[]
    list2=[]
    my_dict={}
    if(a<0 and b<0):
        print("enter valid range ")
    for num in range(a,b+1):
        if num<2:
            continue
        flag=0
        for i in range(2,math.ceil(num/2)+1):
            if num%i == 0:
                flag=1
                list2.append(i)
        if flag==0:
            #print("{} is prime".format(num))
            list1.append(num)
        elif flag ==1:
            #print("{} is not prime, its divisible by {}".format(num,list2))
            my_dict[num]=list2
            list2=[]
    print("list of prime numbers: ",list1)
    return list1,my_dict            
a,b=[int(x) for x in input("enter two numbers as range to find prime numbers: ").split()]

primes,non_primes=prime_numbers_in_interval(a,b)
print("prime list is",primes)
print("composite num list (with all factors)")
for x in non_primes.items():
    print (x)