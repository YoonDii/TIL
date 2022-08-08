### 0803

# 이차원리스트 

> 리스트를 원소로 가지는 리스트
>
> `matrix = [[1,2,3], [4,5,6],[7,8,9]]`
>
> 이차원리스트는 matrix(행렬)이다.

```python
#반복문으로 100x100행렬만들기
matrix = []
for x in range(100):
    matrix.append([0] * 100)

    
#반복문으로 nxm행렬만들기
n = 4 #행
m = 3 # 열
matrix = []
for x in range(n):
	matrix.append([0] * m)

#리스트 컴프리헨션으로 nxm행렬만들기
n = 4 # 행
m = 3 # 열
matrix = [[0] * m for x in range(n)]
```

행과 열을 헷갈리지 말고 잘풀어야함!

