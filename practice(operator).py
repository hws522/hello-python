#증감 연산자 : += -= *= /=
# ++ -- 존재하지 않음.

#관계 연산자 : == != < > true false 값이 나옴.

a = "abc"
b = "def"
print(a == b)
print(a < b) # 문자열 비교할때는 사전순으로 비교. true

#논리 연산자 : and 모두 참인지, or 둘중 하나가 참인지
# not a a가 거짓인지 

a = True
b = False

print(a and b)
print(a or b)
print(not a)

if 3 > 5 or 7 < 10 :
    print("OK")