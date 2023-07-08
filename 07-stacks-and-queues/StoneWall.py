"""
You are going to build a stone wall. The wall should be straight and N meters long, 
and its thickness should be constant; however, it should have different heights in 
different places. The height of the wall is specified by an array H of N positive 
integers. H[I] is the height of the wall from I to I+1 meters to the right of its 
left end. In particular, H[0] is the height of the wall's left end and H[N-1] is
 the height of the wall's right end.

The wall should be built of cuboid stone blocks (that is, all sides of such blocks 
are rectangular). Your task is to compute the minimum number of blocks needed to 
build the wall.

Write a function that, given an array H of N positive integers specifying the
height of the wall, returns the minimum number of blocks needed to build it.

For example, given array H=[8,8,5,7,9,8,7,4,8] containing N = 9 integers
the function should return 7. 
"""

def solution(H):
    stack = []
    num_blocks = 0
    for height in H:
        while stack and height < stack[-1]:
            stack.pop()
            num_blocks += 1
        if not stack or height > stack[-1]:
            stack.append(height)
    return num_blocks + len(stack)   

H=[8,8,5,7,9,8,7,4,8]
print(solution(H))
