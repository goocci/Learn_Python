# 함수
'''
[ 문자열 함수 ]
문자열 포맷팅 함수 : format()
'''
# {n}은 자리 표시자, n은 format()에 지정된 위치(인덱스) 표시
print("you've {0} a friend".format("got"))

str = "{2} {0} {1}".format("a", 100, 200)

print(str)

number = 100
day = "sunday"

print("오늘은 우리가 사귄지 {0}일이야. 요일은 {1}".format(number, day))

# 인덱스와 이름을 혼용해서 사용
print("오늘은 우리가 사귄지 {0}일, 요인은{day}".format(300, day="Sunday"))

# 좌측 정렬
name = "홍길동"
print("{0:<10}".format(name))
# 우측 정렬
print("{0:>10}".format(name))
# 가운데 정렬
print("{0:^10}".format(name))
print("{0:-^20}".format(name)) # 빈공간을 '-'로 채움.

# 소문자를 대문자로 바꾸는 함수
aa = "hello"
aa1 = aa.upper()
print(aa1)

# 대문자를 소문자로 바꾸는 함수
aa2 = aa1.lower()
print(aa2)

# 문자 갯수를 리턴하는 함수
aa = "abcdaa"
cnt = aa.count('a')
print(cnt)

# 문자열의 길이를 구하는 함수
cnt = len(aa)
print(cnt)

# 문자 위치 찾기 함수 : 문자열에서 찾고자하는 문자의 첫번째 위치를 리턴하는 함수
bb = "abcdabcd"
loc = bb.find('c') # 찾고자 하는 문자가 없는 경우에는 -1을 반환한다.
print(loc)
'''
loc = bb.index("c")  #index 함수는 find 함수와는 다르게 찾고자 하는 문자가 없을 경우 에러가 난다.
print(loc)
'''

# 공백지우기 함수 (lstrip, strip, rstrip)
aa = "     very     good     "
print(aa.lstrip() + "morning") # 좌측 공백 제거
print(aa.rstrip() + "morning") # 우측 공백 제거
print(aa.strip() + "morning") # 양측 공백 제거

# 문자열 대체 함수 (replace) :  문자열 내의 특정한 값(문자, 문자열)을 다른 값으로 교체.
aa = "good morning kim"
bb = aa.replace("morning", "night")
print(bb)

# 문자열 나누기(split)
str = "good morning kim"
str_split = str.split() # split()괄호안에 값이 없으면 공백을 기준으로 문자열을 나눈다.
print(str_split)

str = "홍길동/27/서울시 광진구/010-1234-5678"
str_split = str.split('/') # '/'를 구분자로 문자열을 나눈다. 그 결과는 리스트에 저장된다.
print(str_split)