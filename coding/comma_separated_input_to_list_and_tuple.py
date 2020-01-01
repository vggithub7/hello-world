"""program: accept comma separated numbers as input and output a list and tuple"""
def accept_comma_input(n):
    n=n.split(",")
    return n,tuple(n)

n=input("enter comma separated values : ")
list,tuple=accept_comma_input(n)
print("list of input values is : \n",list,"\n tuple of input values is : \n",tuple)
