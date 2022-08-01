### 0801

# 스택, 큐 (Stack, Queue)

#### 1. 스택(stack)

> Stack은 쌓는다는 의미로써, 마치 접시를 쌓고 빼듯이 데이터를 한쪽에서만 넣고 빼는 자료구조 가장 마지막에 들어온 데이터가 가장 먼저 나가므로 LIFO(Last-in First-out, 후입선출) 방식
>
> **뒤집기, 되돌리기, 되돌아가기, 마루지 되지 않은 일 임시저장**
>
> 
>
> list로 간단하게 풀기 = list.append(인자) / list.pop()



#### 2. 큐 (Queue)

>Queue는 한 쪽 끝에서 데이터를 넣고, 다른 한 쪽에서만 데이터를 뺄 수 있는 자료구조 가장 먼저 들어온 데이터가 가장 먼저 나가므로 FIFO(First-in First-out, 선입선출) 방식
>
>dequeue :  큐의 맨 앞에 데이터를 가져오는 행위
>
>enqueue : 큐의 맨 뒤에 데이터를 삽입하는 행위
>
>
>
>list로 간단하게 풀기 = list.append(인자) / list.pop()
>
>하지만 list는 빼야할 데이터가 많은 경우 비효율적!
>
>이럴때는
>
> 덱 (Deque, Double-Ended Queue) 자료구조 == 양 방향으로 삽입과 삭제가 자유로운 큐
>
>덱은 양 방향 삽입, 추출이 모두 큐보다 훨씬 빠르다.
>
>appendleft( ) / popleft( )  왼쪽으로 넣고 빼기
>
>append( ) /  pop( ) 오른쪽으로 넣고 빼기

