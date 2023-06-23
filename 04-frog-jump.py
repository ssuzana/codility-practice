"""
A small frog wants to get to the other side of the road. 
The frog is currently located at position X and wants to get to
a position greater than or equal to Y. The small frog always 
jumps a fixed distance, D.
Count the minimal number of jumps that the small frog must perform
to reach its target.
For example, given: X = 10, Y = 85, D = 30
the function should return 3.
"""
import math
def solution(X, Y, D):
    # Implement your solution here
    return math.ceil((Y-X) / D)

X = 10
Y = 85
D = 30
print(solution(X, Y, D))