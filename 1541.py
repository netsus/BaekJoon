# coding: utf-8
"""
난이도 : 3

문제 : 첫째 줄에 식이 주어진다. 식은 ‘0’~‘9’, ‘+’, 그리고 ‘-’만으로 이루어져 있고, 가장 처음과 마지막 문자는 숫자이다. 
그리고 연속해서 두 개 이상의 연산자가 나타나지 않는다. 수는 0으로 시작할 수 있다. 괄호를 적절히 쳐서 이 식의 값을 최소로하여 출력하시오.

알고리즘 : +와 -로 이루어진 연산에서, 결과를 최소로만들기 위해선, - 를 split해서 그 안의 모든 수를 + 연산한 뒤, - 연산하면 됩니다. 
왜냐하면, -를 기준으로 그 사이값들은 모두 +연산으로 되어있을 것이고, 그것들을 모두 더하면 (숫자들의합)-(숫자들의합)-(숫자들의합) 꼴이 되어, 
- 이후의 숫자들이 모두 최대가 되면서 가장 작은 수가 될것이기 때문입니다.
    
"""

## 일반 풀이
sik_minus = input().split('-') # 55-50+40 => [55, 50+40]
sik_plus = [] #[55, 90]
for i in sik_minus: 
    count = 0 
    i = i.split('+') #[55], [50,40]
    for j in i:
        count += int(j) # 1. 55    2. 50+40 
    sik_plus.append(count) 
result = sik_plus[0]
for i in range(1, len(sik_plus)):
    result -= sik_plus[i]
print(result) # -35

##숏코딩1
sik_minus = input().split('-')
sik_plus = list(map(lambda x: sum(map(int,x.split('+'))),sik_minus))
print(sik_plus[0]-sum(sik_plus[1:]))


##숏코딩2
f,*o=[sum(map(int,t.split('+'))) for t in input().split('-')]
print(f-sum(o))