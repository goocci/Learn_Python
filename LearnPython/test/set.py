'''
집합(sets) : set()
'''

ss = set(['a', 'b', 'c'])
print(ss)

ss = set([1,2,3])
print(ss)

ss = set("Good Morning")
print(ss)

# 집합의 특징 :  - 중복을 허용하지 않는다.(중복을 제거하기위한 필터로 활용되기 한다.)
#                - 순서가 없다.
# 리스트 튜플은 순서가 있다. 따라서 인덱싱을 이용하여 값을 얻어올 수 있다.
# 집합은 순서가 없기 때문에 인덱싱으로 값을 얻어올 수 없다. 딕셔너리 역시 순서가 없는 자료형이다.
# 집합과 딕셔너리는 인덱싱을 지원하지 않는다.
# 집합에 저장된 값을 인덱싱으로 접근하기 위해서는 리스트나 튜플로 변환해야한다.

ss1 = set(['a','b','c'])
list = list(ss1) # 순서가 없기 때문에 실행할 때 마다 변환되는 리스트가 다름...
print(list)
print(list[2])

# 교집합, 합집합, 차집합
s1 = set([1,2,3,4,5,6,7])
s2 = set([3,5,6,8,9])

print(s1 & s2) # 교집합 : &
print(s1.intersection(s2)) # 교집합 : intersection()

print(s1 | s2) # 합집합 : |
print(s1.union(s2)) # 합집합 : union()

print(s1 - s2) # 차집합 : -
print(s1.difference(s2)) # 차집합 : difference()

# 집합에서 값 추가
s1 = set([1,2,3])
s1.add(100) # 한개의 값 추가 : add()
print(s1)

s1 = set([1,2,3,4])
s1.update([10,100,1000]) # 여러개의 값 추가 : update()
print(s1)

# 집합에서 값 제거
s1 = set([1,2,3,4,5])
s1.remove(4)
print(s1)

# 대칭 차집합 : (^) 두개의 집합이 있을 때 둘 중 한집합에만 있는 항목들
s = set("Good Morning")
t = set("Good Night")
print(s^t)

s.remove('g')
# s.remove('h') # 지정 항목이 없으면 에러
s.discard('h') # 집합에서 항목을 제거. 집합내에 없는 항목을 제거 할때는 에러 발생 안한다.
s.discard("G")

# 갯수
length = len(s)
print(length)

print(s)
# 집합 모든 항목 제거
s.clear()
print(s)