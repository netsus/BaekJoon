# coding: utf-8
"""
난이도 : 2

문제 : 문자열 뒤집어 출력

알고리즘 : 처음 숫자 입력받은 만큼 반복하며, 입력받은 문자열을 split(공백 구분)하고 각 단어별로 뒤집어서([::-1] 사용),
         ' '.join()으로 문자열로 만들어 출력
    
"""

## 내 풀이
for _ in range(int(input())):
    print(' '.join([i[::-1] for i in input().split()]))

## 다른 사람 숏 코딩
exec('print(*input()[::-1].split()[::-1]);'*int(input()))

"""
해석: int(input())만큼 반복하며, print로된 부분을 exec로 실행한다.
'print(*input()[::-1].split()[::-1]);'
--> 입력받은 문자열을 그대로 뒤집어서 split하여 리스트로 만든다. (ex] 'ab cd' -> ['dc', 'ba'])
그 후, 다시 뒤집는다. (ex] ['dc', 'ba'] -> ['ba', 'dc'] )
그 후, *을 이용해 unpacking 하여 출력한다.
"""