"""
A non-empty array A consisting of N integers is given. 
The array contains an odd number of elements, and each element of the array 
can be paired with another element that has the same value, 
except for one element that is left unpaired.
Write a function that, given an array A consisting of N integers
 fulfilling the above conditions, returns the value of the unpaired element.

For example, given array A=[9,3,9,3,9,7,9] the function should return 7.
"""
def solution(A):
    ans = 0
    for a in A:
        ans ^= a
    return ans  

A=[9,3,9,3,9,7,9]
print(solution(A))