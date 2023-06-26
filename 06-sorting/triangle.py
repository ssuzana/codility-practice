"""
An array A consisting of N integers is given. 
A triplet (P, Q, R) is triangular if 0 ≤ P < Q < R < N and:
A[P] + A[Q] > A[R],
A[Q] + A[R] > A[P],
A[R] + A[P] > A[Q].

Write a function that, given an array A consisting of N integers, 
returns 1 if there exists a triangular triplet for this array and 
returns 0 otherwise.

For example, given array A=[10,2,5,1,8,20] the function should return 1.
Given array A=[10,50,5,1] the function should return 0.
"""

def solution(A):
    if len(A) < 3:
        return 0
    A.sort()
    for i in range(len(A)-2):
        if A[i] + A[i+1] > A[i+2]:
            return 1
    return 0 

A=[10,2,5,1,8,20]
print(solution(A))
A=[10,50,5,1]
print(solution(A))