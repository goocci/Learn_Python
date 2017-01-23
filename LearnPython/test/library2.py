'''
pickle 모듈 : 객체 형태를 그대로 유지해서 파일에 저장시키고, 불러올 수 있게 하는 모듈.
                바이너리(2진) 형태로 저장한다.
pickle 을 이용해서 파일에 저장 및 조회할 때는 꼭 바이너리 처리를 해야한다.
(b를 입력해서 바이너리라는 것을 표시)
'''
# 저장할때는 pickle.dump(objet, file),
# 불러올때는 pickle.load(file)

import pickle

listA = ['aaa', 'bbb', 'ccc']
fp = open("list.txt", "wb")

pickle.dump(listA,fp)
fp.close()
fp = open("list.txt", "rb")

listB = pickle.load(fp)
print(listB)

##########################

fp = open("dic.txt", "wb")
data = {1:"Hello", 2:"love"}

pickle.dump(data, fp)
fp.close()
fp = open("dic.txt", "rb")

data2 = pickle.load(fp)
print(data2)

# pickle.dumps(object)  ----> string
# pickle.loads(String) ----> object

class Foo:
    var = "Foo 클래스"

fooString = pickle.dumps(Foo) # 클래스도 저장 가능 : 바이너리 형태로
print(fooString)
pickle.loads(fooString)
print(Foo.var)

print(str(fooString))