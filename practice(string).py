#문자열 자료형 뒤집기 : 슬라이싱 활용
str = "Hello World"
print(str[::-1])

# len() : 문자열의 길이를 출력
print(len(str))

# .isalpha() : 특정한 문자열이 문자로만 이루어져 있는지 확인. 공백이나 숫자 체크
print(str.isalpha())

# .isdigit() : 특정한 문자열이 숫자로만 이루어져 있는지 확인.
print(str.isdigit())

# .isalnum() : 특정한 문자열이 문자와 숫자로만 이루어져 있는지 확인.
print(str.isalnum())

# .join(리스트 자료형) : 여러 개의 문자열을 구분자와 함께 합치는 함수.
list = ["Hello", "World", "홍길동"]
print('-'.join(list))
print(','.join(list))
print(' '.join(list))

# sorted(문자열 자료형) : 각문자를 정렬하는 함수
str = "helloworld"
list = sorted(str) #기본 오름차순
print(list)
print(''.join(list))
list = sorted(str, reverse = True) #내림차순.
print(''.join(list))

# split(토큰) : 문자열을 토큰에 따라서 분리하는 함수
str = "ttI wanna watch a movie.tt"
list = str.split(" ")
print(list)

# .find(서브문자열) : 원하는 문자열이 위치한 인덱스를 찾음.
print(str.find("wanna"))
print(str.find(" ", 2)) #인덱스 2 이후의 공백을 찾겠다라는 의미.

#upper(), lower() :  문자열을 대문자로 , 혹은 소문자로 모두 변환.
print(str.upper())
print(str.lower())

#strip() : 좌우로 특정한 문자열을 제거하는 함수
print(str.strip("t")) #()안에 아무것도 안넣으면 공백제거.
print(str.lstrip("t")) #왼쪽만 제거
print(str.rstrip("t")) #오른쪽만 제거

#eval() : 문자열 수식 계산해주는 함수.
exp = "(203 + 506)*4 - (30/6)"
print(eval(exp))