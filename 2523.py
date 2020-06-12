# coding: utf-8
"""
난이도 : 1

문제 : 정수 N 이 주어진다.
 1 부터 N 개 까지 줄 바꿔가며 별을 그리고,  N부터 1개 까지 줄 바꿔가며 별을 그려라.

알고리즘 : for 문을 통해 1부터 2N-1 까지 i로 반복하며,
i가 N 이하일때까진 *을 i 개씩 출력하고, i가 N 초과하면, *을 2N-i 번 출력한다.
    
"""
N = int(input())
for i in range(1,2*N):
    if i <= N:
        print('*'*i)
    else:
        print('*'*(2*N-i))