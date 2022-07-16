with open('student.txt','r', encoding= 'utf-8') as f :
    lines = f.readlines() #호출을 할때마다 한줄씩 읽어서 출력
    print(lines,type(lines))
    #['김철수\n', '신짱구\n', '한유리\n', '이훈이\n', '이맹구\n', '한수지\n'] <class 'list'>
    # 개행없이 쓰고 싶을때는 .strip 메서드 사용하기.
