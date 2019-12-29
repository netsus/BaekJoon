
# coding: utf-8

# In[40]:


"""
난이도 : 3

문제 : 1부터 10000사이의 자연수 N이 주어진다.
    자연수 중에서 6을 연속으로 3개이상 포함하는 수 중에 N번째 수를 출력.

알고리즘 : 666부터 시작하여 1씩 더해가면서, 수를 문자열로바꾼뒤 '666'을 1개 이상 포함하면 하나씩 카운트한다.
        입력받은 N과 카운트수가 일치하는 수를 출력한다.
"""
def Brute_force(N):
    cnt=666
    s=0
    while 1:
        if str(cnt).count('666') >= 1:
            s+=1
            if s==N:
                print(cnt)
                break
        cnt+=1

N = int(input())
Brute_force(N)

