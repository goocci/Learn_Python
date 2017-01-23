'''
예외 처리
'''

'''
FileNotFoundError(파일이 없을 때)
ZeroDivisionError(숫자를 0으로 나누었을 때)
IndexError(리스트에서 얻어 올 수 없는 값일 경우)
SyntaxError(구문 오류)
EOFError(파일의 끝일 경우:읽을 내용이 없을 때)
등...
-> 프로그램 중단

'''
'''
예외 처리 기본 형식(자바의 try ~ catch)
try:
    수행 명령...
except[발생에러[as 에러메세지 변수]]:
    수행 명령...

*** 대괄호는 생략이 가능하다는 표기 방법 ***

1)
try:
    수행 명령...
except:
    수행 명령...

2)
try:
    수행 명령...
except 발생에러:
    수행 명령...

3)
try:
    수행 명령...
except 발생에러 as 에러메시지 변수:
    수행 명령...
'''

try:
    str = input("문자를 입력하세요 >>")
except EOFError:
    print("읽을 내용이 없습니다.")
except KeyboardInterrupt:
    print("입력 취소되었습니다.")
else:
    print("입력한 문자 : {}".format(str))