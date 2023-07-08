"""
A non-empty array A consisting of N integers is given. 
A pair of integers (P, Q), such that 0 <= P <= Q < N, is called a slice of array A. 
The sum of a slice (P, Q) is the total of A[P] + A[P+1] + ... + A[Q].

Write a function that, given an array A consisting of N integers, 
returns the maximum sum of any slice of A.

For example, given array A=[3,2,-6,4,0] the function should return 5.
"""

def solution(A):
    cur_sum = 0
    max_sum = float("-inf")

    for a in A:
        if cur_sum < 0:
            cur_sum = a
        else:
            cur_sum += a
        max_sum = max(max_sum, cur_sum)      

    return max_sum

A=[3,2,-6,4,0]
print(solution(A))
