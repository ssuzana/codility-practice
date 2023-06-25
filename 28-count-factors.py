"""
Write a function that, given a positive integer N, returns the number of its factors.
For example, given N = 24, the function should return 8, because 24 has 8 factors,
namely 1, 2, 3, 4, 6, 8, 12, 24. There are no other factors of 24.
"""

def solution(N):
    num_factors = 0
    i = 1
    while i**2 < N:
        if N % i == 0:
            # if i is a factor of N, then N/i is also a factor
            num_factors += 2
        i += 1
    if i**2 == N:
        num_factors += 1
    return num_factors 

print(solution(24))