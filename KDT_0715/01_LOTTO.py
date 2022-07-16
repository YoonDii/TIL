import random
# 로또번호 생성기
# 1~45까지의 숫자
# 그 중에 6개
num = random.sample(range(1, 46), 6) #range는 [x이상, y미만]으로 설정하기.
print(num, type(num)) # [14, 1, 21, 45, 37, 24] <class 'list'>


num = random.sample(range(1, 46), 6) 
num.sort() #num아 정렬해~
print(num, type(num)) #[3, 7, 20, 27, 31, 33] <class 'list'>


n = int(input('얼마쓸꺼?'))
for i in range(n):#입력받은 수 만큼 결과내기
    num = random.sample(range(1, 46), 6) 
    num.sort() 
    print(num, type(num))
# 얼마쓸꺼?5
# [19, 27, 28, 35, 41, 42] <class 'list'>
# [2, 4, 12, 30, 31, 40] <class 'list'>
# [4, 13, 19, 28, 31, 44] <class 'list'>
# [10, 12, 17, 23, 34, 35] <class 'list'>
# [2, 4, 8, 12, 22, 37] <class 'list'>
