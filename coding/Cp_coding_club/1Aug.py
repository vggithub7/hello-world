N=int(input())
arr1=[int(x) for x in input().split()]
M=int(input())
arrven=[int(x) for x in input().split()]
minn=100000000000000
arrfin1=[]
arrfin2=[]

def fb1(cust,ii):
    minn=100000000000000
    for i in range(ii,M):
        if(minn>abs(arr1[cust]-arrven[i])):
                minn=abs(arr1[cust]-arrven[i])
    arrfin1.append(minn)
for i in range(N):
    
    if (abs(arr1[i]-arrven[1])<abs(arr1[i]-arrven[0])):
        if abs(arr1[i]-arrven[1])==0:
            arrfin2.append('O')
        else:
            arrfin2.append('R')
        #minl=abs(arr1[i]-arrven[i+1])
        fb1(i,1)
        #/* while(i!=N-2):
        #    if(minl>abs(arr1[i]-arrven[i+1])):
        #        minl=abs(arr1[i]-arrven[i+1])
        #arrfin1.append('minl') */
    else:
        arrfin1.append(arr1[i]-arrven[0])
        if arr1[i]-arrven[0]:
            arrfin2.append('L')
        else:
            arrfin2.append('O')
    #
for i in range(N):
    print(arrfin1[i],arrfin2[i])
#print(arrfin1,arrfin2)
/*
There is a street in Lucknow which is famous for its street market. The street starts at point 0 and extends upto  units (you can think of these points on a 1-D line starting at zero and extending to the right upto ).

At a moment there are several customers and several street vendors on the street. Each customer in the street wants to reach a vendor as soon as possible. Can you tell for each customer how far is the nearest vendor and in which direction, so that he/she can move to the correct position as desired.

Note: If a customer has nearest vendors at equal distance on both sides. Then the customer prefers to move left

Input Format

First line of the input contains a single integer  (number of customers).

Next line contains a sequence  consisting of  space-seperated non-negative integers, i-th integer representing the coordinates of the i-th customer.

Next line contains a single integer  (Number of street vendors).

Next line contains a sequence  consisting of  space-seperated non-negative integers, i-th integer representing the coordinates of the i-th vendor.

Note: There can be multiple street vendors and customers on the same coordinate.

Constraints



Output Format

Print N lines, i-th line should contain an integer  and a character  seperated by a space, where  represents the distance of the nearest vendor in units from the i-th customer and,  equals 'L' if the nearest vendor is on left side of the customer or 'R' if the nearest customer is on right side or 'O' if a vendor is on the same coordinate as that of the customer (i.e if  equals to zero)

Note: If a customer has nearest vendors at equal distance on both sides. Then the customer prefers to move left

Sample Input 0

2
1 3
2
0 3
Sample Output 0

1 L
0 O
Explanation 0

1st customer with coordinate 1 can go to street vendor at coordinate 0 (1st vendor).

2nd customer with coordinate 3 can stay at the position as there is vendor on that coordinate only.

Sample Input 1

1
4
2
2 6 
Sample Output 1

2 L
Explanation 1

There is only a single customer in the street. The customer has a vendor at distance 2 in left side(at coordinate 2) and a vendor at distance 2 in right side(at coordinate 6). Now as both the vendors are equidistant from the customer, the customer prefers to move left(as given in the question)
*/
