#시퀀스(sequence) : 문자열, 리스트, 투플 등의 인덱스를 가지는 자료형
# 순서와 인덱스를 가짐. 
#len 사용가능.
#반복문등에서 사용가능.
string = "Hello World"
list = ['H','e','l','l','o',' ','w','o','r','l','d']
tuple = ('H','e','l','l','o',' ','w','o','r','l','d')

print(string[0 : 5])
print(list[0 : 5])
print(tuple[0 : 5])

for i in tuple : 
    print(i)

print(len(tuple))

print('i' in string) #string 에서 i 를 포함하고 있는지 true false로 나옴.
print('i' in list)
print('i' in tuple)

if 'H' in list:
    print("'H'포함하고 있음.")
