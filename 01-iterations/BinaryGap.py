""" 
Write a function that, given a positive integer N, 
returns the length of its longest binary gap. 
The function should return 0 if N doesn't contain a binary gap.
"""

def solution(N):
    # To extract the bit at index i, i.e. the (i+1)th bit: (x >> i) & 1
    last_one = None
    gap = 0
    for i in range(32):
        if (N >> i) & 1:
            if last_one is not None:
                gap = max(gap, i - last_one - 1)
            last_one = i
    return gap    

# N = 1041: return 5, because N has binary representation 10000010001 
print(solution(1041) == 5)
# N = 32: return 0, because N has binary representation 100000 
print(solution(32) == 0)
