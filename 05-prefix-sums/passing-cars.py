"""
A non-empty array A consisting of N integers is given. 
The consecutive elements of array A represent consecutive cars on a road.

Array A contains only 0s and/or 1s:
0 represents a car traveling east,
1 represents a car traveling west.

The goal is to count passing cars. We say that a pair of cars (P, Q), 
where 0 <= P < Q < N, is passing when P is traveling to the east and
 Q is traveling to the west.

For example, consider array A=[0,1,0,1,1].
We have five pairs of passing cars: (0, 1), (0, 3), (0, 4), (2, 3), (2, 4).
"""

def solution(A):
    zeros = 0
    pairs = 0
    for a in A:
        if a == 0:
            zeros +=1
        elif a == 1:
            pairs += zeros
            if pairs > 10**9:
                return -1      
    return pairs 

A=[0,1,0,1,1]
print(solution(A))