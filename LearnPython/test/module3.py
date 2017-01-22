'''
모듈의 name속성 (__name__)

모든 모듈은 이름을 갖고 있다.
모듈의 name 속성을 이용하면 외부로 부터 불러들여 졌을 때 곧바로 실행되지 않게 할 수 있다.
'''

def sum(i,j):
    return i+j

def differ(i,j):
    return i-j

if __name__ == "__main__":
    print(sum(1, 2))
    print(differ(1, 2))

# 파이썬의 모듈은 name 속성을 가지고 있는데 name이 'main'일 경우에는
# 사용자가 직접 실행한것임을 의미한다. 따라서, 적절하게 name 속성을 활용하여
# 요구에 맞게 실행될 수 있도록 한다.