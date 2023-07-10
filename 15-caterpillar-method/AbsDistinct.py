"""
https://app.codility.com/demo/results/trainingYW2MP2-S8Y/

A non-empty array A consisting of N numbers is given. The array is sorted in non-decreasing order. 
The absolute distinct count of this array is the number of distinct absolute values among the elements of the array.

For example, consider array A=[-5,-3,-1,0,3,6].
The absolute distinct count of this array is 5, because there are 5 distinct absolute values among the elements of this array, 
namely 0, 1, 3, 5 and 6.

"""

def solution(A):
    return len(set([abs(val) for val in A]))


A=[-5,-3,-1,0,3,6]
print(solution(A))