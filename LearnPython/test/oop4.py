# 클래스 변수와 객체 변수

class Man:

    cnt = 0 # 클래스 변수

    def __init__(self, name): # 생성자
        ''' 데이터 초기화 '''
        self.name = name # 객체 변수(메소드 내에서 선언된 변수)
        print("{} 생성되는 중...".format(self.name))

        Man.cnt += 1 # 클래스 변수에 접근 : 클래스명.클래스변수명

    def die(self):
        ''' Man 객체가 죽었을 때 '''
        print("{} 사망".format(self.name))

        Man.cnt -= 1

        if Man.cnt == 0 :
            print("{}은 최후의 생존자였다.".format(self.name))
        else :
            print("아직 {:d}명의 생존자가 남아있다.".format(Man.cnt))

    def say(self):
        print("생성완료 : 안녕하세요!! 저의 이름은 {} 입니다".format(self.name))

    @classmethod # 장식자(decorator) : how_many = classmethod(how_many)의 다른 표현
    def how_many(how):
        ''' 현재의 객체 수량 체크'''
        print("현재 {}명이 남았습니다.".format(Man.cnt))

# 실행
gameActor1 = Man("전사")
gameActor1.say()

gameActor2 = Man("마법사")
gameActor2.say()

gameActor3 = Man("궁수")
gameActor3.say()

print("-------------------------")
gameActor2.die()
gameActor1.die()
gameActor3.die()

#Man.say() # 객체 메소드 say() 이렇게 접근이 안됨!!! 에러!!
Man.how_many() # 클래스 메소드 호출 : 클래스명.메소드명