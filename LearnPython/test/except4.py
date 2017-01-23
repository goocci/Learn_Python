# 예외 발생시키기 : raise 명령어를 이용해서 에러를 강제로 발생시키기는 방법

class Fleight:
    def fly(self):
        raise NotImplementedError # 파이썬 내장 에러 : 자식 클래스가 부모 클래스 메소드를 구현하지 않았을 경우

class Plane(Fleight):
    #pass
    def fly(self):
        print("떳다~ 떳다~ 비행기~")

plane = Plane()
plane.fly()