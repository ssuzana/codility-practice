"""
A small frog wants to get to the other side of a river. 
The frog is initially located on one bank of the river (position 0)
and wants to get to the opposite bank (position X+1). 
Leaves fall from a tree onto the surface of the river.

You are given an array A consisting of N integers representing the falling leaves.
A[K] represents the position where one leaf falls at time K, measured in seconds.

The goal is to find the earliest time when the frog can jump to the other side 
of the river. The frog can cross only when leaves appear at every position across 
the river from 1 to X (that is, we want to find the earliest moment when all the
positions from 1 to X are covered by leaves). 
If the frog is never able to jump to the other side of the river,
the function should return -1.
For example, given X = 5 and array A=[1,3,1,4,2,3,5,4]
the function should return 6.
"""

def solution(X, A):
    leaves = [0] * (X+1)
    total_leaves = 0

    for i,a in enumerate(A):
        if leaves[a] == 0:
            leaves[a] += 1
            total_leaves += 1
        if total_leaves == X:
            return i
    return -1      

A=[1,3,1,4,2,3,5,4]
X=5
print(solution(X, A))