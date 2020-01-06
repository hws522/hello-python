#tuple : list 와 비슷한 자료형
#한번 설정된 값을 바꿀수 없음. 
tuple = (1, 2, 3)
list = (2, 4, 6)
print(tuple)
print(list)

for i in tuple :
    print(i)

list1 = [1, 2, 3]
list2 = [4, 5, 6]
tuple = (list1, list2)
print(tuple)
print(tuple[0][1]) 

#tuple[0] = [7,8,9] # 불가능
tuple[0][1] = 7 # 가능

#tuple 의 원소 자체는 바꿀수 없지만, tuple의 원소로 리스트가 있을때는 리스트의 값은 바꿀 수 있다. 
#인덱싱, 슬라이싱 등의 문법도 그대로 사용 가능.

tuple = (1, 2, 3, 4, 5, 6)
print(tuple[0:5] * 3)