# coding: utf-8
"""
난이도 : 6

문제 : 첫줄에 숫자 N과 K가 주어진다. 1 ~ N 까지 수열이 있을때, 1부터 N까지 동그랗게 있다고 했을 때, 모든 수가 출력될 때 까지 K번째 수를 출력.
       예를들어 1 부터 7 까지 있을때, K가 3이면, 3 출력하고 6출력하고 7하고 다시 1, 2해서 2출력하는 식으로 출력한다. -> 3, 6, 2, 7, 5, 1, 4

알고리즘 : 1 부터 N까지 자연수 리스트를 만들어서 arr에 저장한다. 
           K-1을 초기 pop_idx(리스트에서 뺄 값의 인덱스)에 할당한다.
           for문을 N번 돌면서,
              pop_idx가 arr의 길이 이상일 때, pop_idx를 len(arr)로 나눈 나머지를 pop_idx에 넣는다. (값을 빼다보면 리스트 한바퀴 다 돈 뒤에 뺄 인덱스를 결정하기 위한 것.)
           arr에서 pop_idx번쨰를 빼서 결과로 출력할 리스트(result)에 append한다.
           pop_idx에 K-1(윗줄에서 하나를 뺐으니 K에서 1을 뺀 것)을 더한다. -> 위의 for문 반복

즉, arr에서 pop_idx를 계속 빼내어 result에 추가하는데, 한번 뺼때 마다 pop_idx는 K-1씩 더해진다.
특이한 점은, arr를 한바퀴 다 돌았을 때, 다음에 뺄 인덱스를 결정하는 조건문인데, pop_idx가 len(arr) 이상인 경우 
arr에서 pop_idx는 index out of range 이므로, pop_idx에 pop_idx를 len(arr)로 나눈 나머지가 되야 arr에서 해당 번째의 index를 뺄 수 있기 때문이다.
"""

N,K = map(int,input().split())
arr = [i for i in range(1,N+1)]

result=[]
pop_idx = K-1

for i in range(N):
    if pop_idx >= len(arr):
        pop_idx = pop_idx % len(arr)
    result.append(str(arr.pop(pop_idx)))
    pop_idx += K-1
print('<'+', '.join(result)+'>')