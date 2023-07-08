"""
Write a function that, given an array A consisting of N integers
 and an integer K, returns the array A rotated K times.
 For example, given
    A = [3, 8, 9, 7, 6]
    K = 3
the function should return [9, 7, 6, 3, 8].
"""

def solution1(A, K):
    K = K % len(A)
    if A == []:
        return A
    while K > 0:
        last = A.pop()
        A = [last] + A
        K -= 1
    return A  

def solution2(A, K):
    # modify A in-place
    if A == []:
        return A
    K = K % len(A)
    i = 0
    start = 0
    while i < len(A):
        cur = start 
        prev = A[start] #store the value in the position
        
        while True:
            next_idx = (cur + K) % len(A) 
            temp = A[next_idx] #store it temporaly 
            A[next_idx] = prev #overide the next 
            prev = temp #reset prev
            cur = next_idx #reset current
            i += 1

            if start == cur:
                break 
        
        start += 1
    return A   

print(solution2(A=[3, 8, 9, 7, 6], K=3))
