# coding: utf-8
"""
난이도 : 7

문제 : 첫 째줄에 테스트 케이스(T)가 주어지고, 그 다음부터, 
학생수(N)와 1번~N번 학생이 선택한 학생 번호가 한 칸씩 띄어서 입력된다. -> 이런게 총 T번 입력됨.
1번 학생부터 N번 학생이 선택한 학생을 방향그래프로 치환했을때, 사이클에 포함되지 않는 학생 수를 출력하시오.

알고리즘 : 각 테스트 케이스에 대해,
인덱스와 학생 번호를 맞춰 주기위해, 입력받은 학생 번호에서 1을 빼준다. (인덱스는 0부터 N-1 선택한 학생 번호도 0 ~ N-1 이 된다.)
각 학생을 정점으로 치환하여 방향그래프라고 생각하자.
for 문을 돌며 각 정점별로 사이클이 만들어지는지 dfs 함수에서 확인한다. 
-> dfs 함수
    각 정점에서 시작하면 빈 집합 visited를 생성하고, 전체 그래프에서 어디어디 방문했는지를 표시하는 tt_visited가 있다. (한 그래프에 대해 tt_visited는 한번 정의한다.)
    dft 함수내에서
    현재 정점(cur)이 tt_visited에 있다는 것은, 과거에 dfs 순회했던 적이 있는 점에 도달했다는 뜻이므로, 여기서 dfs 재귀를 종료한다.(굳이 순회하지 않아도 이미 했던 곳.)
    다음 정점(nex)이 visited에 있다는 것은, 현재 dfs순회에 있어서 사이클이 형성되었다는 것을 의미한다.
        사이클이 발견되었으므로, 다음에 발견될될 정점(nex)를 사이클의 시작점(cycle_start)으로 보고 team에 1을 더한뒤 백트래킹을 하면서,
        현재 정점(cur)이 시작 정점(cycle_start)가 될때까지 team에 1을 더한다.
        (사이클이 발견되었을때, 다음에 발견될 정점을 시작점으로 보기때문에 백트래킹 전에 team에 1을 더해준다.)
        백트래킹을 진행하다, 현재 정점(cur)이 사이클의 시작정점(cycle_start)이 되면, 백트래킹을 종료하고 dfs는 종료되며

    다음 사이클이 있는지 for문에서 또 검증하게 된다. (없다면 for문이 종료됨.) -> for start, end in enumerate(students): 

    최종적으로 전체 학생수(N)에서 사이클을 형성하는 학생수(team)을 빼서 출력한다.
    
"""

import sys
sys.setrecursionlimit(10**8)

def dfs(cur, nex, visited, tt_visited):
    if cur in tt_visited: # DFS End
        return True, None
    visited.add(cur)
    tt_visited.add(cur)
    
    if nex in visited: # cycle
        global team
        team += 1
        return (cur == nex), nex
    
    is_cycle, cycle_start = dfs(nex, students[nex], visited, tt_visited)
    if is_cycle == False:
        team += 1
        if cur == cycle_start:
            is_cycle = True
    return is_cycle, cycle_start

T=int(sys.stdin.readline())
for i in range(T):
    N=int(sys.stdin.readline())
    students = list(map(lambda x:int(x)-1,sys.stdin.readline().split()))
    team = 0
    tt_visited = set()
    
    for start, end in enumerate(students):
        if start in tt_visited:
            continue
        dfs(start, end, set(), tt_visited)
    print(N-team)