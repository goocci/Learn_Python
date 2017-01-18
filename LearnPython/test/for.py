'''

for 변수 in 리스트(튜플, 문자열):
	 <실행할 문장1>
	 <실행할 문장2>
	 ...

'''

list1 = ["a", "b", "c"]

for i in list1 :
    print(i)

jumsu = [90, 40, 30, 70, 80] # 1번부터 5번 학생의 시험점수

number = 0

for i in jumsu :
    number = number + 1
    if i >= 60 : print("%d번 학생의 점수 %d 합격" %(number, i))
    else : print("%d번 학생의 점수 %d 불합격" %(number, i))

# continue 사용
number = 0
for i in jumsu:
    number = number +1
    if i < 60: continue
    print ("%d 번 학생 합격입니다" % number)

aa = [('a', 'b'), ('c', 'd'), ('e', 'f')]
for (i, j) in aa :
    print(i+j)

''' for문과 range 함수

 - range 함수는 두개, 세개의 숫자를 이용하는 함수이다.
   숫자가 두개인 경우 1씩 증가하는 숫자의 리스트를 반환한다.
   숫자가 세개인 경우 세번 째 숫자는 증가치를 의미한다.

   사용예> range(1,5) ---> 리스트 [1,2,3,4] 반환한다.
              range(1,5,2) ---> [1,3] //2씩 증가 시킨다.
			  ** 주의: 두번째 숫자 이하가 아니라 미만★ 까지만 반환을 한다.
'''

for i in range(1,5) :
    print(i)
else : # 반복문에서 else절은 루프를 다 돌고 난 뒤에 항상 실행됨. break문을 사용한 경우에는 실행 안됨.
    print("반복문 종료")

'''
   자바에서 for(int i = 0; i < 5; i++) 과
   같이 파이썬에서 표현을 한다면
   for i in range(0,5)와 같이 표기할 수 있다.
'''

# range 함수를 이용한 구구단 출력

for i in range(2,10) :
    for j in range(1,10) :
        print("%d * %d = %d" %(i,j,i*j), end=", ")
    print(" ")

# 리스트에 for문을 이용하여 값 담기!!!

aa = [1,2,3,4,5,6,7,8,9]

gugudan_3 = []

for i in aa :
    gugudan_3.append(i*3) # 3단

print(gugudan_3)

gugudan_4 = [i*4 for i in aa]
print(gugudan_4)

# 5단의 결과값 중에서 짝수만 리스트에 추가
gugudan_5 = [i*5 for i in aa if i%2 == 0]
print(gugudan_5)

'''
★리스트 내포(List comprehension)의 기본적인 구조 -> for문으로 리스트에 값담기?

  1) [표현식 for 항목 in 반복가능한 객체 if 조건]
      위에서 if조건은 생략이 가능하다.

  2) [표현식 for 항목1 in 반복가능한객체1 if 조건1
                for 항목2 in 반복가능한객체2 if 조건2
				.....
				for 항목n in 반복가능한객체n if 조건n]
'''
# 구구단의 결과를 저장하는 리스트 구현
gugudan = [i*j for i in range(2,10)
                for j in range(1,10)]
print(gugudan)