#예외처리. 오류가 나올수 있는 상황을 처리.

try:
    print(3/0)
except Exception as e: #오류메세지를 저장해서 직접 출력가능.
    print(e)
#except:
 #   print("0으로는 나눌 수 없습니다.")
else:
    print("예외 없이 성공적으로 실행되었습니다.")
finally:
    print("예외 처리를 마칩니다.") # 상황에 상관없이 나옴.