# coding: utf-8
"""
난이도 : 3

문제 : 문제에서 정의한 fibonacci함수에 테스트 케이스(T)만큼 반복하여 자연수 N을 넣었을때, 0이 출력되는 횟수와 1이 출력되는 횟수를 구하는 문제

알고리즘 : 0이 출력되는 횟수, 1이 출력되는 횟수 역시, 피보나치 수열임을 통해 구함.
    
"""
## 일반 풀이
def fib(N):
    zeros=[1,0,1]
    ones=[0,1,1]
    if N >= 3:
        for i in range(2,N):
            zeros.append(zeros[i-1] + zeros[i])
            ones.append(ones[i-1] + ones[i])
    print(f"{zeros[N]} {ones[N]}")

T = int(input())
for _ in range(T):
    N = int(input())
    fib(N)

## 숏코딩 풀이
T = int(input())
for _ in range(T):
    N = int(input())
    zero,one=1,0 # zero: 0개수, one: 1개수
    for i in range(N):
        zero,one = one,zero+one # zero와 one에 대해 피보나치적용
    print(zero,one)