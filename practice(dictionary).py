#사전 자료형 : 키와 값을 한쌍을 원소로 가지는 자료형.

dict = {} #중괄호 사용됨.
dict ["안녕"] = "Hello"
dict ["기적"] = "Miracle"
dict ['안녕'] = "Hi" #이렇게 쉽게 변경가능

#del dict["기적"] #삭제 가능
#dict.clear() #모두 삭제.
print(dict)

print("자료형의 길이 추출가능 : ", len(dict))

for i, k in enumerate(dict):
#i 에는 인덱스
#k 에는 키값
    print("[인덱스: ", i, "] 한글 : ", k, "/ 영어 : ", dict[k])

keys = dict.keys() #키 값만 빼내기.
key_list = list(keys) #키값들을 리스트로 변환
values = dict.values() #갑만 빼내기.
values_list = list(values) #값들을리스트로 변환
print("키 : ", key_list)
print("값 : ", values_list)

if "안녕" in dict:
    print("존재합니다.")

scores = {}
scores["서현우"] = 90
scores["홍길동"] = 100
scores["나미야"] = 40

print(sorted(scores)) #키로 정렬됨. 오름차순
print(sorted(scores, reverse = True)) #키로 내림차순
print(sorted(scores.values())) #값 기준으로 정렬.
