'''
** while문

while <조건문>:
	<실행할 명령문 1>
	<실행할 명령문 2>
	<실행할 명령문 3>
	.....

'''

aa = 0

while aa < 10 :
    aa = aa + 1
    print("aa = %d" %aa)
    if aa == 10 :
        print("종료")

'''
무한루프
while 1:
	<실행할 명령문1>
	<실행할 명령문2>
	.....
'''

# 보조 제어문 (break, continue)
m = 100
n = 10

while m:        # 숫자는 0이 아니면 무조건 true
    n = n - 1
    print("현재 %d 입니다" %n)

    if not n :
        print("n의 값은 0 입니다")
        break # while 빠져나감

# 1에서 부터 10까지의 정수중 홀수를 출력하는 코드
i = 0
while i < 10 :
    i = i + 1
    if i % 2 == 0 : continue # continue는 while문의 맨처음 (i<10)으로 돌아가게하는 명령문
    else : print(i)