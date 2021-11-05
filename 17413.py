# coding: utf-8
"""
난이도 : 5.5

문제 : 주어진 문자열에 대해 단어(숫자 or 알파벳 소문자)만 뒤집기. 단어는 공백을 구분자로 구분한다.
(단, '<' 특수문자가 나오면 반드시 '>'가 뒤에 나오며 그 사이의 문자는 태그이름으로 간주되어 뒤집지 않는다.)

알고리즘 : 주어진 문자열을 list()를 사용하여 리스트로 만든다.
while문을 이용하여 리스트의 인덱스를 순차적으로 돈다.
  1. '<'로 시작하는 경우 '>'로 끝날때까지 인덱스++
  2. isalnum()을 통해 문자가 영어소문자거나 숫자인경우 start에 인덱스를 넣는다.
    --> 그 뒤로, i(인덱스)가 len(arr)보다 작고 arr[i]가 isalnum가 참인경우계속 i+=1진행
    끝나면 end=i (이때, i는 isalnum이 아닌 첫 문자열이다) arr[start:end]까지를 뒤집으면 딱 end 앞의 문자열까지 뒤집어 진다.
  3. else --> <,>도 아니고, 문자나 숫자도 아닌 경우 -> 공백인 경우 i+=1해준다.



(참조 : https://hongcoding.tistory.com/62)
    
"""
arr = list(input())

i=0
start=0

while i < len(arr): # while문을 이용하여 리스트의 인덱스를 순차적으로 돈다.
    if arr[i] == '<': # '<'로 시작하는 경우 
        while arr[i] != '>': # '>'로 끝날때까지 인덱스++
            i+=1
    if arr[i].isalnum(): # isalnum()을 통해 문자가 영어소문자거나 숫자인경우 
        start=i    # start에 인덱스 넣기
        while i < len(arr) and arr[i].isalnum():
            i+=1
        end=i # 끝나면 end=i (이때, i는 isalnum이 아닌 첫 문자열이다)
        # arr[start:end]까지를 뒤집으면 딱 end 앞의 문자열까지 뒤집어 진다.
        arr[start:end] = arr[start:end][::-1]
    else:
        i+=1

print("".join(arr))