"""
Write a function that, given an array A consisting of N integers, 
returns the number of distinct values in array A.

For example, given array A=[2,1,1,2,3,1] the function should return 3.
"""

def solution(A):
    return len(set(A))

A = [2,1,1,2,3,1]
print(solution(A))
