### 0811

# DFS 코딩테스트

코딩테스트는 주로 문제의 내용을 코드로 구현 가능한지 테스트한다.

• 문제 풀이에 시간 제한이 없는 경우가 많기 때문에 시간 복잡도를 생각하지 않고 풀어보는 것이 좋다.

• 완전탐색 중에서도 2차원 배열의 탐색, 델타 탐색 등 선형 탐색이 주를 이룬다.



단순 구현(Implementation)은 문제에 제시된 풀이 과정을 그대로 구현하는 유형

• 시뮬레이션의 경우 완전탐색 유형 중 하나로써, 모든 경우의 수를 탐색하여 풀이한다 . 

• 아이디어나 알고리즘을 요구하기 보다는, 문제에 제시된 과정을 그대로 구현할 수 있는가가 핵심

```python
# 8방향 델타값
directions = {
"R": (0, 1),
"L": (0, -1),
"B": (1, 0),
"T": (-1, 0),
"RT": (-1, 1),
"LT": (-1, -1),
"RB": (1, 1),
"LB": (1, -1),
}
방향이 알파벳으로 입력되므로, 딕셔너리를 사용한다.

#이차원행렬만들기
visited = [[False] * m for _ in range(n)]
```

