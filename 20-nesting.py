"""
A string S consisting of N characters is called properly nested if:
 - S is empty;
 - S has the form "(U)" where U is a properly nested string;
 - S has the form "VW" where V and W are properly nested strings.
For example, string "(()(())())" is properly nested but string "())" isn't.

Write a function that, given a string S consisting of N characters, 
returns 1 if string S is properly nested and 0 otherwise.

For example, given S = "(()(())())", the function should return 1 and 
given S = "())", the function should return 0.
"""

def solution(S):
    stack = []
    for ch in S:
        if stack and ch == ")" and stack[-1] == "(":
            stack.pop()
        else:
            stack.append(ch)     
    if not stack:
        return 1
    return 0 

S = "(()(())())"
print(solution(S))
S = "())"
print(solution(S))