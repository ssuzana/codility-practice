
'''
https://app.codility.com/demo/results/trainingS5WKN8-4EZ/

You are given an array A consisting of N integers.
For each number A[i] such that 0 <= i < N, we want to count the number of elements of the array
that are not the divisors of A[i]. We say that these elements are non-divisors.

'''
import math
from collections import Counter 

def solution(A):
    counter = Counter(A)
    nondiv = {}

    for item in counter:
        num_divisor = 0
        for i in range(1, int(math.sqrt(item)) + 1, 1):
            if (item % i ==0):
                another_divisor = item // i 
            
                if i in counter:
                    num_divisor = num_divisor + counter[i] 
                
                if another_divisor != i:
                    if another_divisor in counter:
                        num_divisor = num_divisor + counter[another_divisor]
                
        num_non_divisor = len(A) - num_divisor
        nondiv[item] = num_non_divisor
    
    return [nondiv[A[i]] for i in range(len(A))]


A = [3, 1, 2, 3, 6]
print(solution(A))