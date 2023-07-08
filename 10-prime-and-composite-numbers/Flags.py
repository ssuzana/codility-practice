"""
A non-empty array A consisting of N integers is given.
A peak is an array element which is larger than its neighbours. 
More precisely, it is an index P such that 0 < P < N - 1 and 
A[P - 1] < A[P] > A[P + 1].

For example, the array A=[1,5,3,4,3,4,1,2,3,4,6,2]
has exactly four peaks: elements 1, 3, 5 and 10.

 You have to choose how many flags you should take with you. The goal is to set 
 the maximum number of flags on the peaks, according to certain rules:

 Flags can only be set on peaks. What's more, if you take K flags, 
 then the distance between any two flags should be greater than or equal to K. 
 The distance between indices P and Q is the absolute value |P - Q|.

For example, given the mountain range represented by array A, above, with N = 12, if you take:
two flags, you can set them on peaks 1 and 5;
three flags, you can set them on peaks 1, 5 and 10;
four flags, you can set only three flags, on peaks 1, 5 and 10.
You can therefore set a maximum of three flags in this case.

Write a function that, given a non-empty array A of N integers, 
returns the maximum number of flags that can be set on the peaks of the array.
"""

def solution(A):
    N = len(A)

    # find all the peaks
    peaks = []
    for i in range(1, N-1):
        if A[i] > A[i-1] and A[i] > A[i+1]:
            peaks.append(i)

    num_peaks = len(peaks)

    if num_peaks < 2:
        return num_peaks

    # binary search to find the maximum number of flags
    left, right = 1, num_peaks

    while left <= right:
        flags = (left + right) // 2
        pos, count = 0, 0

        for i in range(num_peaks):
            if peaks[i] >= pos:
                count += 1
                pos = peaks[i] + flags

                if count == flags:
                    break

        if count >= flags:
            left = flags + 1
        else:
            right = flags - 1

    return right

A=[1,5,3,4,3,4,1,2,3,4,6,2]
print(solution(A))
