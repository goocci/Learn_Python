'''
리스트 관려 함수들
'''

# 리스트에 값을 추가하는 함수 : 끝에 추가

list = [10, 100, 1000]
list.append(11)
print(list)
list.append("abc")
print(list)
list.append(['a','b'])
print(list)

# 리스트 정렬 함수
list = [4.5, 10, 3.3]
list.sort()
print(list)

list = ['b', 'd', 'a', 'c']
list.sort() # 기본적으로 오름차순 정렬
print(list)

# 리스트 뒤집기 함수
list.reverse() # sort()함수를 적용 후 reverse()를 사용하면 내림차순 정렬이 된다.
print(list)

list = ['c', 'a', 'd', 'b']
list.reverse()
print(list)

# 요소의 위치를 반환하는 함수
list = ['c', 'a', 'd', 'b']
aa = list.index('a')
print(aa)

# 요소를 삽입하는 함수
aa = [1,2,3,4]
aa.insert(2, 'a') # append함수는 무조건 제일 뒤에 추가시키지만, insert 함수는 원하는 위치에 추가 시킬수 있다.
print(aa)

# 요소를 제거하는 함수
cc = [1,2,3,1,2,3]
cc.remove(3) # 지우고자 하는 값이 여러개일 경우에는 첫번째 값을 제거한다.
cc.remove(3)
print(cc)

# 특정 요소값을 끄집어 내는 함수
dd = [1,2,3,'a',1,2,'b',3]
aa = dd.pop() # ()안에 값이 없을 경우에는 리스트상의 마지막 값을 꺼내온다.
print(dd) # 끄집어낸 요소는 리스트에서 삭제를 한다.
print(aa)

bb = dd.pop(3) # ()안에 값은 위치값(인덱스)
print(bb)

# 요소의 갯수를 파악하는 함수
dd = [1,'a',3,'a',1,2,'b',3]
cnt = dd.count('a') # count(요소값) 요소의 갯수를 구하는 함수
print(cnt)

# 리스트 확장 함수
a = [1,2,3]
a.extend([1,2,3,4,5])
print(a)

a = [1,2,3]
a += [1,2,3,4] # a = a + [1,2,3,4], *= (a*=1 --> a=a*1), -= (b-=1---> b=b-1)
print(a)