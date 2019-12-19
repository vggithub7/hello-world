#program: print sum of curr and prev given a list of numbers

def sum_curr_prev(list):
    prev=0
    
    for i in list :
        sum=prev+i
        print(sum)
        prev=i
list=[1,2,3,4,5,6,7,8,9,10]
sum_curr_prev(list)