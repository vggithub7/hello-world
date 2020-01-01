"""program: Create a dictionary with values (i, i*i) with 1 to n"""
def my_dict(n):
    dict={}
    for i in range(1,n+1):
        dict[i]=i*i
    return dict
dict={}
n=int(input("enter value till which u want squares "))
dict=my_dict(n)     
print(dict) 