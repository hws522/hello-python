'''#index(원소) : 리스트 내 특정한 원소의 인덱스를 찾기
list = ['서현우', '강종구', '이태일', '박한울', '이상욱']
print(list.index('이태일'))

#reverse() : 리스트의 원소를 뒤집기
list.reverse()
print(list)

print(list[::-1]) #슬라이싱으로도 뒤집기 가능

#sum(리스트 자료형) : 리스트의 모든 원소의 합. 숫자만 가능.
list = [0,1,2,3,4,5,6]
print(sum(list))

#range(시작, 끝) : 특정 범위를 지정
my_range = range(5, 10)
print(my_range)

#list(특정범위) : 특정 범위의 원소를 가지는 리스트를 반환.
list = list(my_range)
print(list) #결과 [5, 6, 7, 8, 9]

#all() / any() : 리스트의 모든 원소가 참인지 / 하나라도 참인지 
list = [True, False, True]
print(all(list))
print(any(list))

#enumerate() : 리스트에서 인덱스와 원소를 함꼐 추출
my_list = ['가', '나', '다', '라', '마']
result = list(enumerate(my_list))
print(result)


#sort() : 리스트의 원소를 정렬.  기본 오름차순
my_list = ['서현우', '강종구', '이태일', '박한울', '이상욱']
my_list.sort()
print(my_list)

#count() : 특정한 원소의 개수를 추출
print(my_list.count('서현우'))

#del() : 리스트의 특정 원소를 제거
del my_list[1]
print(my_list) # 결과는 1번인덴스 뺴고 출력.

#insert(삽입할 위치의 인덱스, 값) : 리스트에 특정 원소 삽입.
my_list.insert(3, '마이크')

#append() : 리스트의 가장 마지막원소로 삽입.
my_list.append("야나두")

'''