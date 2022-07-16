### 0713

# 함수

- 특정한 기능을 하는 코드의 조각(묶음) 
- 특정 명령을 수행하는 코드를 매번 다시 작성하지 않고, 필요 시에만 호출하여 간편히 사용

### 1.정의

#### 1-1. 사용자 함수 (Custom Function)

-  구현되어 있는 함수가 없는 경우, 사용자가 직접 함수를 작성 가능

```python
#초기 값 설정하고 함수 정의하기
def function_name(parameter):
	# code block
	return returning_value
#print해서 출력1-2. 내장함수(Built-in Function) 활용

```

#### 1-2.  내장함수(Built-in Function)

| 내장 함수                                                    |                                                              |                                                              |                                                              |
| :----------------------------------------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| **A**[`abs()`](https://docs.python.org/ko/3/library/functions.html#abs)[`aiter()`](https://docs.python.org/ko/3/library/functions.html#aiter)[`all()`](https://docs.python.org/ko/3/library/functions.html#all)[`any()`](https://docs.python.org/ko/3/library/functions.html#any)[`anext()`](https://docs.python.org/ko/3/library/functions.html#anext)[`ascii()`](https://docs.python.org/ko/3/library/functions.html#ascii) **B**[`bin()`](https://docs.python.org/ko/3/library/functions.html#bin)[`bool()`](https://docs.python.org/ko/3/library/functions.html#bool)[`breakpoint()`](https://docs.python.org/ko/3/library/functions.html#breakpoint)[`bytearray()`](https://docs.python.org/ko/3/library/functions.html#func-bytearray)[`bytes()`](https://docs.python.org/ko/3/library/functions.html#func-bytes) **C**[`callable()`](https://docs.python.org/ko/3/library/functions.html#callable)[`chr()`](https://docs.python.org/ko/3/library/functions.html#chr)[`classmethod()`](https://docs.python.org/ko/3/library/functions.html#classmethod)[`compile()`](https://docs.python.org/ko/3/library/functions.html#compile)[`complex()`](https://docs.python.org/ko/3/library/functions.html#complex) **D**[`delattr()`](https://docs.python.org/ko/3/library/functions.html#delattr)[`dict()`](https://docs.python.org/ko/3/library/functions.html#func-dict)[`dir()`](https://docs.python.org/ko/3/library/functions.html#dir)[`divmod()`](https://docs.python.org/ko/3/library/functions.html#divmod) | **E**[`enumerate()`](https://docs.python.org/ko/3/library/functions.html#enumerate)[`eval()`](https://docs.python.org/ko/3/library/functions.html#eval)[`exec()`](https://docs.python.org/ko/3/library/functions.html#exec) **F**[`filter()`](https://docs.python.org/ko/3/library/functions.html#filter)[`float()`](https://docs.python.org/ko/3/library/functions.html#float)[`format()`](https://docs.python.org/ko/3/library/functions.html#format)[`frozenset()`](https://docs.python.org/ko/3/library/functions.html#func-frozenset) **G**[`getattr()`](https://docs.python.org/ko/3/library/functions.html#getattr)[`globals()`](https://docs.python.org/ko/3/library/functions.html#globals) **H**[`hasattr()`](https://docs.python.org/ko/3/library/functions.html#hasattr)[`hash()`](https://docs.python.org/ko/3/library/functions.html#hash)[`help()`](https://docs.python.org/ko/3/library/functions.html#help)[`hex()`](https://docs.python.org/ko/3/library/functions.html#hex) **I**[`id()`](https://docs.python.org/ko/3/library/functions.html#id)[`input()`](https://docs.python.org/ko/3/library/functions.html#input)[`int()`](https://docs.python.org/ko/3/library/functions.html#int)[`isinstance()`](https://docs.python.org/ko/3/library/functions.html#isinstance)[`issubclass()`](https://docs.python.org/ko/3/library/functions.html#issubclass)[`iter()`](https://docs.python.org/ko/3/library/functions.html#iter) | **L**[`len()`](https://docs.python.org/ko/3/library/functions.html#len)[`list()`](https://docs.python.org/ko/3/library/functions.html#func-list)[`locals()`](https://docs.python.org/ko/3/library/functions.html#locals) **M**[`map()`](https://docs.python.org/ko/3/library/functions.html#map)[`max()`](https://docs.python.org/ko/3/library/functions.html#max)[`memoryview()`](https://docs.python.org/ko/3/library/functions.html#func-memoryview)[`min()`](https://docs.python.org/ko/3/library/functions.html#min) **N**[`next()`](https://docs.python.org/ko/3/library/functions.html#next) **O**[`object()`](https://docs.python.org/ko/3/library/functions.html#object)[`oct()`](https://docs.python.org/ko/3/library/functions.html#oct)[`open()`](https://docs.python.org/ko/3/library/functions.html#open)[`ord()`](https://docs.python.org/ko/3/library/functions.html#ord) **P**[`pow()`](https://docs.python.org/ko/3/library/functions.html#pow)[`print()`](https://docs.python.org/ko/3/library/functions.html#print)[`property()`](https://docs.python.org/ko/3/library/functions.html#property) | **R**[`range()`](https://docs.python.org/ko/3/library/functions.html#func-range)[`repr()`](https://docs.python.org/ko/3/library/functions.html#repr)[`reversed()`](https://docs.python.org/ko/3/library/functions.html#reversed)[`round()`](https://docs.python.org/ko/3/library/functions.html#round) **S**[`set()`](https://docs.python.org/ko/3/library/functions.html#func-set)[`setattr()`](https://docs.python.org/ko/3/library/functions.html#setattr)[`slice()`](https://docs.python.org/ko/3/library/functions.html#slice)[`sorted()`](https://docs.python.org/ko/3/library/functions.html#sorted)[`staticmethod()`](https://docs.python.org/ko/3/library/functions.html#staticmethod)[`str()`](https://docs.python.org/ko/3/library/functions.html#func-str)[`sum()`](https://docs.python.org/ko/3/library/functions.html#sum)[`super()`](https://docs.python.org/ko/3/library/functions.html#super) **T**[`tuple()`](https://docs.python.org/ko/3/library/functions.html#func-tuple)[`type()`](https://docs.python.org/ko/3/library/functions.html#type) **V**[`vars()`](https://docs.python.org/ko/3/library/functions.html#vars) **Z**[`zip()`](https://docs.python.org/ko/3/library/functions.html#zip) **_**[`__import__()`](https://docs.python.org/ko/3/library/functions.html#import__) |

> 출처 -https://docs.python.org/ko/3/library/functions.html

#### 1-3. pstdev 함수 (파이썬 표준 라이브러리 - statistics)

- 평균과 중심 위치의 측정
  - 함수는 모집단(population)이나 표본(sample)에서 평균이나 최빈값을 계산합니다.

| [`mean()`](https://python.flowdas.com/library/statistics.html#statistics.mean) | 데이터의 산술 평균(arithmetic mean) ( "average").            |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [`fmean()`](https://python.flowdas.com/library/statistics.html#statistics.fmean) | 빠른, 부동 소수점 산술 평균.                                 |
| [`geometric_mean()`](https://python.flowdas.com/library/statistics.html#statistics.geometric_mean) | 데이터의 기하 평균(geometric mean).                          |
| [`harmonic_mean()`](https://python.flowdas.com/library/statistics.html#statistics.harmonic_mean) | 데이터의 조화 평균(harmonic mean).                           |
| [`median()`](https://python.flowdas.com/library/statistics.html#statistics.median) | 데이터의 중앙값(median) (중간값).                            |
| [`median_low()`](https://python.flowdas.com/library/statistics.html#statistics.median_low) | 데이터의 낮은 중앙값(low median).                            |
| [`median_high()`](https://python.flowdas.com/library/statistics.html#statistics.median_high) | 데이터의 높은 중앙값(high median).                           |
| [`median_grouped()`](https://python.flowdas.com/library/statistics.html#statistics.median_grouped) | 그룹화된 데이터의 중앙값, 또는 50번째 백분위 수(50th percentile) |
| [`mode()`](https://python.flowdas.com/library/statistics.html#statistics.mode) | 이산(discrete) 또는 범주(nominal) 데이터의 단일 최빈값(mode) (가장 흔한 값) |
| [`multimode()`](https://python.flowdas.com/library/statistics.html#statistics.multimode) | 이산 또는 범주 데이터의 최빈값(mode) (가장 흔한 값) 리스트.  |
| [`quantiles()`](https://python.flowdas.com/library/statistics.html#statistics.quantiles) | 데이터를 같은 확률을 갖는 구간으로 나눕니다.                 |

- 분산측정
  - 이 함수는 모집단이나 표본이 평균값에서 벗어나는 정도를 측정합니다.

| [`pstdev()`](https://python.flowdas.com/library/statistics.html#statistics.pstdev) | 데이터의 모집단 표준 편차(population standard deviation). |
| ------------------------------------------------------------ | --------------------------------------------------------- |
| [`pvariance()`](https://python.flowdas.com/library/statistics.html#statistics.pvariance) | 데이터의 모집단 분산(population variance).                |
| [`stdev()`](https://python.flowdas.com/library/statistics.html#statistics.stdev) | 데이터의 표본 표준 편차(sample standard deviation).       |
| [`variance()`](https://python.flowdas.com/library/statistics.html#statistics.variance) | 데이터의 표본 분산(sample variance).                      |

> 출처- https://python.flowdas.com/library/statistics.html#

### 2. 함수 기본 구조

- 선언과 호출(define & call)
- 입력(Input) 
- 범위(Scope) 
- 결과값(Output)

#### 2-1. 선언과 호출

- 함수의 선언은 def 키워드를 활용함 
- 들여쓰기를 통해 Function body(실행될 코드 블록)를 작성함 
  - Docstring은 함수 body 앞에 선택적으로 작성 가능
    - 작성시에는 반드시 첫 번째 문장에 문자열 ''' ''' 
- 함수는 parameter를 넘겨줄 수 있음 
- 함수는 동작 후에 return을 통해 결과값을 전달함
- 함수는 함수명()으로 호출
  - parameter가 있는 경우, 함수명(값1, 값2, …)로 호출

```python
def KDT():
    return True  

def cook(a, b)
	return a + b  
```

#### 2-2. 입력(Input)

- Parameter : 함수를 실행할 때, 함수 내부에서 사용되는 식별자 
- Argument : 함수를 호출 할 때, 넣어주는 값

```python
def function(ham): # parameter : ham
return ham
function('spam') # argument: 'spam'
```

- **Argument**
  - 함수 호출 시 함수의 parameter를 통해 전달되는 값 
  - Argument는 소괄호 안에 할당 func_name(argument) 
    - 필수 Argument : 반드시 전달되어야 하는 argument 
    -  선택 Argument : 값을 전달하지 않아도 되는 경우는 기본 값이 전달

- **positional arguments**
  - 기본적으로 함수 호출 시 Argument는 위치에 따라 함수 내에 전달됨

```python
def add(x, y):        add(2,3)
    return x + y
```

- **keyword arguments**
  - 직접 변수의 이름으로 특정 Argument를 전달할 수 있음 
  - Keyword Argument 다음에 Positional Argument를 활용할 수 없음

```python
def add(x, y):        add(x=2, y=5)   add(2, y=5)
	return x + y
```

- **Default Arguments Values**
  - 기본값을 지정하여 함수 호출 시 argument 값을 설정하지 않도록 함 
    - 정의된 것 보다 더 적은 개수의 argument들로 호출 될 수 있음

```python
def add(x, y=0):       add(2)
	return x + y         
```

- **정해지지 않은 개수의 arguments**
  - 여러 개의 Positional Argument를 하나의 필수 parameter로 받아서 사용 
    - 몇 개의 Positional Argument를 받을지 모르는 함수를 정의할 때 유용 
  -  Argument들은 튜플로 묶여 처리되며, parameter에 *를 붙여 표현

```python
def add(*args):           add(2)
	for arg in args:      add ( 2, 3, 4, 5)
	print(arg)
```

- **정해지지 않은 개수의 keyword arguments**
  - 함수가 임의의 개수 Argument를 Keyword Argument로 호출될 수 있도록 지정 
  - Argument들은 딕셔너리로 묶여 처리되며, parameter에 **를 붙여 표현

```python
def family(**kwargs):
	for key, value in kwargs:
	print(key, ":", value)
family(father='John', mother='Jane', me='John Jr.')
```

#### 2-3. 범위(Scope)

- 함수는 코드 내부에 local scope를 생성하며, 그 외의 공간인 global scope로 구분 
-  **scope **
  - global scope : 코드 어디에서든 참조할 수 있는 공간 
  -  local scope : 함수가 만든 scope. 함수 내부에서만 참조 가능 
- **variable** 
  - global variable : global scope에 정의된 변수 
  - local variable : local scope에 정의된 변수

- **객체 수명주기**
  - 객체는 각자의 수명주기(lifecycle)가 존재 
    - **built-in scope**
      -  파이썬이 실행된 이후부터 영원히 유지 
    - **global scope** 
      - 모듈이 호출된 시점 이후 혹은 인터프리터가 끝날 때까지 유지 
    - **local scope**
      - 함수가 호출될 때 생성되고, 함수가 종료될 때까지 유지

```python
def func():
	a = 20
	print('local', a)
func()
print('global', a)   ## a는 Local scope에서만 존재
```

- **이름 검색 규칙(Name Resolution)**
  - 파이썬에서 사용되는 이름(식별자)들은 이름공간(namespace)에 저장되어 있음 
  -  아래와 같은 순서로 이름을 찾아나가며, LEGB Rule이라고 부름 
    - Local scope : 함수 
    -  Enclosed scope : 특정 함수의 상위 함수 
    -  Global scope : 함수 밖의 변수, Import 모듈 
    - Built-in scope : 파이썬 안에 내장되어 있는 함수 또는 속성 
  -  즉, 함수 내에서는 바깥 Scope의 변수에 접근 가능하나 수정은 할 수 없음

#### 2-4. 결과값(Output)

- **return**
  - 함수는 반드시 값을 하나만 return한다. 
    - 명시적인 return이 없는 경우에도 None을 반환한다. 
  - 함수는 return과 동시에 실행이 종료된다.

```python
def minus_and_product(x, y):
	return x - y
	return x * y
###return은 하나밖에 못함.

#return은 함수 안에서 값을 반환하기 위해 사용되는 키워드.
#print는 출력을 위해 사용되는 함수.
```

### 3. 함수 응용

- 내장함수 활용하기

- map(function, iterable) 

  - 순회 가능한 데이터구조(iterable)의 모든 요소에 함수(function)적용하고, 그 결과를 map object로 반환

  - 알고리즘 문제 풀이시 input 값들을 숫자로 바로 활용하고 싶을 때

    ```python
    a, b = map(int, input().split())
    ```

    