"""
Write a function that, given a non-empty array A, 
returns the value of the maximal product of any triplet.

For example, given array A=[-3,1,2,-2,5,6] such that:
the function should return 60, as the product of triplet (2, 4, 5) is maximal.
"""

def solution(A):
    A.sort()
    return max(A[-3] * A[-2] * A[-1], A[0] * A[1] * A[2], A[0] * A[1] * A[-1])


A=[-3,1,2,-2,5,6]
print(solution(A))
