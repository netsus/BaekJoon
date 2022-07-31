# coding: utf-8
"""
난이도 : 7

문제 : 2812 크게 만들기

알고리즘 : 그리디, 스택
    
"""
import sys
I = sys.stdin.readline
N, K = map(int, I().split())
S = I()
k = K
s = [S[0]]
for e in S[1:]:
    while k and s and s[-1] < e:
        s.pop()
        k -= 1
    s.append(e)
print(''.join(s[:N-K]))
