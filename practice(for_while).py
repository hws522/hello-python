#숫자 범위 표현 : range(start, end)
sum = 0
for i in range(1 , 10) : 
    print(i)
    sum = sum + i

print("sum : ", sum)

count = 0
for i in "Hello World" : #띄어쓰기도 문자로 포함.
    print(i)
for i in "Hello World" :
    if i == 'o':
        count = count + 1
print("o의 개수 : ", count)

sum = 0

list = [1, 2, 3, 4, 5] #리스트 사용 가능
for i in list :
    sum = sum + i
print("합계 : ", sum)

#continue : 더이상 명령어를 실행하지 않고 다음반복
#break : 반복문 종료

for i in list :
    if i % 2 == 1:
        continue
    print(i)

#while : 특정 조건을 만족 할때만 반복. for 보다 간단.

i = 0
sum = 0
while i < 5 :
    i += 1
    if i % 2 == 1:
        continue
    sum = sum + i
print("짝수 합계 : ", sum)

