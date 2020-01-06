#모듈 : 미리 작성된 함수 코드를 모아 놓은 파이썬 파일. c++ 헤더파일처럼 자신만의 모듈을 만들 수도 가져올 수도  있다. 
import math
print(math.pow(3, 8)) # 3의 8제곱
print(math.sqrt(64)) #64의 제곱근
print(math.gcd(72, 24)) #두수의 최대공약수
#같은 시스템내에 lib라는 파일을 함수처럼 만들고 아래처럼 불러와 사용. 서브라임에서는 사용안되는듯.
import lib
print(lib.add(3, 7)) 이런식. 

#모듈이 크다면 from lib import add 이런식으로 하면 
#print(add(3, 7)) 이런식으로 사용 가능.

#import lib as t 
#as를 사용 하면 모듈을 짧은 단어로 사용 가능
#print(t.add(3, 7)) 이런식으로 사용 가능.