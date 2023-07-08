
"""
A non-empty array A consisting of N integers is given.
The leader of this array is the value that occurs in more than half of the elements of A.
An equi leader is an index S such that 0 ≤ S < N - 1 and two sequences A[0], A[1], ..., A[S] 
and A[S + 1], A[S + 2], ..., A[N - 1] have leaders of the same value.

For example, given array A=[4,3,4,4,4,2] we can find two equi leaders:
0, because sequences: (4) and (3, 4, 4, 4, 2) have the same leader, whose value is 4.
2, because sequences: (4, 3, 4) and (4, 4, 2) have the same leader, whose value is 4.
The goal is to count the number of equi leaders.
"""

from collections import Counter
def solution(A):
    """
    If two local leaders are equal in value, then that value is also shared by the global leader;
    or, conversely, if the list has no leader, then there is no equi leader to be found either.
    """
    N = len(A)
    counter = Counter(A)
    # get most frequent element and its count
    candidate_leader, count = counter.most_common(1)[0]

    if count <= N // 2:
        return 0

    equi_leaders = 0
    sub_count = 0

    for i, num in enumerate(A):
        if num == candidate_leader:
            sub_count += 1
        if sub_count > (i + 1)//2 and (count - sub_count) > (N - i - 1)//2:
            equi_leaders += 1
    
    return equi_leaders  
