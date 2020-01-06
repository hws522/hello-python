#List
#비슷한 성질을 가진 객체의 나열
#Index
#0 1 2 ...
a = [3.5, 4.3, 2.3, 4.5, 3.2, 1.3]
print(a)
print("Index 0 = ", a[0])
print("Index 2 = ", a[2])
a[0] = 1.0
print("Index 0 = ", a[0])

sum = 0

for i in a :
    sum = sum + i
print("average : ", sum / len(a)) #len : 길이를 구함.

b = [
    [90, 95, 30, 20, 50, 66, 58, 90, 54, 10], #이중리스트
    [33, 44, 55, 56, 77, 88, 99, 11, 22, 66]
    ]

sum = 0
english = b[0]
for i in english :
    sum = sum + i
print("english average : ", sum / len(english))

sum = 0
math = b[1]
for i in math :
    sum = sum + i
print("math average : ", sum / len(math))

a = [10, 20, 30 , 40 , 50]
b = [70, 50, 30 , 10]
print(a.count(10)) #리스트 내 특정 원소가 몇 개 포함되어 있는지 반환
print(a.index(50)) #리스트 내 특정 원소의 인덱스를 반환. 
a.append(25) #리스트의 끝에 새로운 원소를 삽입.
print(a)

a.sort() #기본설정은 오름차순. 자동으로 정렬됨.
print(a)
a.extend(b) #리스트의 끝에 다른 리스트를 삽입.
print(a)
a.insert(3, 70) #원하는 인덱스의 위치에 원소를 삽입.
print(a)
a.remove(10) #리스트 내 특정한 원소를 앞에서 부터 하나만 삭제.
print(a)
a.pop(3) #리스트 내 특정 인덱스의 원소를 삭제.
print(a)
a.reverse() #리스트 순서를 뒤바꿈.
print(a)