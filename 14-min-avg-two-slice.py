"""
Write a function that, given a non-empty array A consisting of N integers, 
returns the starting position of the slice with the minimal average. 
If there is more than one slice with a minimal average, 
you should return the smallest starting position of such a slice.

For example, given array A=[4,2,2,5,1,5,8] the function should return 1.
"""

def solution(A):
    min_avg = (A[0] + A[1]) / 2
    idx = 0
    for i in range(2,len(A)):
        avg_2 = (A[i-1] + A[i]) / 2
        if avg_2 < min_avg:
            min_avg = avg_2
            idx = i-1
        avg_3 = (A[i-2] + A[i-1] + A[i]) / 3
        if avg_3 < min_avg:
            min_avg = avg_3
            idx = i-2
    return idx 

A=[4,2,2,5,1,5,8]
print(solution(A))