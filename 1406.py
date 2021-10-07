# coding: utf-8
"""
난이도 : 7

문제 : 문자열이 주어지고, 입력될 명령어 개수(n)이 주어진다.
이 때, 명령어 별로 아래 기능이 수행되며, 에디터처럼 역할을 하면 된다.
처음에 주어진 문자열의 맨 오른쪽에 커서가 존재한다.
 1) L : 커서 왼쪽으로 한칸 이동 (맨 왼쪽이면 유지)
 2) D : 커서 오른쪽으로 한칸 이동 (맨 오른쪽이면 유지)
 3) B : 커서 왼쪽 문자 삭제 (맨 왼쪽이면 아무일도 안함)
 4) P 문자 : 대문자 P 뒤에 오는 문자를 커서 왼쪽에 추가

알고리즘 : 주어진 문자열을 리스트로 만들어 stk_l(스택 left)에 할당하고, stk_r(스택 right)라는 빈 리스트를 생성합니다.

--> bottom-왼쪽 스택-top (커서) top-오른쪽 스택-bottom 이런 모양으로 스택 2개를 만들어 커서는 중간에 있다고 상상하자.

 1) L : 커서가 왼쪽으로 이동할 때는 왼쪽 스택(stk_l)에서 pop하여 오른쪽 스택(stk_r)에 넣는 작업을 합니다. (stk_l의 길이가 0이면 유지)
 2) D : 커서가 오른쪽으로 이동할 때는 오른쪽 스택(stk_r)에서 pop하여 왼쪽 스택(stk_l)에 넣음. (stk_r의 길이가 0이면 유지)
 3) B : 커서 왼쪽문자 삭제는 stk_l를 그냥 pop 한다. (stk_l의 길이가 0이면 pop할께 없으므로 유지 - 커서가 맨 왼쪽에 있다는 뜻)
 4) P 문자 : 문자를 커서 왼쪽에 추가하는 것은 stk_l에 append하는 것.

최종 적으로는 stk_l와 stk_r의 reverse형태를 합쳐서 문자열로 출력
"""
from sys import stdin
stk_l = list(stdin.readline().strip())
stk_r = []
n=int(stdin.readline())
for i in range(n):
    cmd=stdin.readline().strip()
    if cmd.startswith('P'):
        stk_l.append(cmd.split()[-1])
    elif cmd == "L" and len(stk_l) != 0:
        stk_r.append(stk_l.pop())
    elif cmd == "B" and len(stk_l) != 0:
        stk_l.pop()
    elif cmd == "D" and len(stk_r) != 0:
        stk_l.append(stk_r.pop())
print(''.join(stk_l + stk_r[::-1]))