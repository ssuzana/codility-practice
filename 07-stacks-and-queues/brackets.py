"""
A string S consisting of N characters is considered to be properly nested 
if any of the following conditions is true:

- S is empty;
- S has the form "(U)" or "[U]" or "{U}" where U is a properly nested string;
- S has the form "VW" where V and W are properly nested strings.
For example, the string "{[()()]}" is properly nested but "([)()]" is not.

Write a function that, given a string S consisting of N characters,
 returns 1 if S is properly nested and 0 otherwise.

For example, given S = "{[()()]}", the function should return 1 and 
given S = "([)()]", the function should return 0.
"""

def solution(S):
    hashmap = {")" : "(", "]" : "[", "}" : "{"}
    stack = []

    for ch in S:
        if stack and ch in hashmap and stack[-1] == hashmap[ch]:
            stack.pop()
        else:
            stack.append(ch)     
    if not stack:
        return 1
    return 0    

S = "{[()()]}"
print(solution(S))
S = "([)()]"
print(solution(S))