"""
Write a function that, given an array A of N integers, 
returns the smallest positive integer (greater than 0) that does not occur in A.

For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.
Given A = [1, 2, 3], the function should return 4.
Given A = [-1, -3], the function should return 1.
"""

def solution(A):
    min_so_far = 1
    A.sort()
    for a in A:
        if a == min_so_far:
            min_so_far += 1
    return min_so_far 

A = [1, 3, 6, 4, 1, 2]
print(solution(A))