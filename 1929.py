# coding: utf-8
"""
난이도 : 4

문제 : 자연수 M과 N이 주어진다. ( 1 <= M <= N)
M이상 N이하의 소수를 순서대로 출력. (소수는 1개이상 반드시 존재하도록 입력이 주어진다.)

알고리즘 : 에라토스테네스 체를 활용
sieve 변수에 N에 대하여 체 초기화 (0부터 N까지 N+1개에 True로 배열 초기화)
for문 이용 sqrt(N)+1까지만 i로 반복(그 뒤에는 앞수의 배수이기 때문)
  i가 소수이면 i를 제외한 모든 i의 배수를 제외(seive[i]=False)
for문이 끝나면 seive 변수에 True인 인덱스(2 이상)는 모두 소수이다.
seive배열의 소수중 M 이상인 소수만 출력.    
"""

def eratos_mn(m,n):
    N=n+1;M=m
    sieve=[True]*N # 체 초기화 (0부터 n-1 까지)

    m = int(N ** 0.5) + 1 # sqrt(n)+1 까지만 반복하면된다. 
    for i in range(2,m): # 소수는 2부터
        if sieve[i] == True: # 소수이면
            for j in range(i+i, N, i): # i의 2배수부터, 모든 배수 제거
                sieve[j] = False
    ## M이상 이고, 소수인 경우 리스트로 반환
    return [i for i in range(2,N) if (sieve[i] == True) and (i >= M)]

M,N=map(int,input().split())
print(*eratos_mn(M,N),sep='\n')