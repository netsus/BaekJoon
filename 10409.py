
# coding: utf-8

# In[21]:


"""
난이도 : 3

문제 : 정수로 n(일의 개수), T(총 시간)가 주어지고, 다음줄에 n개의 시간(처리되는데 걸리는 시간)이 주어진다.
    FCFS(First Come First Served)규칙이 적용될때 주어진 시간 T 안에 몇개의 일이 처리되는지 출력하시오.

알고리즘 : 함수 FCFS_process는 n,T, num_li(n개의 시간)이 입력된다.
    처리되는 순서이자 일의 개수는 order에 저장되고, 처리됨에 따라 걸리는 시간은 score에 저장된다.
    score가 T 이하이고, 처리되는 일의 개수(order)가 n개보다 작은 동안 while문이 반복된다.
        일이 하나씩 처리될때 마다. score에 시간이 더해지고, 더해진 score가 T 이하일때 order에 1이 더해진다
    if문을 이용해 
        마지막일까지 모두 진행된 경우에 마지막 일때문에 T를 초과하는 경우를 예외처리 하였다.
    그외의 경우
        order를 출력해주면 된다.
    
"""
def FCFS_process(n,T,num_li):
    score=0;order=0
    while score <= T and order < len(num_li):
        score += num_li[order]
        if score <= T:
            order += 1
    if order == len(num_li) and sum(num_li) > T :
        print(order-1)
    else:
        print(order)
        
n,T = map(int,input().split())
num_li = list(map(int,input().split()))
FCFS_process(n,T,num_li)

