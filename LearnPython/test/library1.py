'''
라이브러리(library) : 전세계의 파이썬 개발자(사용자)들에 의해서 이미 만들어진 프로그램들을 모아놓은 것을 말한다.-
'''
"""
파이썬 라이브러리는 파이썬 설치시 자동으로 컴퓨터에 설치가된다.

sys 모듈, pickle 모듈, io 모듈, os 모듈, glob 모듈, time 모듈, calendar 모듈, random 모듈, 쓰레드(thread) 모듈 등....

sys.argv : 명령행에서 인수를 전달한다.
sys.exit() : ctrl+Z(윈도우 환경), ctrl+D(유닉스환경)를 눌러서 대화형 인터프리터(쉘)를 종료하는 기능
sys.path.append() : 자신이 만든 모듈을 불러서 사용하기 위해 위치를 지정하는 명령
"""

import sys
#sys.exit()
print(sys.argv)
sys.path
