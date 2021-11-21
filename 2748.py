# coding: utf-8
"""
난이도 : 1

문제 : n이 주어졌을 때, n 번째 피보나치수 출력

알고리즘 : fib함수내에 초기값 [0,1]을 리스트 fibs에 넣고 입력된 n에 대해 2부터 n까지 반복하며,
            fibs[-1] + fibs[-2]를 fibs에 append한다.
          마지막에 fibs리스트의 마지막 값을 리턴하면, n 번째 피보나치수가 리턴된다.
    
"""
def fib(n):
  fibs = [0,1]
  for i in range(2,n+1):
    fibs.append(fibs[-1] + fibs[-2])
  return fibs[-1]

print(fib(int(input())))