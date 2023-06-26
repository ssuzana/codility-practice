"""
Write a function,that, given an array A consisting of N integers containing daily prices 
of a stock share for a period of N consecutive days, returns the maximum possible profit
from one transaction during this period. The function should return 0 if it was impossible
to gain any profit.

For example, given array A = [23171, 21011, 21123, 21366, 21013, 21367]
the function should return 356.
"""

def solution(A):
    if not A:
        return 0
    min_so_far = A[0]
    max_profit = 0

    for i in range(1, len(A)):
        if A[i] > min_so_far:
            max_profit = max(max_profit, A[i]- min_so_far)
        else:
            min_so_far = A[i]
            
    return max_profit 

A = [23171, 21011, 21123, 21366, 21013, 21367]
print(solution(A))