#클래스 : 반복되는 불필요한 소스코드를 최소화 하면서 
#현실 세계의 사물을 컴퓨터 프로그래밍 상에서 
#쉽게 표현 할 수 있도록 해주는 프로그래밍 기술.

#인스턴스 : 클래스로 정의된 객체를 프로그램 상에서 이용할 수 있게 만든 변수.

# 클래스의 멤버 : 클래스 내부에 포함되는 변수
# 클래스의 함수 : 클래스 내부에 포함되는 함수. 메소드라고 부릅니다.

class Car:
    #클래스의 생성자
    def __init__(self, name, color):
        self.name = name #클래스의 멤버
        self.color = color #클래스의 멤버
    #클래스의 메소드
    def show_info(self):
        print("name : ", self.name, "/ color : ", self.color)

    #setter 메소드 c++과 똑같다. 말만 그런건지 이렇게 써야만 하는건지 잘 모르겠다. 해보니까 이름 바꿔도 됨.  
    #클래스 내에 변수 변경
    def  settt_name(self, name):
        self.name = name
    def __del__(self):
        print("인스턴스를 소멸시킵니다.")

car1 = Car("소나타", "빨간색")
car1.show_info()
car1.settt_name("아반떼")
car1.show_info()


car2 = Car("아반떼", "검은색")
car2.show_info()

print(car1.name, "을(를) 구매했습니다.") #클래스의 멤버변수에 접근할 땐 온점으로 접근. c++과 비슷.
#파이썬에서는 클래스 첫번째 매개변수는 self. 클래스를 통해 생성된 인스턴스 그자체.
#자동 소멸되나 , del car1 이런식으로 써도됨. 오류 날 수도 있음. del 이후에 불러내면 에러.

#상속 : 다른클래스의 멤버 변수와 메소드를 물려 받아 사용하는 기법.
#부모와 자식 관계가 존재.
#자식클래스 : 부모클래스를 상속받은 클래스

class Unit:
    def __init__(self, name, power):
        self.name = name
        self.power = power
    def attack(self):
        print(self.name, "이 공격을 수행합니다. [전투력 : ", self.power, "]")

unit = Unit("홍길동", 450)
unit.attack()

class Monster(Unit):
    def __init__(self, name, power, type):
        self.name = name
        self.power = power
        self.type = type

monster = Monster("슬라임", 30, "초급")
monster.attack() #상속을 통해 사용 가능. #상속받은 클래스와 부모클래스가 똑같다면 자식클래스를 우선처리함.


