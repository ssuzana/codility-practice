"""
You are given two non-empty arrays A and B consisting of N integers. 
Arrays A and B represent N fish in a river. 
If P and Q are two fish and P < Q, then fish P is initially upstream of fish Q. 
Initially, each fish has a unique position.

Fish number P is represented by A[P] and B[P]. 
Array A contains the sizes of the fish. All its elements are unique. 
Array B contains the directions of the fish. It contains only 0s and/or 1s, where:
0 represents a fish flowing upstream,
1 represents a fish flowing downstream.
If two fish move in opposite directions and there are no other (living) fish 
between them, they will eventually meet each other. 
Then only one fish can stay alive - the larger fish eats the smaller one. 
More precisely, we say that two fish P and Q meet each other when P < Q, 
B[P] = 1 and B[Q] = 0,and there are no living fish between them. 
After they meet:
If A[P] > A[Q] then P eats Q, and P will still be flowing downstream,
If A[Q] > A[P] then Q eats P, and Q will still be flowing upstream.
We assume that all the fish are flowing at the same speed. 
That is, fish moving in the same direction never meet. 
The goal is to calculate the number of fish that will stay alive.

For example, consider arrays A=[4,3,2,1,5] and B=[0,1,0,0,0].
Initially all the fish are alive and all except fish number 1 are moving upstream. 
Fish number 1 meets fish number 2 and eats it, then it meets fish number 3 and 
eats it too. Finally, it meets fish number 4 and is eaten by it.
The remaining two fish, number 0 and 4, never meet and therefore stay alive.
"""

def solution(A, B):
    stack = [] # store downstream fish
    survivors = 0 # count surviving upstream fish 
    for i in range(len(A)):
        size, direction = A[i], B[i]    
        if direction == 1: # fish flowing downstream
            stack.append(size)
        else: # fish flowing upstream
            while len(stack) > 0:
                if stack[-1] > size:
                    # upstream fish is eatean by the downstream fish
                    break
                else:
                    stack.pop()  # upstream fish eats the downstream fish
            else:
                survivors += 1

    return survivors + len(stack)

A=[4,3,2,1,5]
B=[0,1,0,0,0]
print(solution(A, B))
