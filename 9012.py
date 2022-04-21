# coding: utf-8
"""
난이도 : 3

문제 : 문제에서 입력으로 반복할 테스트 케이스 수 T가 주어지고, 다음 줄부터 T줄 만큼 괄호 문자열이 한 줄씩 주어집니다. 모든 괄호의 쌍이 맞으면 YES를, 쌍이 맞지 않으면 NO를 출력합니다.

알고리즘 : 
1. 일반 풀이 : 쌍이 맞는지 체크하는 변수 pair_check=0으로 초기화. 
brk_list의 요소를 brk로 반복하며, '('로 시작하는 경우 pair_check+=1을 해주고, ')'로 끝나는 경우 pair_check-=1을 해줍니다. 
    만약, pair_check<0 이라면 괄호 쌍에 맞지않게 ')'가 한번 더 나온경우 -> NO를 출력. 
brk_list를 모두 반복하고, pair_check>0 이라면, 괄호쌍이 맞지않게 '('가 더 많은 경우 -> NO 출력
pair_check가 0인 경우는 모든 괄호쌍이 맞는 경우이므로, YES를 출력

2. 숏코딩 풀이 : b에 '()'가 존재하는 동안 계속 반복하며 '()'를 제외. b가 빈문자열이면 괄호쌍이 맞는 경우, 빈문자열이 아니면 괄호쌍이 틀린 경우 -> 삼항 연산 
print("NO" if brk else "YES")
"""

## 일반 풀이
T = int(input()) ## 테스트케이스
for _ in range(T):
    brk_list=list(input()) ## 괄호 리스트
    pair_check=0
    for brk in brk_list:
        if brk == '(':
            pair_check+=1
        elif brk ==')':
            pair_check-=1
        if pair_check < 0:
            print("NO")
            break
    if pair_check > 0:
        print("NO")
    elif pair_check==0:
        print("YES")

## 숏코딩
for _ in range(int(input())):
    b=input()
    while '()' in b:
        b=b.replace('()','')
    print("NO" if brk else "YES")