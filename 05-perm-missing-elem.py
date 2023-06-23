"""
An array A consisting of N different integers is given. 
The array contains integers in the range [1..(N + 1)], 
which means that exactly one element is missing.
Your goal is to find that missing element.

For example, given array A=[2,3,1,5] the function should return 4.
"""
def solution(A):
    N = len(A)
    return (N+1)*(N+2)//2 - sum(A)

A=[2,3,1,5]
print(solution(A))