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


# + 튜플
# 튜플은 리스트와 거의 비슷하지만, 한 번 만들면 내용을 변경할 수 없다. 그래서 리스트보다 더 안전하게 데이터를 관리할 수 있다.
# 리스트는 수정 가능
menu_list = ["돈까스", "치즈까스"]
menu_list[0] = "생선까스" # 가능

# 튜플은 수정 불가능
menu_tuple = ("돈까스", "치즈까스")
# menu_tuple[0] = "생선까스" # 에러 발생



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