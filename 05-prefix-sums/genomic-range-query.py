"""
A DNA sequence can be represented as a string consisting of the letters A, C, G and T, 
which correspond to the types of successive nucleotides in the sequence. 
Each nucleotide has an impact factor, which is an integer. 
Nucleotides of types A, C, G and T have impact factors of 1, 2, 3 and 4, respectively. 
You are going to answer several queries of the form: 
What is the minimal impact factor of nucleotides contained in a particular part of the given DNA sequence?

The DNA sequence is given as a non-empty string S = S[0]S[1]...S[N-1] consisting of N characters. 
There are M queries, which are given in non-empty arrays P and Q, each consisting of M integers. 
The K-th query (0 <= K < M) requires you to find the minimal impact factor of nucleotides contained 
in the DNA sequence between positions P[K] and Q[K] (inclusive).

For example, given the string S = 'CAGCCTA' and arrays P=[2,5,0], Q=[4,5,6],
the function should return the values [2, 4, 1].
"""

def solution(S, P, Q):
    ans = []
    for i,j in zip(P,Q):
        part = S[i:j+1]
        if 'A' in part:
            ans.append(1)
        elif 'C' in part:
            ans.append(2)
        elif 'G' in part:
            ans.append(3)
        else:
            ans.append(4)
    return ans 

S = 'CAGCCTA'
P=[2,5,0]
Q=[4,5,6]
print(solution(S,P,Q))