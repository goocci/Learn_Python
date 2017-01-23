''' 기본 내장 함수들'''

# eval(expression) : 값을 구함
x = 10
print(eval("x+10"))

# exec(obj) : 파이썬 명령을 실행
a = 100
exec("b=a+100")
print(b)

# chr(num) : 아스키코드 값을 문자로 반환
print(chr(97))
print(chr(66))

# ord(str) : 한 문자의 아스키코드 값을 반환
print((ord('a')))
print(ord('A'))

# hex(num) : 16진수로 변환(문자열로)
print(hex(100))
# oct(num) : 8진수
# bin(num) : 2진수

# id(obj) : 객체의 고유번호 반환
aa = 10
print(id(10))
print(id(aa))
bb = aa
print(id(bb))

# isinstance(class, classinfo) : class가 classinfo의 서브 클래스 일 때 True 반환
class Person: pass
student = Person()
print(isinstance(student, Person))
professor = 100
print(isinstance(professor, Person))

""" iterable : 반복 가능한 자료형 or sequence 자료형? (문자열, 리스트, 튜플, 딕셔너리, 집합) """

# list(iterable) : 리스트로 반환
print(list((1,2,3,4)))
aa = [1,4,5]
cc = list(aa) # list()는 aa의 리스트를 복사해서 cc에 대입 : aa와 cc는 다른 리스트 객체
print(cc)
print(id(aa))
print(id(cc))

# len(seq) : 길이 반환
print(len("Hello World"))
print(len([1,2,3,4,5]))
print(len(('a','b')))

# sorted(iterable[,key][,reverse]) : 정렬된 리스트를 반환
print(sorted([5,3,1,2,4]))
print(sorted(['c','e','a','f']))
print(sorted("alphabet"))

# sort() : 객체 그 자체 내에서 정렬시켜줌(반환X)
bb = [4,3,1,2,5]
print(bb.sort()) # None
print(bb) # 정렬된 bb 출력

# map(func, iterable) : iterable의 각 요소를 func()의 반환값으로 매핑해서 iterater로 반환
def map_test2(a):
    return a*3

print(list(map(map_test2, [100,200,300])))

# map() 사용 안하면...
def map_test(li):
    res = []
    for i in li:
        res.append(i*3)
    return res

res = map_test([10,20,30,40])
print(res)

"""
** lambda : 함수를 생성할 때 사용하는 예약어 def 와 동일한 기능의 예약어이다.
			보통 '한줄'로 간결하게 함수를 만들어 사용할 때 사용한다.
            (def 를 사용할 수 없는 곳에서 사용한다)

** 사용 형식
	lambda 인수1, 인수2,.... : 인수를 이용한 표현식
"""
# lambda 사용
print(list(map(lambda x: x*3, [1,2,3])))

sss = lambda x, y: x*y ### sss라는 함수를 만듬
print(sss(10,20))
# or
def sss(x, y):
    return x*y
print(sss(30,40))
# def 를 사용할 수 없는 곳
li = [lambda x,y:x*y, lambda x,y:x/y]
print(li[0](10,5))

# enumerate(iterable, start=0) : (인덱스:해당값) 튜플 형태로 변환
seasons = ["spring", "summer", "fall", "winter"]
print(list(enumerate(seasons)))          # [(0, 'spring'), (1, 'summer'), (2, 'fall'), (3, 'winter')]
print(list(enumerate(seasons, start=2))) # [(2, 'spring'), (3, 'summer'), (4, 'fall'), (5, 'winter')]

for i,j in enumerate(seasons):
    print("%s%s" %(i,j))

# filter(func, iterable) : iterable의 각 요소 중 func()의 반환값이 참인 것만을 묶어서 iterater로 반환
def positive(x): return x>0

print(list(filter(positive, [1,-12,4,0,-3,7,9,-1])))
print(list(filter(lambda x: x>0, [3,-8,4,0,3,7,9,-1]))) # lambda 사용

# filter() 사용 안하면...
def positive(li):
    res = []
    for i in li:
        if i > 0: # 양수의 값만 출력
            res.append(i)
    return res

print(positive([1,-12,3,0,-3,7]))

# pow(x, y [,z]) : 거듭제곱을 구한다. pow(x,y)는 x**y와 같다

# divmod(a,b) : a를 b로 나눈 (몫, 나머지)를 구한다. 튜플 반환
print(divmod(7,4))

# all(iterable) : iterable의 모든 요소가 True일 경우 True를 반환
print(all([1,2,3]))
print(all([1,2,3,4,0]))
# any(iterable) : iterable의 하나 이상의 요소가 True일 경우 True를 반환
print(any([1,2,3,4]))
print(any([1,2,0]))
print(any([0," "]))
print(any([0,""]))

# max(iterable or 인자들) : iterable 중 최대값 반환
print(max([1,2,3,5,4]))
print(max("Hello")) # 아스키코드 값으로 판단
print(max(1,2,3,8,4,5))
# min()도 비슷

# repr() : eval() 함수로 다시 객체를 복원할 수 있는 문자열 생성 !! str()과 차이점이 있음
print(repr("hi".upper()))
print(eval(repr("hi".upper())))