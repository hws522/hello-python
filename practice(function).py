def add(a, b) : #함수 정의 할때 def
    sum = a + b
    return sum #c++과는 달리 리턴타입이 필요없는듯.
'''
def add(a, b) : 리턴타입필요없을땐 이런식으로.
    print(a + b)
'''
a = add(2,3)

print(add(1,2))
print(a)

#가변인자 : 함수의 매개변수가 가변적일 수 있을 때 사용 . 포인터형식으로 사용. 
#일반적으로 다수의 매개변수를 넣는경우 튜플형식으로 처리됨

def function(*data) :
    print(data)

function(1,2,3)    

#전역 변수
#지금까지 쓰던거.

#지역변수
#함수안에 쓰는거 

def add(a) : 
    a = a + 5 # a 는 지역변수 

a = 2 # a 는 전역변수
add(a)
print(a) #결과는 2가 나옴.

def add() :
    global a #함수 안에서 전역변수를 사용하고싶으면 global. global로 설정된 변수는 매개변수로 사용될 수 없음. 
    a = a + 5

add()
print(a) # 결과 정상적으로 7 나옴.

#파이썬의 함수는 반환 값이 여러 개일 수 있다. 그 경우 튜플형태로 출력된다.

def function() :
    a = 5
    b = [1, 2, 3]
    return a, b

a, b = function()
print(a)
print(b)
