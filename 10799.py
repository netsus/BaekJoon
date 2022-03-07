# coding: utf-8
"""
난이도 : 6

문제 : '('와 ')'로 이루어진 문자열이 주어진다.
    괄호'()'가 완성되는 부분에서 레이져가 발사된다. 3가지 조건에 따라 쇠막대기가 존재한다.
    1. 쇠막대기는 자신보다 긴 쇠막대기 위에만 놓일 수 있다.
    2. 각 쇠막대기를 자르는 레이저는 적어도 하나 존재한다.
    3. 레이저는 어떤 쇠막대기의 양 끝점과도 겹치지 않는다.

알고리즘 : 스택을 이용하여 잘리는 쇠막대기 개수를 세는 알고리즘.
괄호로 이루어진 문자열을 br에 할당. 
for문을 이용해 br을 하나씩 반복하며
  '('로 시작하는 경우 stack에 넣는다. (레이저로 잘릴 때, 쇠막대기 개수를 세기 위한 스택)
  ')'로 시작하는 경우 바로 직전 문자에 따라 2가지 처리를 진행
      직전 문자가 '(' 인 경우, 레이저가 발사되는 지점 이다. stack에서 pop을 한 뒤, stack의 길이만큼을 result에 더한다.
        --> pop을 해서 레이저 부분을 제외하고, 쇠막대기부분만 result에 합한다.
      직전 문자가 ')' 인 경우, 맨 위의 쇠막대기가 끝나는 부분이다. stack에서 pop을 한 뒤, result에 1을 더한다.
        --> 맨위에 쇠막대기가 끝나는 쪼가리 1개만 더한다.
    
"""
br=input();stack=[];result=0

for i in range(len(br)):
    if br[i] == '(':
        stack.append(br[i])
        
    else:
        if br[i-1] == '(':
            stack.pop()
            result+=len(stack)
        else:
            stack.pop()
            result+=1
print(result)