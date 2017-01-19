# 절차(구조적) 지향 프로그래밍 예

showInfo = ""
w_showInfo = ""

def person(name, age) :
    global showInfo
    showInfo += "이름: "+name+", "+"나이: "+age+"\n"

def w_person(name, age) :
    global w_showInfo
    w_showInfo += "이름: "+name+", "+"나이: "+age+"\n"

person("김민구","27")
person("홍길동","22")
w_person("김태희","21")
print(showInfo)
print(w_showInfo)

# 객체 지향 프로그래밍 예

class Person :
    def __init__(self):
        self.info = ""

    def showInfo(self, name, age):
        self.info += "이름: "+name+", "+"나이: "+age+"\n"
        print(self.info)

man = Person()
woman = Person()
man.showInfo("김민구","27")
man.showInfo("홍길동","23")
woman.showInfo("김태희","22")