# coding: utf-8
"""
난이도 : 3

문제 : 숫자 개수(N)와, 1 이상 정수의 나열이 주어진다.
      1 부터 N까지 순서대로 스택에 넣고 빼면서 입력받은 정수의 나열을 만들 수 있는지 묻는 문제입니다.
      만들 수 있다면 push와 pop을 어떤 순서대로 하는지 +와 -로 출력하고 만들 수 없다면 "NO"를 출력.

알고리즘 : 숫자 개수(N)을 for문으로 반복하면서, 각 반복에서 수(trg)를 입력받습니다.
              while 문을 통해 입력받은 수(trg) 까지 cnt를 통해 1부터 차례대로 stack에 넣습니다.(result에 '+'도 넣습니다.)
              trg 순서가 되면 스택의 끝부분과 타겟이 되는 trg가 같을때 pop 하며 result에 '-'를 넣습니다.
          그렇게 다음 반복에서도 while문 부터 돌며 trg와 cnt를 비교합니다. 만약 cnt가 trg와 같은경우 스택의 마지막과 trg를 비교했을 때 같지 않으면 스택을 통해 만들어질 수 없는 수열이라고 판단하고 NO를 출력합니다.

          -> cnt는 순서대로 stack에 값이 들어가도록 하며, stack의 마지막 값이 수의 나열과 달라지면 NO를 출력하도록 하는 알고리즘입니다.

    
"""
from collections import deque

def stack_seq(N,stack,result,cnt):
    for i in range(N):
        trg = int(input())
        while cnt < trg:
            cnt+=1
            stack.append(cnt)
            result.append('+')
        if stack[-1] == trg:
            stack.pop()
            result.append('-')
            continue
        else:
            result = False
            break
    if result:
        for i in result:
            print(i)
    else:
        print("NO")

N = int(input())
stack = [] # 대신에 stack = deque() 를 사용한다면, 자료구조 특성에 의해 성능이 향상됩니다.
result = []
cnt=0
stack_seq(N,stack,result,cnt)