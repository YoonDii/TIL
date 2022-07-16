with open('student.txt','r', encoding= 'utf-8') as f :
    text = f.read() #텍스트파일 읽어줘
    print(text,type(text))
    # 김철수
    # 신짱구
    # 한유리
    # 이훈이
    # 이맹구
    # 한수지
    #  <class 'str'>


    with open('student.txt','r', encoding= 'utf-8') as f :
        text = f.read() 
    # text는 string타입
    print(text,type(text))
    # text.split() --> list 타입으로
    names = (text.split())
    cnt = 0 
    for name in names: #성이 김씨인 사람은 몇명?
       if name.startswith('김'):
       # if name[0] == '김':
            cnt += 1
    print(cnt) #1

