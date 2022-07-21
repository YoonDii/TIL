with open('student.txt','r', encoding= 'utf-8') as f :
    line = f.readline() #호출을 할때마다 한줄씩 읽어서 출력
    print(line,type(line))
    #김철수
    #<class 'str'>


with open('student.txt','r', encoding= 'utf-8') as f :
    for line in f:
        print(line, end='')  #end=''는 개행빼기
        # 김철수  
        # 신짱구
        # 한유리
        # 이훈이
        # 이맹구
        # 한수지