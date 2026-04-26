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