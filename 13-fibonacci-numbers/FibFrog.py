"""
https://app.codility.com/demo/results/trainingJRUT4G-Y9R/

A small frog wants to get to the other side of a river. The frog is initially located at one bank of the river (position -1)
and wants to get to the other bank (position N). The frog can jump over any distance F(K), where F(K) is the K-th Fibonacci 
number. Luckily, there are many leaves on the river, and the frog can jump between the leaves, but only in the direction of 
the bank at position N.

The leaves on the river are represented in an array A consisting of N integers. Consecutive elements of array A represent 
consecutive positions from 0 to N - 1 on the river. Array A contains only 0s and/or 1s:

0 represents a position without a leaf;
1 represents a position containing a leaf.

The goal is to count the minimum number of jumps in which the frog can get to the other side of the river 
(from position -1 to position N). The frog can jump between positions -1 and N (the banks of the river) 
and every position containing a leaf.

For example, consider array A=[0,0,0,1,1,0,1,0,0,0,0].
The frog can make three jumps of length F(5) = 5, F(3) = 2 and F(5) = 5.

"""


def solution(A):
    A.append(1)  # Append 1 to mark the other side of the river
    N = len(A)

    # Generate Fibonacci numbers up to N
    fib = [1, 1]
    while fib[-1] + fib[-2] <= N:
        fib.append(fib[-1] + fib[-2])

    # Create an array to track reachable positions
    reachable = [-1] * N
    for jump in fib:
        reachable[jump - 1] = 1

    # Iterate over each position in A
    for i, val in enumerate(A):
        if reachable[i] > 0 and val == 1:
            # Try different jump sizes from Fibonacci sequence
            for jump in fib:
                if jump + i >= N:  # Check if jumping beyond the river's length
                    break
                else:
                    # Update the minimum number of jumps required to reach the current position
                    if reachable[i + jump] < 0 or reachable[i + jump] > reachable[i] + 1:
                        reachable[i + jump] = reachable[i] + 1

    return reachable[-1] 

A=[0,0,0,1,1,0,1,0,0,0,0]
print(solution(A))