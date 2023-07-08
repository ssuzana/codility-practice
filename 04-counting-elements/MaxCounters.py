'''
You are given N counters, initially set to 0, and you have two possible operations on them:
- increase counter by 1: increase(X)
- max counter: set value of all counters to current maximum.
A non-empty array A of M integers is given. This array represents consecutive operations:
if A[K] = X, such that 1 <= X <= N, then operation K is increase(X),
if A[K] = N + 1 then operation K is max counter.
For example, given integer N = 5 and array A=[3,4,4,6,1,4,4]
the values of the counters after each consecutive operation will be:
    (0, 0, 1, 0, 0)
    (0, 0, 1, 1, 0)
    (0, 0, 1, 2, 0)
    (2, 2, 2, 2, 2)
    (3, 2, 2, 2, 2)
    (3, 2, 2, 3, 2)
    (3, 2, 2, 4, 2)
'''

def solution(N, A):
    ans = [0] * N
    max_val = 0
    cur_max = 0
    for a in A:
        if 1 <= a <= N:
            if max_val > ans[a-1]:
                ans[a-1] = max_val
            ans[a-1] += 1   
            cur_max = max(cur_max, ans[a-1])  
        else:
            max_val = cur_max    
 
    return [max(val, max_val) for val in ans] 


N = 5
A=[3,4,4,6,1,4,4]
print(solution(N,A))
