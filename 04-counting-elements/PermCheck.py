"""
A non-empty array A consisting of N integers is given.
A permutation is a sequence containing each element from 1 to N once, and only once.
Write a function that, given an array A, returns 1 if array A is a permutation
and 0 if it is not.
For example, given array A=[4,1,3,2] the function should return 1.
Given array A=[4,1,3] the function should return 0.

"""
def solution(A):
    n = len(A)
    s = set(range(1,n+1))

    for a in A:
        if a not in s:
            return 0
        s.remove(a)
    if not s:
        return 1
    return 0  

A=[4,1,3,2]
print(solution(A))
A=[4,1,3]
print(solution(A))
