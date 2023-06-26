"""
Write a function that, given three integers A, B and K, 
returns the number of integers within the range [A..B] that are divisible by K.
For example, for A = 6, B = 11 and K = 2, your function should return 3.
"""

def solution(A, B, K):
    if A % K == 0:  
        # we add 1 to the count because A itself is divisible by K
        return (B - A) // K + 1
    else:      
        # we subtract A % K from A to get 
        # the first integer within the range that is divisible by K    
        return (B - (A - A % K )) // K

A = 6
B = 11
K = 2
print(solution(A,B,K))