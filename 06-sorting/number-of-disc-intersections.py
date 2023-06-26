"""
We draw N discs on a plane. The discs are numbered from 0 to N - 1.
An array A of N non-negative integers, specifying the radiuses of the discs, 
is given. The J-th disc is drawn with its center at (J, 0) and radius A[J].

Write a function that, given an array A describing N discs as explained above, 
returns the number of (unordered) pairs of intersecting discs. 
The function should return -1 if the number of intersecting pairs exceeds 10,000,000.

Given array A=[1,5,2,1,4,0] the function should return 11.
"""

def solution(A):
    n = len(A)
    left, right = [0] * n, [0] * n
    pairs = 0

    for i in range(n):
        left[i] = i - A[i] 
        right[i] = A[i] + i

    left.sort()
    right.sort()
    
    active_discs = 0
    j = 0
    for i in range(n):
        while j < n and left[j] <= right[i]:
            active_discs += 1
            j += 1
            
        active_discs -= 1
        pairs += active_discs

        if pairs > 10**7:
            return -1

    return pairs 

A=[1,5,2,1,4,0]
print(solution(A))