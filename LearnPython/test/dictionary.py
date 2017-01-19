'''
딕셔너리
dic = { key1:value1, key2:value2, key3:value3 .... }
'''
a = {1:"Hello!!"}
print(a)

a = {"first":['a','b','c']}
print(a)

sports = {"축구":"박지성", "야구":"이대호", "피겨스케이팅":"김연아"}
print(sports["축구"])
print(sports["피겨스케이팅"])

# 추가
aa = {1:"안녕"}
aa[2] = "하이"
print(aa)
aa["third"] = "헬로"
print(aa)
aa[3] = [1,2,3]
print(aa)
aa["인사"] = "굿모닝"
print(aa)
aa[0] = 0
print(aa)

# 삭제
del aa["인사"]
print(aa)

'''
*** 딕셔너리 사용 주의사항 ***
key값(지수)은 고유한 값이므로 중복되는 값을 설정해 놓으면 안된다.
만약 중복이 된다면 하나만 적용되고 나머지는 제외된다.

키값으로 리스트는 사용 불가. 튜플은 사용 가능.
(키값은 변할 수 없기 때문에...)
'''

# dict() 함수 : 항목(key:value)이 없는 딕셔너리를 생성
aa = dict()
print(aa)

aa["one"] = "첫번째" # 항목 추가
print(aa)

# key 리스트 생성 : keys()
bb = {"name":"홍길동", "phone":"01012345678", "age":"27"}
keyList = bb.keys()
print(keyList) # dict_keys(['name', 'phone', 'age']) 객체

for key in bb.keys() : # 각각의 키값 출력 # dict_keys 객체의 각 요소값을 출력
    print(key)

keyList1 = list(bb.keys()) # 리스트형태로 : list()
print(keyList1) # ['name', 'phone', 'age']

# value 리스트 생성 : values()
valueList = bb.values()
print(valueList) # dict_values(['홍길동', '01012345678', '27']) 객체

# key와 value 한쌍(항목)을 얻기 : items()
item = bb.items()
print(item) # 리턴값은 dict_items객체이다. 이객체의 요소는 튜플로 구성된다.
            # dict_items객체 : [('name', '홍길동'), ('hp', '010-1234-1234'), ('age', 24)]

# key:value 쌍을 모두 삭제 : clear()
# bb.clear()
# print(bb)

# key값을 이용하여 vlaue를 얻어오기 : get()
age = bb.get("age")
print(age)

age = bb["age"] # get()을 이용하지 않는 방법
print(age)

'''
gender = bb['gender'] 이때 키값이 존재하지 않으면 에러가 난다.
print(gender)
'''

# get()는 키값이 존재하지 않을 경우에는 None값을 리턴한다.
gender = bb.get('gender')
print(gender)
print("======= get() 실행후 bb 딕셔너리 ======")
print(bb)

# 딕셔너리내에 키값이 없을 경우 디폴트값을 주는 방법
gender = bb.get("gender", "디폴트값")
print(gender)

# 딕셔너리내에 해당 키가 존재하는지 알아보기
confirm = "gender" in bb
print(confirm) # False
confirm = "name" in bb
print(confirm) # True

# pop() 함수를 이용해서 value값을 가져오기 : 딕셔너리에 항목을 제거한다
m = bb.pop("name")
print(m)
print("========= pop() 실행후 bb 딕셔너리 ========")
print(bb)

bb["name"] = "홍길동"
print(bb)

m = bb.pop("gender", "디폴트값") # 키가 없는 경우에는 디폴트값(생략가능)으로 대체 :pop(키 [,디폴트값])
print(m)

# 딕셔너리의 항목 갯수
length = len(bb)
print(length)