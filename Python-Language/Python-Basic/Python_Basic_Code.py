# 연산자
print(1+1) # 2
print(3-2) # 1
print(5*2) # 10
print(6/3) # 2

print(2**3) # 2^3 = 8 (R: ^)
print(5%3) # 나머지 구하기 = 2 (R: %%)
print(10%3) # 나머지 구하기 = 1 (R: %%)
print(5//3) # 나누기 몫 구하기 = 1 (R: %/%)

print(10 > 3) # True
print(4 >= 7) # False
print(10 < 3) # False
print(5 <= 5) # True

print(3 == 3) # True
print(4 == 2) # False
print(3 + 4 == 7) # True

print(1 != 3) # True (1은 3이 아니다)
print(not(1 != 3)) # False (1은 3이 아니다의 반대)
print((3 > 0) and (3 < 5)) # True (3은 0보다 크고 5보다 작다)
print((3 > 0) & (3 < 5)) # True (3은 0보다 크고 5보다)

print((3 > 0) or (3 > 5)) # True (3은 0보다 크거나 5보다 크다)
print((3 > 0) | (3 > 5)) # True (3은 0보다 크거나 5보다 크다)

# R에서는 (5 > 4) & (4 > 3)으로 표현하지만, Python에서는 수학식처럼 5 > 4 > 3으로 표현 가능. 
print(5 > 4 > 3) # True
print(5 > 4 > 7) # False 





# <<자료구조>>

# 5-1. 리스트

# 지하철 칸별로 10명, 20명, 30명이 있다고 가정
subway = [10, 20, 30]
print(subway)

subway = ["유재석", "조세호", "박명수"]
print(subway)

# 조세호가 몇 번째 칸에 타고 있는가?
print(subway.index("조세호"))

# 하하가 다음 정류장에서 다음 칸에 탐
subway.append("하하")
print(subway)

# 정형돈이 유재석 / 조세호 사이에 태워봄
subway.insert(1, "정형돈") # 파이썬은 0부터 시작하기 때문에 1은 두 번째 칸을 의미
print(subway)

# 지하철에 있는 사람을 한 명씩 뒤에서 꺼냄
print(subway.pop())
print(subway)

# 같은 이름의 사람이 몇 명 있는지 확인
subway.append("유재석")
print(subway)
print(subway.count("유재석"))

# 정렬도 가능
num_list = [5, 2, 4, 3, 1]
num_list.sort()  # 오름차순 정렬
print(num_list)

# 순서 뒤집기
num_list.reverse()
print(num_list)

# 모두 지우기
num_list.clear()
print(num_list)

# 다양한 자료형 함께 사용
mix_list = ["조세호", 20, True]  # R: mix_list <- list("조세호", 20, True)
print(mix_list)

# 리스트 확장
num_list = [5, 2, 4, 3, 1]
mix_list = ["조세호", 20, True]

num_list.extend(mix_list)  # num_list에 mix_list의 요소들을 추가
print(num_list)


# + 튜플
# 튜플은 리스트와 거의 비슷하지만, 한 번 만들면 내용을 변경할 수 없다. 그래서 리스트보다 더 안전하게 데이터를 관리할 수 있다.
# 리스트는 수정 가능
menu_list = ["돈까스", "치즈까스"]
menu_list[0] = "생선까스" # 가능

# 튜플은 수정 불가능
menu_tuple = ("돈까스", "치즈까스")
menu_tuple[0] = "생선까스" # 에러 발생



# 5-2. 사전

cabinet = {3: "유재석", 100: "김태호"}  # 케비넷 열쇠는 3, 100이고, 각각 유재석과 김태호가 쓰고 있다.
print(cabinet)
print(cabinet[3])  # 3번 열쇠를 가져오면 유재석이 나온다.
print(cabinet[100])  # 100번 열쇠를 가져오면 김태호가 나온다.
print(cabinet.get(3))  # get()을 사용해서도 3번 열쇠를 가져올 수 있다.

print(cabinet.get(5))  # get()을 사용해서 5번 열쇠를 가져오려고 하면 None이 나온다.
print(cabinet.get(5, "사용 가능"))  # get()을 사용할 때 두 번째 인자로 "사용 가능"을 넣으면, 5번 열쇠가 없을 때 "사용 가능"이라는 메시지를 출력할 수 있다.

print(3 in cabinet)  # 3번 열쇠가 케비넷 안에 있는지 확인할 수 있다. True
print(5 in cabinet)  # 5번 열쇠가 케비넷 안에 있는지 확인할 수 있다. False

# 새 손님
cabinet = {"A-3": "유재석", "B-100": "김태호"}
cabinet["c-20"] = "조세호"  # 새로운 손님이 왔을 때, 새로운 열쇠와 이름을 추가하거나 사용 중일 경우 업데이트할 수 있다.
print(cabinet)

# 간 손님
del cabinet["A-3"]  # 손님이 나갔을 때, 열쇠와 이름을 삭제할 수 있다.
print(cabinet)

# key 들만 출력
print(cabinet.keys())

# value 들만 출력
print(cabinet.values())

# 폐업
cabinet.clear()  # 케비넷을 모두 비울 수 있다.



# 5-4. 세트(set)
# 세트는 집합을 의미한다. 중복된 값을 허용하지 않고, 순서가 없다. 그래서 리스트나 튜플보다 더 빠르게 데이터를 처리할 수 있다.

my_set = {1, 2, 3, 3, 3}  # 중복된 값이 있어도 하나만 남는다.
print(my_set)

java = {"유재석", "김태호", "양세형"}
python = set(["유재석", "박명수"])

# 교집합 (java와 python을 모두 할 수 있는 개발자)
print(java & python)  # R: intersect(java, python)
print(java.intersection(python))  # R: "

# 합집합 (java 할 수 있거나 python 할 수 있는 개발자)
print(java | python)  # R: union(java, python)
print(java.union(python))  # R: "

# 차집합 (java는 할 수 있지만 python은 할 줄 모르는 개발자)
print(java - python)  # R: setdiff(java, python)
print(java.difference(python))  # R: "

# python을 할 줄 아는 사람이 늘어남
python.add("김태호")
print(python)

# java를 잊어버림
java.remove("김태호")
print(java)





# <<제어문 & 함수>>

# 6. 제어문
# 6-1. if

wether = input("오늘 날씨는 어때요? ")  # 사용자로부터 입력을 받는 함수
if wether == "비" or wether == "눈":  # R: if (wether == "비" | wether == "눈")
    print("우산을 챙기세요")
elif wether == "미세먼지":
    print("마스크를 챙기세요")
else:
    print("준비물 필요 없어요")        

temp = int(input("기온은 어때요? "))  # 사용자로부터 입력을 받는 함수, 입력받은 값은 문자열이므로 int() 함수를 사용하여 정수로 변환
if temp >= 30:
    print("너무 더워요. 나가지 마세요")
elif 10 <= temp and temp < 30:  # R: elif (10 <= temp < 30)
    print("괜찮은 날씨에요")
elif 0 <= temp < 10:
    print("외투를 챙기세요")
else:
    print("너무 추워요. 나가지 마세요")



 # 6-2. for
print("대기번호 1")
print("대기번호 2")
print("대기번호 3")
print("대기번호 4")

# 위의 코드를 for문으로 바꾼다면
for waiting_no in [0, 1, 2, 3, 4]:  # R: for (waiting_no in c(0, 1, 2, 3, 4))
    print("대기번호 : {0}".format(waiting_no))  # R: print(paste("대기번호 :", waiting_no)) 

# 위의 코드와 같은 의미의 코드
for waiting_no in range(5):
    print(f"대기번호 : {waiting_no}")

for waiting_no in range(1, 6):  # R: for (waiting_no in 1:5)  # range(1, 6) 는 1부터 5까지의 숫자를 생성하는 함수
    print(f"대기번호 : {waiting_no}")   

starbucks = ["아이언맨", "토르", "아이엠 그루트"]
for customer in starbucks:
    print(f"{customer}, 커피가 준비되었습니다.")



# 6-3. while
customer = "토르"
index = 5
while index >= 1:
    print(f"{customer}, 커피가 준비되었습니다. {index}번 남았어요.")
    index -= 1  # index = index - 1
    if index == 0:
        print("커피는 폐기처분되었습니다.")

# 무한루프 생성
# customer = "아이언맨"
# index = 1
# while True:  # 항상 참이기 때문에 무한루프가 된다.
#     print(f"{customer}, 커피가 준비되었습니다. 호출 {index}회")
#     index += 1

customer = "토르"
person = "Unknown"
while person != customer:
    print(f"{customer}, 커피가 준비되었습니다")
    person = input("이름이 어떻게 되세요?")



# 6-4. continue, break
absent = [2, 5]  # 결석한 학생 번호
for student in range(1, 11):  # 1부터 10까지의 학생 번호
    if student in absent:
        continue  # 결석한 학생은 다음 반복으로 넘어감
    print(f"{student}번, 책을 읽어봐")  # 결석하지 않은 학생은 책을 읽어보라고 출력 

no_book = [7]  # 책을 깜빡한 학생 번호
for student in range(1, 11):
    if student in no_book:
        print(f"오늘 수업은 여기까지. {student}번, 오늘 수업 끝나고 교무실로 따라와.")  # 책을 깜빡한 학생은 수업 끝나고 교무실로 오라고 출력
        break  # 책을 깜빡한 학생이 나오면 반복문 종료
    print(f"{student}번, 책을 읽어봐")  # 책을 깜빡하지 않은 학생은 책을 읽어보라고 출력



# 6-5. 한 줄 for문
# 출석번호가 1, 2, 3, 4, 5, 앞에 100을 붙이기로 함 -> 101, 102, 103, 104, 105
students = [1, 2, 3, 4, 5]
students = [i + 100 for i in students]  # 학생 번호에 100을 더하는 한 줄 for문
print(students)

# 학생 이름을 길이로 변환
students = ["Iron man", "Thor", "I am Groot"]
students = [len(i) for i in students]  # 학생 이름의 길이를 구하는 한 줄 for문
print(students)

# 학생 이름을 대문자로 변환
students = ["Iron man", "Thor", "I am Groot"]
students = [i.upper() for i in students]  # 학생 이름을 대문자로 변환하는 한 줄 for문
print(students)



# 7-1. 함수
def open_account():
    print("새로운 계좌가 생성되었습니다.")
open_account() 



# 7-2. 전달값과 반환값
def deposit(balance, money):  # 입금  # balance: 현 잔액, money: 입금액
    print(f"입금이 완료되었습니다. 잔액은 {balance + money}원입니다.")
    return balance + money

def withdraw(balance, money):  # 출금
    if balance >= money:  # 잔액이 출금보다 많으면
       print(f"출금이 완료되었습니다. 잔액은 {balance - money}원 입니다.")
       return balance - money
    else:  # 잔액이 출금보다 적으면
        print(f"출금이 완료되지 않았습니다. 잔액은 {balance}원 입니다.")
        return balance

def withdraw_night(balance, money):  # 저녁에 출금
    commission = 100  # 수수료 100원
    if balance >= money + commission:  # 잔액이 출금 + 수수료보다 많으면
         print(f"수수료는 {commission}원이며, 잔액은 {balance - money - commission}원 입니다.")
         return commission, balance - money - commission
    else:  # 잔액이 출금 + 수수료보다 적으면
        print(f"출금이 완료되지 않았습니다. 수수료는 {commission}원이며, 잔액은 {balance}원 입니다.")
        return commission, balance

balance = 0  # 현 잔액
balance = deposit(balance, 1000)
balance = withdraw(balance, 2000)  # 잔액이 부족하기에 불가능
balance = withdraw(balance, 500)
commission, balance = withdraw_night(balance, 200)
commission, balance = withdraw_night(balance, 1000)  # 잔액이 부족하기에 불가능





# <<머신러닝 기초 : 데이터 객체화 및 분석 파이프라인에서 사용>>

# 9-1. 클래스
# 마린 : 공격 유닛, 군인. 총을 쏠 수 있음
name = "마린"  # 유닛의 이름
hp = 40  # 유닛의 체력
damage = 5  # 유닛의 공격력

print(f"{name} 유닛이 생성되었습니다.")
print(f"체력 {hp}, 공격력 {damage}\n")  # \n : 줄바꿈. 밑에 빈 줄 하나 추가

# 탱크 : 공격 유닛, 탱크. 포를 쏠 수 있음, 일반 모드 / 시즈 모드.
tank_name = "탱크"
tank_hp = 150
tank_damage = 35

print(f"{tank_name} 유닛이 생성되었습니다.")
print(f"체력 {tank_hp}, 공격력 {tank_damage}\n")

tank2_name = "탱크"
tank2_hp = 150
tank2_damage = 35

print(f"{tank2_name} 유닛이 생성되었습니다.")
print(f"체력 {tank2_hp}, 공격력 {tank2_damage}\n")

def attack(name, location, damage):
    print(f"{name} : {location} 방향으로 적군을 공격합니다. [공격력 {damage}]")

attack(name, "1시", damage)
attack(tank_name, "1시", tank_damage)
attack(tank2_name, "1시", tank2_damage)
# 공격 유닛이 많아질수록, 공격 유닛의 정보를 저장하는 변수도 많아지고, 공격 유닛을 공격하는 함수도 많아짐.
# 그래서 클래서라는 것을 만들어서, 유닛의 정보를 저장하는 변수와 유닛이 하는 행동을 함수로 묶어서 관리할 수 있음.

class Unit:
    def __init__(self, name, hp, damage):  # __init__ : 아래 설명
        self.name = name
        self.hp = hp
        self.damage = damage
        print(f"{self.name} 유닛이 생성되었습니다")
        print(f"체력 {self.hp}, 공격력 {self.damage}")

marine1 = Unit("마린", 40, 5)
marine2 = Unit("마린", 40, 5)
tank = Unit("탱크", 150, 35)



# 9-2. __init__ :  클래스의 생성자 함수로, 객체가 생성될 때 자동으로 호출되는 함수. 객체의 초기화 작업을 수행한다.
 # __init__ 함수에 정의된 갯수 만큼 인자를 전달해야 한다.



# 9-3. 멤버 변수 : class 내에 정의된 변수로, 객체마다 고유한 값을 가질 수 있다. self를 통해 접근한다.    

  # 레이스 : 공중 유닛, 비행기. 클로킹 (상대방에게 보이지 않음)
wraith1 = Unit("레이스", 80, 5)
print(f"유닛 이름 : {wraith1.name}, 공격력 : {wraith1.damage}")  # 멤버 변수를 이용하여 외부에서 유닛의 이름과 공격력을 출력

  # 마인드 컨트롤 : 상대방 유닛을 내 것으로 만드는 것 (빼앗음)
wraith2 = Unit("빼앗은 레이스", 80, 5)
wraith2.clocking = True  # wraith2 객체에 clocking 이라는 멤버 변수를 추가로 정의하여 클로킹 상태를 나타냄
                         # 기존의 다른 객체에는 적용이 되지 않음.
if wraith2.clocking == True:
    print(f"{wraith2.name}는 현재 클로킹 상태입니다.")