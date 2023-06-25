"""
An integer N is given, representing the area of some rectangle.
The area of a rectangle whose sides are of length A and B is A * B, 
and the perimeter is 2 * (A + B).

The goal is to find the minimal perimeter of any rectangle whose area equals N. 
The sides of this rectangle should be only integers.

For example, given an integer N = 30, the function should return 22.
Given an integer N = 101, the function should return 204.
"""

import math

def solution(N):
    x = 1
    for i in range(1, math.ceil(math.sqrt(N))+1):
        if N % i == 0:
            x = i
    return 2*x + 2*(N//x)


print(solution(30))
print(solution(101))