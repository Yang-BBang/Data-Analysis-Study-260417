# 4장

# 변수 만들기, 데이터 프레임 만들기
english <- c(90, 80, 60, 70)                    #영어 점수 변수 생성
math <- c(50, 60, 100, 20)                      #수학 점수 변수 생성
df_midterm <- data.frame(english, math)         #데이터 프레임 생성

# 엑셀 파일
library(readxl)                                 #readxl 패키지 로드
df_exam <- read_excel("excel_exam.xlsx")        #엑셀 파일 불러오기 

# csv 파일
df_csv_exam <- read.csv("csv_exam.csv")         #csv 파일 불러오기
write.csv(df_midterm, file = "df_midterm.csv")  #csv 파일로 저장하기

# RDS 파일
load("df_midterm.rds")                          #RDS 파일 불러오기
save(df_midterm, file = "df_midterm.rds")       #RDS 파일로 저장하기



# 5장

# 데이터 준비, 패키지 준비
mpg <- as.data.frame(ggplot2::mpg)              #데이터 불러오기
library(dplyr)                                  #dplyr 로드
library(ggplot2)                                #ggplot2 로드

# 데이터 파악
head(mpg)                                       #Raw 데이터 앞부분
tail(mpg)                                       #Raw 데이터 뒷부분
View(mpg)                                       #Raw 데이터 뷰어창에서 확인
dim(mpg)                                        #차원  
str(mpg)                                        #속성
summary(mpg)                                    #요약 통계량

# 변수명 수정
mpg <- rename(mpg, company = manufacturer)

# 파생변수 생성
mpg$total <- (mpg$cty + mpg$hwy)/2                    #변수 조합
mpg$test <- ifelse(mpg$total >= 20, "pass", "fail")   #조건문 활용

# 빈도 확인
table(mpg$test)                                 #빈도표 출력
qplot(mpg$test)                                 #막대 그래프 생성



# 6장

# 조건에 맞는 데이터만 추출하기
exam %>% filter(english >= 80)

# 여러 조건 동시 충족
exam %>% filter(class == 1 & math >= 50)

# 여러 조건 중 하나 이상 충족
exam %>% filter(math >= 90 | english >= 90)
exam %>% filter(class %in% c(1, 3, 5))          #1, 3, 5반만 추출

# 필요한 변수만 추출하기
exam %>% select(math)
exam %>% select(class, math, english)

# 함수 조합하기, 일부만 출력하기
exam %>%
  select(id, math) %>%
  head(10)

# 순서대로 정렬하기
exam %>% arrange(math)                          #오름차순 정렬
exam %>% arrange(desc(math))                    #내림차순 정렬
exam %>% arrange(class, math)                   #여러 변수 기준 오름차순 정렬

# 파생변수 추가하기
exam %>% mutate(total = math + english + science)

# 여러 파생변수 한 번에 추가하기
exam %>%
  mutate(total = math + english + science,
         mean = (math + english + science)/3)

# mutate()에 ifelso() 적용하기
exam %>% mutate(test = ifelse(science >= 60, "pass", "fail"))

# 추가한 변수를 dplyr 코드에 바로 활용하기
exam %>%
  mutate(total = math + english + science) %>%
  arrange(total)

# 집단별로 요약하기
exam %>%
  group_by(class) %>%
  summarise(mean_math = mean(math))

# 각 집단별로 다시 집단 나누기
mpg %>%
  group_by(manufacturer, drv) %>%
  summarise(mean_cty = mean(cty))

# 가로로 데이터 합치기
total <- left_join(test1, test2, by = "id")

# 세로로 데이터 합치기
group_all <- bind_rows(group_a, group_b)



# 7장

#결측치 정제하기
# 결측치 확인
table(is.na(df$score))

# 결측치 제거
df_nomiss <- df %>% filter(!is.na(score))

# 여러 변수 동시에 결측치 제거
df_nomiss <- df %>% filter(!is.na(score) & !is.na(sex))

# 함수의 결측치 제외 기능 이용하기
mean(df$score, na.rm = T)
exam %>% summarise(mean_math = mean(math, na.rm = T))

#이상치 정제하기
# 이상치 확인
table(outlier$sex)

# 결측 처리
outlier$sex <- ifelse(outlier$sex == 3, NA, outlier$sex)

# boxplot으로 극단치 기준 찾기
boxplot(mpg&hwy)$stats

# 극단치 결측 처리
mpg$hwy <- ifelse(mpg$hwy < 12 | mpg$hwy > 37, NA, mpg$hwy)



# 8장

#산점도
ggplot(data = mpg, aes(x = displ, y = hwy)) +
  geom_point()
# 축 설정 추가
ggplot(data = mpg, aes(x = displ, y = hwy)) +
  geom_point() +
  xlim(3, 6) +
  ylim(10, 30)

# X축 별 색 추가
ggplot(data = mpg, aes(x = displ, y = hwy, col = displ)) + geom_point()

# 그래프값 자체 색 추가
ggplot(data = mpg, aes(x = displ, y = hwy)) +
  geom_point(col = "red")

#평균 막대 그래프
# 1단계. 평균표 만들기
df_mpg <- mpg %>%
  group_by(drv) %>%
  summarise(mean_hwy = mean(hwy))

# 2단계. 그래프 생성하기, 크기순 정렬하기
ggplot(data = df_mpg, aes(x = reorder(drv, -mean_hwy), y= mean_hwy)) + geom_col()

#빈도 막대 그래프
ggplot(data = mpg, aes(x = drv)) +
  geom_bar

#선 그래프
ggplot(data = economics, aes(x = date, y = unemploy)) +
  geom_line()

#상자 그림
ggplot(data = mpg, aes(x = drv, y = hwy)) +
  geom_boxplot()



# 15장 - R 내장 함수, 변수 타입과 데이터 구조

# 데이터 추출하기
exam[1,]                                        #행 번호로 행 추출
exam[exam$class == 1,]                          #조건을 충족하는 행 추출
exam[exam$class == 1 & exam$math >= 50,]        #여러 조건을 충족하는 행 추출

exam[,1]                                        #열 번호로 변수 추출
exam[, "class"]                                 #변수명으로 변수 추출
exam[,c("class", "math", "english")]            #변수명으로 여러 변수 추출
exam[1,3]                                       #행, 변수 동시 추출 - 인덱스
exam[exam$math >= 50, "english"]                #행, 변수 동시 추출 - 조건문, 변수명

# 변수 타입
var <- c(1, 2, 3, 1, 2)                         #numeric 변수 만들기
var <- factor(c(1, 2, 3, 1, 2))                 #factor 변수 만들기
var <- factor(c("a", "b", "b", "c"))            #문자로 구성된 factor 변수 만들기

class(var)                                      #변수 타입 확인하기
levels(var)                                     #factor 변수의 구성 범주 확인
var <- as.numeric(var)                          #factor 타입을 numeric 타입으로 변환하기

# 데이터 구조
a <- 1                                          #벡터 만들기
b <- "hello"
x1 <- data.frame(var1 = c(1, 2, 3),
                 var2 = c("a", "b", "c"))       #데이터 프레임 만들기
x2 <- matrix(c(1:12), ncol = 2)                 #매트릭스 만들기
x3 <- array(1:20, dim = c(2, 5, 2))             #어레이 만들기
x4 <- list(f1 = a,                              #리스트 만들기
           f2 = x1,
           f3 = x2,
           f4 = x3)

# 리스트 활용하기
x <- boxplot(mpg$cty)                           #상자 그림 만들기
x$stats[, 1]                                    #요약 통계량 추출
