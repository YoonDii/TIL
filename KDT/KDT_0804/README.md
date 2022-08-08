### 0804

# 이차원리스트 (순회,전치,회전)

#### 📢순회

```python
#이중 for문을 이용한 행 우선 순회
matrix = [
[1, 2, 3, 4],
[5, 6, 7, 8],
[9, 0, 1, 2]
]
for i in range(3):#행 ↓
	for j in range(4):#열→
		print(matrix[i][j], end=" ")
	print()
>>> 1 2 3 4
>>> 5 6 7 8
>>> 9 0 1 2


#이중 for문을 이용한 열 우선 순회
matrix = [
[1, 2, 3, 4],
[5, 6, 7, 8],
[9, 0, 1, 2]
]
for i in range(4):#열
	for j in range(3):#행
		print(matrix[j][i], end=" ")
	print()
>>> 1 5 9
>>> 2 6 0
>>> 3 7 1
>>> 4 8 2

#행 우선 순회를 이용해 이차원 리스트의 총합 구하기
matrix = [
[1, 1, 1, 1],
[1, 1, 1, 1],
[1, 1, 1, 1]
]
total = 0
for i in range(3):
	for j in range(4):
		total += matrix[i][j]
print(total)
>>> 12

#위 코드를 간략하게 줄여보자! Pythonic하게!
matrix = [
[1, 1, 1, 1],
[1, 1, 1, 1],
[1, 1, 1, 1]
]
total = sum(map(sum, matrix))
print(total)
>>> 12

#최소/최댓값구하기
matrix = [
[0, 5, 3, 1],
[4, 6, 10, 8],
[9, -1, 1, 5]
]
max_value = max(map(max, matrix))
min_value = min(map(min, matrix))
print(max_value)
>>> 10
print(min_value)
>>> -1
```



#### 📢전치

> 전치(transpose)란 행렬의 행과 열을 서로 맞바꾸는 것을 의미.

```python
matrix = [
[1, 2, 3, 4],
[5, 6, 7, 8],
[9, 0, 1, 2]
]
#전치 행렬을 담을 이차원리스트 초기화(행과열의 크키가 반대)
transposed_matrix = [[0] * 3 for _ in range(4)]
for i in range(4):
	for j in range(3):
		transposed_matrix[i][j] = matrix[j][i] # 행, 열 맞바꾸기
"""
transposed_matrix = [
[1, 5, 9],
[2, 6, 0],
[3, 7, 1],
[4, 8, 2]
]
"""
```



#### 📢회전

> 문제에서 이차원 리스트를 왼쪽, 오른쪽으로 90도 회전하는 경우가 존재한다.

```python
# 왼쪽으로 90도 회전하기
matrix = [
[1, 2, 3],
[4, 5, 6],
[7, 8, 9]
]
n = 3
rotated_matrix = [[0] * n for _ in range(n)]
for i in range(n):
	for j in range(n):
		rotated_matrix[i][j] = matrix[j][n-i-1]
        
#오른쪽으로 90도 회전하기
matrix = [
[1, 2, 3],
[4, 5, 6],
[7, 8, 9]
]
n = 3
rotated_matrix = [[0] * n for _ in range(n)]
for i in range(n):
	for j in range(n):
		rotated_matrix[i][j] = matrix[n-j-1][i]
```

