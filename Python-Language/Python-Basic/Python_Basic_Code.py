# 연산자
print(1+1) # 2
print(3-2) # 1
print(5*2) # 10
print(6/3) # 2

print(2**3) # 2^3 = 8 (R = ^)
print(5%3) # 나머지 구하기 = 2 (R = %%)
print(10%3) # 나머지 구하기 = 1 (R = %%)
print(5//3) # 나누기 몫 구하기 = 1 (R = %/%)

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