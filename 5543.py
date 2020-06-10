# coding: utf-8
"""
난이도 : 1.5

문제 : 숫자 5개가 주어진다. 처음 3수는 버거가격, 마지막 2수는 음료 가격이다. 버거와 음료 같이 사는경우 세트가 적용되어 50원할인 된다.
가장 저렴한 세트가격은?

알고리즘 : 사실 버거중 제일 싼것 + 음료중 제일 싼것 - 50 이 정답이다.
리스트 컴프리핸션으로 버거가격을 리스트로 받고 -> buger
음료 가격도 리스트로 받는다 -> soda
buger의 최소값 + soda의 최소값 - 50 이 가장 저렴한 세트 가격이다.
    
"""
buger = [int(input()) for i in range(3)]
soda = [int(input()) for i in range(2)]
print(min(buger)+min(soda)-50)