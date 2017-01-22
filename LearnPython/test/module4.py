# 클래스, 변수, 함수를 포함하는 모듈 만들기
PI = 3.141592

class Math:
    def aaa(self, r):
        return PI*(r**2)

def sum(i,j):
    return i+j

if __name__ == "__main__": # module4.py 을 직접 실행하는 경우
    print(PI)
    bb = Math()
    print(bb.aaa(10))
    print(sum(PI,10))

# dir() 내장함수 : 객체(모듈)에 정의되어 있는 식별자(변수이름, 함수이름, 클래스이름 등등)들을 알려주는 함수
# 리스트 형태로 반환하는 함수

# 패키지 : 단순하게 폴더라고 생각하자
# (파이썬에서 폴더는 모듈을 담는 역할을 한다. init.py 파일 포함)