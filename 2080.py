# coding: utf-8
"""
난이도 : 6

문제 : 괄호 쌍이 올바르게 맞는 수식이 주어진다. (괄호쌍은 적어도1개, 많아야 10개)
해당 수식에서 **올바른 괄호 쌍을 제거해서 나올 수 있는 서로 다른 식을 사전 순으로 출력 (괄호쌍이 적어도 1개 이상이기 때문에, 제거되는 괄호쌍은 1개 이상, 10개 이하이다.)**

알고리즘 : 
1. 어떤 자료형으로 어떻게 풀었는지
    1. 처음에 입력받은 문자열을 리스트로 만들어서, **스택을 이용해 괄호쌍을 찾아,** **괄호쌍의 인덱스를 갖는 리스트**를 만든다. 
    2. 처음에 입력받은 문자열 리스트에서 괄호부분을 모두 제거 → 공백 문자( ‘’ )로 만든다.
    3. 괄호쌍 인덱스 리스트에 대해 **combinations를 이용 → 추가할 괄호쌍의 인덱스를 사용**.
        1. 즉, combinations의 2번째 인자로 0을 넣으면, 추가할게 없는 경우 (모든 괄호가 제외된 경우)
        2. 1을 넣으면 1개의 괄호쌍을 제외한 경우
        3. 주어진 예시에서 괄호쌍이 총 2개이므로, 이건 돌지 않음
    4. 괄호쌍이 제외된게 중복일 수 있으니, 이를 모두 집합에 추가한뒤 → sorted하여 출력 
"""
from itertools import combinations

problem = list(input()) # 문제 입력받는 리스트
p, brk_idx = [],[] # 괄호쌍 찾을 스택 -> p , 괄호쌍 인덱스 저장할 이중리스트 -> brk_idx
result=set() # 결과 저장할 집합

for i,v in enumerate(problem): ## 괄호쌍 인덱스 저장 및 problem에서 괄호 제거
    if v == '(':
        problem[i]=''
        p.append(i)
    if v == ')':
        problem[i]=''
        brk_idx.append([p.pop(),i])      

for i in range(len(brk_idx)): ## 괄호쌍의 조합(combinations)을 이용해 괄호 추가
    for j in combinations(brk_idx,i):
        P=problem[:]
        for s,e in j:
            P[s]='('
            P[e]=')'
        result.add(''.join(P))
print(*sorted(result),sep='\n') ## 결과 출력