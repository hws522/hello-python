#파일 입출력
#open() : 파일을 특정한 모드로 여는 함수. 읽을 때는 r, 쓸 때는 w
#read() : 파일 객체로 부터 모든 내용을 읽는 함수.


#f = open("input.txt", "r", encoding = "utf-8")
'''
f.seek(9) #9바이트를 건너뛰고 읽겠다. 일반적으로 파이썬에서는 한글이 3바이트씩 차지함.
data = f.read()
print(data)
f.close()'''
'''
count = 0
while count < 3:
    data = f.readline() # readline() : 파일 객체로 부터 한 줄씩 문자열을 읽는 함수 입니다.
    count = count + 1
    print("%d번째 줄 : %s" %(count, data))
f.close()
'''
'''
# readlines() : 전체 내용을 한번에 리스트에 담는 함수 입니다.
list = f.readlines()
for i , data in enumerate(list):
    print("%d번째 줄 : %s" %(i + 1, data), end = '') #end를 씀으로써 리스트 안에 있는 
                                                        #백슬래시로 인해 두번줄바꿈이 일어나지 않게함.

#print(list)
f.close()'''

'''
with open("input.txt", "r", encoding = "utf-8") as f: #with 를 쓰면 따로 오픈 클로즈를 쓰지 않아도 됨. 
                                                            #with 구문을 나오면 자동으로 닫힘.
    list = f.readlines()
    for i , data in enumerate(list):
        print("%d번째 줄 : %s" %(i + 1, data), end = '') '''

def process(filename):
    with open(filename, "r") as f:
        #키 : 알파벳, 값 : 빈도수
        dict = {}                                                      
        data = f.read()
        for i in data:
            if i in dict:
                dict[i] += 1
            else:
                dict[i] = 1

    return dict

dict = process("input.txt")              
print(dict)

#빈도수를 기준으로 내림차순

dict = sorted(dict.items(), key = lambda a:a[1], reverse = True)  
print(dict)

for data, count in dict:
    if data == '\n' or data == ' ':
        continue
    print("%d번 출현 : [%c]" %(count, data))