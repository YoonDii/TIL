# 'r' : read (읽기 전용)
# 'w' : write (쓰기 전용 - 덮어씀)
# 'a' : append (쓰는데 파일 있으면 이어서 씀)

# 파일명, 모드설정,인코딩설정
with open('test.txt','w', encoding = 'utf-8') as f:
    f.write('coging is hell\n') #txt파일 만들어서 내용쓰기.
    for i in range(1, 6): #i에 range만큼 반복하기
        f.write(f'{i}일째!\n') #개행(\n) 꼭 확인하기!!!
       
# coging is hell
# 1일째!
# 2일째!
# 3일째!
# 4일째!
# 5일째!

    