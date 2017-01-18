'''
사용자 정의 함수

def 함수명(인수):
	  <실행할 명령1>
	  <실행할 명령2>
	  ...

  *인수(매개변수, 파라미터)

'''

def show_max(a, b) :
    if a > b :
        print("최댓값", a)
    elif a == b :
        print(a,"와",b,"는 같다")
    else :
        print("최댓값",b)

show_max(10, 6)

i = 5
j = 5
show_max(i,j)

i = 10
j = 100
show_max(i,j)

def sum(a,b) :
    return a+b

a = 10
b = 15
d = sum(a,b)
print(d)

def sum(a,b,c):
	return a+b+c

c = sum(10, 20, 30)
print(c)
# sum 함수는 두개의 인자(a,b)를 통해서 입력을 받는다. 서로 더한 값을 돌려주는 함수이다.
# 돌려주는 값(리턴 값)을 받기 위해서는 받을 변수 필요하다.
# 리턴값을 받을 변수 = 함수명(인수1, 인수2, ...)

'''
** 일반적인 함수의 구조

   def 함수명(인수,...) :
	<실행할 명령>
	.....
	return 값
'''

# 인수가 없는 함수(입력값이 없는 함수)
def show():
	return "Hello"

aa = show()
print(aa)

# 인수도 없고 리턴값도 없는 함수
def show():
	print("안녕하세요")

show()

# 예상할 수 없는 인수를 갖는 함수
# def 함수명(*인수)
def sum(*a) : # 일종의 리스트 형태??★
    total = 0
    for i in a :
        total += i
    return total

result = sum(10,20,30)
print(result)

def cal(aa, *a) :
    if aa == "sum" :
        tot = 0
        for i in a :
            tot += i
    elif aa == "mul" :
        tot = 1
        for i in a :
            tot *= i

    return tot

res = cal("sum", 1,2,3)
print(res)
res = cal("mul", 4,5,6)
print(res)

# 리턴값의 유형
def return_value(a,b) :
    return a+b, a-b # 튜플형태로 두개 이상의 리턴값 가져올 수 있다.

a = return_value(1,2)
print(a)

# 리턴만 단독으로 사용할 경우에는 함수를 바로 빠져 나간다.
def show(aa) :
    if aa == 0:
        return # 함수 빠져나감
    else :
        print("0이 아니다")

show(0)

# 인수에 초기값 설정 : ★초기화 하고자 하는 인수는 마지막에 설정!!!
def show(name, age, gender="M") :
    print("이름:", name)
    print("나이:", age)
    if gender == "M" :
        print("남자")
    else :
        print("여자")

show("김민구","27") # 인자값을 주지 않아도 함수에서 인수의 초기값이 있어서 가능
show("홍길동","22","Q")