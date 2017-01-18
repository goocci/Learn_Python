'''
[ 변수의 스코프(scope) ]
 사용자가 정의한 함수안에서 선언된 변수는 그 함수 밖에서는
 사용될 수 없다. 즉, 그변수의 범위는 함수 안에서만 유효하다.
 이경우 그 함수의 지역(local, 로컬)을 변수의 스코프(범위, scope)라 한다.
 함수내에서 선언된 변수를 지역변수(로컬변수)라고 한다.
'''

# 지역변수 선언 예
a = 20 # 전역변수 : 여기서 선언된 변수 a는 프로그램이 종료 될때까지 유효하다.

def func(a) :
    print("전역 변수", a)
    a = 10 # 지역변수
    print("지역 변수", a)

func(a) # 전역변수를 인자로

def func1(b) :
    b += 1
    print(b)

func1(30) # b = 30 : 함수의 인자로 들어가면서 인수 b = 30은 지역변수

# 전역변수 선언(global문으로 선언)
aa = 10

def aa_func(aa):
    aa = aa+1
    return aa

aa = aa_func(aa) #함수 밖에서 선언된 변수의 값을 변경시키는 예(return문을 사용)

print(aa)

bb = 100

def bb_func():
    global bb # global은 함수안에서 함수밖의 변수를 직접 사용하겠다라는 의미
    bb = bb+1

bb_func()
print(bb)

# 될수 있으면 global문은 사용하지 않는 것이 바람직하다.
# global문을 사용하는 것보다는 return문을 이용해서 사용하는 것이 좋다.