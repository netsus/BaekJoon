# coding: utf-8
"""
난이도 : 1

문제 : 5개의 숫자들이 빈칸을 사이에 두고 하나씩 주어진다.

알고리즘 : 5가지 숫자를 제곱해서 더 한뒤에 10으로 나눈 나머지 출력
    
"""

li=map(int,input().split()) # 5가지 숫자를 리스트형태로 받아서, li에 저장
print(sum(map(lambda x: x**2,li))%10) # li에 각 인자를 제곱해서 더한 뒤, 10으로 나누기

# 위의 풀이 숏코딩으로
print(sum(map(lambda x: x**2,map(int,input().split())))%10)