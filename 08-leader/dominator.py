"""
The dominator of array A is the value that occurs in more than half of the elements of A.
Write a function that, given an array A consisting of N integers, returns index of any element 
of array A in which the dominator of A occurs. The function should return -1 if array A does not
have a dominator.

For example, given array A=[3,4,3,2,3,-1,3,3] the function may return 0, 2, 4, 6 or 7.
"""

from collections import Counter
def solution(A):
    counter = Counter(A)
    for i, val in enumerate(A):
        if counter[val] > len(A)/2:
            return i
    return -1

A=[3,4,3,2,3,-1,3,3]
print(solution(A))