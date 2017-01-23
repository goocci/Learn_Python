# random 모듈 (난수 발생 모듈)
"""
  난수 : 0.0 ~1.0 사이의 실수 값
"""
import random
print(random.random())

print(random.randint(1,10))

print(random.randint(10, 50))

def pop_list(data):
	n = random.randint(0, len(data)-1)
	return data.pop(n)

if __name__ =="__main__":
	data = [1,3,5,6,7]
	while data:print(pop_list(data))