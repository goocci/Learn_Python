# 에러 파하기(pass 활용) : 특정 에러가 발생할 경우 통과시키는 방법

try:
    fp = open("nofile.txt", "r")
except FileNotFoundError:
    pass # 파일이 없어도 예외로 처리하지 않고 넘어간다.

print("에러없이 수행됨")