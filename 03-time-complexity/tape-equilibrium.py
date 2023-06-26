"""
A non-empty array A consisting of N integers is given. 
Array A represents numbers on a tape.

Any integer P, such that 0 < P < N, splits this tape into two non-empty parts:
 A[0], A[1], ..., A[P - 1] and A[P], A[P + 1], ..., A[N - 1].

The difference between the two parts is the value of: 
|(A[0] + A[1] + ... + A[P - 1]) - (A[P] + A[P + 1] + ... + A[N - 1])|

Find the minimal difference that can be achieved.
For example, given A=[3,1,2,4,3] the function should return 1.
"""

def solution(A):
    left_sum = 0
    right_sum = sum(A)
    min_diff = float('inf')
 
    for i in range(len(A) - 1):
        left_sum += A[i]
        right_sum -= A[i]
        diff = abs(left_sum - right_sum)
        min_diff = min(min_diff, diff)

    return min_diff

A=[3,1,2,4,3]
print(solution(A))