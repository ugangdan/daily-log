#전지전능하신 마법의 소라고둥님
from random import *

#random() * 8 0~8까지의 랜덤 숫자
#random() * 8 +1 1~8까지의 랜덤숫자
#int 붙이면 정수처리
#randrange(1, 8) 1부터 8까지의 랜덤 숫자 (8포함X)
#randint(1, 8) 1부터 8까지의 랜덤숫자 

print("???: 아브라카다브라~ 전지전능하신 마법의 소라고둥님이시어 부디 제 앞에 나타나 저에게 진실을 알려주소서.")
print()
print("마법의 소라고둥: 크허억! 너냐 날 여기로 부른 자가")
print()
print("???: 네 접니다. 마법의 소라고둥님 제 시험점수를 알려주세요.")
print()
print("마법의 소라고둥: 흠흠 어디보자 너의 시험점수는 ",int(random() * 100) + 1, "점이다.")
print()
print("???: 그렇군요 한개만 더 질문할게요. 제가 이번년도에 연애를 할 수 있을까요?")
print()
print("마법의 소라고둥: 너가 이번년도에 연애를 할 확률은",randrange(0, 101), "%다.")
