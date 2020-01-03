
# coding: utf-8

# In[3]:


"""
난이도 : 2.5

문제 : 처음에 정렬할 수가 몇개인지 주고, 정렬 할 수를 차례대로 모두 '\n'을 구분자로 하나씩 입력받는다.
    수들을 정렬하여 하나씩 출력해야 한다. 즉, N과 N개의 수가 주어졌을때 오름차순 정렬하여 행 구분자로 출력.
    (단, O(nlogn) 시간안에 풀어야 답으로 인정된다.)

알고리즘 : 파이썬에 내장된 sorted 함수를 이용하면 간단하게 풀 수 있다.
    (물론, merge sort를 직접 구현하여 푸는것이 출제의 의도이다.)
    python3는 매우 느리기 때문에, pypy3로 제출해야 정답으로 인정된다.

"""
for i in sorted([int(input()) for x in range(int(input()))]):
    print(i)
