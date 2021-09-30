
# coding: utf-8

# In[38]:


"""
2231 분해합

난이도 : 2.5

문제 : 주어진 수 N 에 대하여, 임의의 수 M과 M을 이루는 한자리 수를 모두 더한 것이 N이 될때,
    M을 N의 생성자라한다. 생성자가 없으면 0출력, 생성자가 여러개이면 최소값출력, 생성자가 1개면 그거 출력
    (단, 모두 자연수)

알고리즘 : make_M 함수는 수(n)을 입력받아, n + n을 이루는 한자리수 모두 합을 반환. 즉, 분해합을 반환한다.
    find_least_M 함수는 입력받은 수 N에 대하여, 브루트 포스 탐색할 수의 범위를 결정한다.
    (수의 범위는 첫쨰자리수 + 나머지자리수*9 로 했다. 이유는 항상 최소의 생성자가 포함될 수 있도록)
    최소 생성자를 찾는 경우 (if make_M(i)==num이 성립한 경우) 생성자를 출력한다.
    flag를 이용하여 생성자가 없을때는 0을 출력한다.

"""
def make_M(n):
    M = n + sum(list(map(int,' '.join(str(n)).split())))
    return M

def find_least_M(N):
    num = int(N)
    num_range = int(N[0]) + len(N[1:])*9
    num_start = num - num_range
    flag=0
    for i in range(num_start,num+1):
        if make_M(i)==num:
            print(i)
            flag=1
            break
    if flag==0:
        print(0)
    return None
        
N = input()
find_least_M(N)

