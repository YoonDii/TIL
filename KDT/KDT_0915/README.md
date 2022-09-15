### 0915

# JavaScript-1

> 웹을 하려면 자바스트립트를 모르면 안된다!

`출처`-`mdn`

#### 1. 동적 클라이언트 스트립팅 자바스크립트!

아무리 열심히 css + html을 하더라도 자바스크립트가 없으면 원하는 대로 동작하지 않는다.

자바스크립트는 정적인 HTML 콘텐츠를 프로그램 구현을 통해 동적으로 변경하거나 사용자와의 상호작용을 담당하게 됩니다.

HTML이나 CSS와 달리 자바스크립트는 C언어, 자바와 같은 일반 프로그램언어와 비슷한 구조를 가지고 있습니다. 따라서 단순히 콘텐츠 제작만을 생각하는 프론트엔드 초보 개발자에게는 가장 어려운 부분이라 할 수 있습니다.

자바스크립트는 객체(Object) 기반의 스크립트 언어로 기본적으로는 웹 브라우저에서 해석되는 인터프리터 언어이며 Node.js와 같은 프레임워크를 사용하면 서버 프로그래밍에도 사용할 수 있습니다.

현재 컴퓨터나 스마트폰 등에 포함된 웹 브라우저에는 자바스크립트 인터프리터가 내장되어 있습니다.



#### 자바스크립트 특징

- 동적이며 타입을 명시할 필요가 없는 인터프리터 언어 이다.
- 객체지향 프로그래밍과 함수형 프로그래밍을 모두 표현할 수 있다.
- HTML의 내용, 속성, 스타일을 변경 할 수 있다.
- 이벤트를 처리하고 사용자와의 상호작용을 가능하게 함.
- AJAX 기술을 이용해 서버와 실시간 통신 기능을 제공.

----------------------------------

### 2.기본문법

자바스크립트는 기본적으로 HTML 문서의 `<head></head>` 사이에 위치 합니다. 그러나 그 외 위치에 둘수도 있고 외부파일이나 다른 서버를 통해 참조하는 방식으로도 사용할 수 있습니다.

여기서는 자바스크립트의 소스가 위치하는 몇몇 유형에 대해 살펴 봅니다.



#### 1) 내부 자바스크립트

HTML 문서 내부에 자바스크립트 소스코드를 두는 유형 입니다. `<head></head>` 혹은 `<body></body>` 에 둘 수 있으며 양쪽에 모두 있어도 상관 없습니다.

```
<script>
  alert('hello world');
</script>
```

- 현재 HTML 파일의 문서구조(DOM)에 쉽게 접근이 가능.
- 현재 화면에 동적인 요소를 부여하는 자바스크립트가 같은 소스파일에 위치하기 때문에 코드 관리와 이해가 쉬움.
- 자바스크립트 소스가 복잡해지는 경우 관리가 어려움.
- 공통된 기능을 만들기 어렵고 코드의 재활용이 어려움.



#### 2) 외부 JavaScript

HTML 문서 외부에 별도의 파일을 생성하고 HTML 에서 불러와 사용하는 방식 입니다. 이때 자바스크립트 파일의 위치는 HTML과 동일한 서버 혹은 외부 서버일수도 있습니다.

- 웹의 HTML코드로부터 웹의 동작을 구현하는 자바스크립트 코드를 분리할 수 있음.
- HTML과 자바스크립트 코드의 읽기가 수월해지고 유지 보수 간편.
- 공통기능의 모듈화와 코드 재활용이 가능해 짐.
- 소스가 분리되어 있고 HTML, 자바스크립트 모두 복잡한 경우 소스 이해가 어려울 수 있음.

```
//external.js 파일
function printDate() {
  alert('hello world');
}
<head>
  <script src="../external.js"></script>
  <!-- 외부 서버의 js파일 참고인 경우 다음과 같이 사용 -->
  <script src="https://www.cdn.com/myjs/external.js"></script>
</head>
```



#### 3) 소스파일 위치 결정

브라우저는 HTML의 구조와 CSS 스타일을 렌더링하는 도중 자바스크립트를 만나게 되면 이에 대한 해석과 구현이 완료될때까지 브라우저 렌더링을 멈추게 됩니다. 즉, 자바스크립트의 삽입 위치에 따라 스크립트 실행순서와 브라우저 렌더링에 영향을 미치기 때문에 다음 사항을 고려해 적절한 위치선정이 필요 합니다.



#### `<head></head>`

- 브라우저 렌더링에 방해가 될 수 있으며 무거운 스크립트가 실행되는 경우 오랫동안 화면이 보여지지 않을수 있음.
- 문서를 초기화하거나 설정하는 가벼운 스크립트들을 주로 사용.
- 문서의 DOM(Document Object Model) 구조가 필요한 경우 HTML이 모두 로드 된 이후 실행되어야 하므로 `window.onload`와 같은 로드 이벤트가 추가되어야 함.



#### `<body></body>`

- 태그내 모든 위치에 둘 수 있음.
- 웹페이지 로딩이 완료된 다음 실행하기 위해 일반적으로는 `</body>` 바로 앞에 위치.
- 이경우 문서의 DOM 구조가 완료된 시점에 실행되기에 별다른 추가설정이 필요없음.



#### 내부 자바스크립트 VS 외부 자바스크립트

- 비교적 간단한 코드로 구성되며 현재 파일에만 적용되는 경우 내부 자바스크립트를 사용.
- 공통기능 구현이나 소스가 길어지면 외부 자바스크립트로 관리함.
- 공통 라이브러리로 개발된 경우 CDN을 통해 외부 서버로 부터 참조해서 사용함.

------



## 2-1.변수와 자료형

자바스크립트는 다른 언어들과 달리 자료형이 고정되어 있지 않은 동적타입 언어 입니다. 따라서 변수를 선언할때 별도의 자료형을 명시하지 않아도 됩니다.

### 1) 자료형

내부적으로는 Primitive(기본형)과 Object(객체형)이 있으며 각각 다음과 같습니다.

#### Primitive

- Boolean: true, false
- null: 빈 값을 표현
- undefined: 값을 할당하지 않은 변수가 가지는 값
- Number: 숫자형으로 정수와 부동 소수점, 무한대 및 NaN(숫자가 아님)등.
- String: 문자열

#### Object

- Reference 타입
- 클래스 뿐만 아니라, 배열과 함수, 사용자 정의 클래스도 모두 Object.
- JSON(Java Script Object Notation)의 기본 구조.

Object 에 대해서는 06.함수와 객체 에서 자세히 살펴봅니다.

### 2) 변수 선언

- 변수이름은 대소문자를 구별.
- 여러 변수를 한번에 선언할 수 있음.
- 지역변수와 전역변수가 있음.
- 기본적으로 소문자로 시작되는 Camel Case 를 사용.

```
var firstNumber;
firstNumber = 10;
```

#### var, let, const

> ES6 이전에는 `var` 만 존재했으며 function-scoped 로 인해 다른 언어들과 다른 문제가 있었음.

- `var`는 지역변수 개념으로 함수 범위에서 유효함.
- `var`를 선언하지 않으면 자동으로 전역변수가 됨.
- `let`과 `const` 는 ES6 에서 등장한 block-scoped 변수 선언.
- `let`은 값의 재할당이 가능하고 const 는 불가능(immutable).
- `const`로 선언된 배열이나 객체의 경우 새로운 객체로 재할당하는 것은 안되고, 배열값의 변경/추가, 객체의 필드 변경등은 가능.

다음은 var 를 이용한 변수선언 예 입니다.

```
var foo = 'foo1';
console.log(foo); // foo1
 
if (true) {
  var foo = 'foo2';
  console.log(foo); // foo2
}

console.log(foo); // foo2
```

다음은 `let`과 `const` 예 입니다.

```
let foo = 'foo1';
const bar = 'bar1';
console.log(foo); // foo1
 
if (true) {
  let foo = 'foo2';
  console.log(foo); // foo2
  console.log(bar); // bar1
}
 
console.log(foo); // foo1
bar = 'bar2'; // error
```

#### hoisting

> 호이스팅은 끌어올리기라는 사전전 의미를 가지고 있습니다. 자바스크립트에서 모든 변수 선언은 호이스트 되고 함수의 경우 선언형식은 호이스팅 되며 변수에 할당된 형태는 호이스팅 되지 않습니다.

자바스크립트 변수에 있어 변수의 선언이 위치와 상관없이 최상위 레벨로 끌어올려진다고 이해할 수 있습니다.

```
if (true) {
  console.log(foo); // undefined
  var foo = 'foo1';
  console.log(foo); // foo1
}
```

- 일반적인 언어인 경우 `foo` 변수는 첫번째 출력문에서 선언되기 전 상태로 에러가 발생해야 함.
- 자바스크립트는 `var foo` 가 호이스트 되어 변수는 선언되고 값이 할당되지 않은 상태가 됨.

```
var myVar;

function myVar() {
  ...
}
console.log(typeof myVar); // function
```

- 위 예제에서는 myVar 라는 변수를 먼저 선언한 상태에서 동일 이름의 함수를 정의.
- 함수 선언이 호이스팅 되어 myVar 변수에 할당.

경우에 따라 호이스팅은 사소한 문제를 일으키지 않아 유용할수 있으나 복잡한 코드에서는 오류 가능성이 높으므로 변수 선언시에는 var, let, const 등을 명확히 구분해서 사용하는 것이 좋다.

#### String 변수

일반적인 프로그램언어들은 문자열을 표현할때 `큰따옴표(" ")` 를 사용하는데 반해 자바스크립트는 `" ",' '` 를 모두 사용할 수 있습니다.

```
var string;
string = "Java Script"; // 혹은 'Java Script'
```

-----------------------------

## 연산자와 제어문

일반적인 프로그램언어와 같이 자바스크립트도 다양한 연산자와 `if, for` 와 같은 제어문을 가지고 있습니다.

### 1) 연산자

기본적으로 다른 프로그램언어들과 유사 합니다.

#### 비교 연산자

> 비교연산자의 결과는 기본적으로 true/false 입니다.

| 연산자 | 연산자 설명                                     |
| :----: | ----------------------------------------------- |
|   ==   | 값이 같은지 비교                                |
|  ===   | 값과 타입이 모두 같은지 비교                    |
|   !=   | 같지 않음                                       |
|  !==   | 값이나 타입이 같지 않음                         |
|   >    | 크다                                            |
|   <    | 작다                                            |
|   >=   | 같거나 크다                                     |
|   <=   | 작거나 크다                                     |
|   ?    | 3항연산 (조건)? 참인경우 수행 : 거짓인경우 수행 |

비교 연산자 목록

#### 논리 연산자

| 연산자 | 연산자 설명 |
| :----: | ----------- |
|   &&   | AND 연산자  |
|  \|\|  | OR 연산자   |
|   !    | NOT 연산자  |

논리 연산자 목록

### 2) 조건문

C, 자바와 매우 유사합니다. if, else, switch 등이 있습니다.

#### if, else if

> 특정 조건이 참인 경우 수행되는 코드 블럭을 정의 합니다. else 와 결합해 조건 범위나 조건을 세분화하는 것이 가능하며 AND, OR 연산을 함께 사용할 수 있습니다.

```
var score = 85;

if (score >= 90)
	console.log('A');
else if (score >= 80)
	console.log('B');
else if (score >= 70)
	console.log('C');
else
	console.log('F');
```

- score 에 따라 해당 점수 구간의 성적이 출력되도록 합니다.

#### switch

> 입력값에 따라 처리를 다르게 하는 경우 사용합니다. 내용적으로는 `if ~ else if` 와 유사합니다.

```
var level = 'B';

switch(level) {
  case 'A' :
    console.log('VIP 등급');break;
  case 'B' :
    console.log('일반 등급');break;
  default :
    console.log('등급없음');break;
}
```

### 3) 반복문

반복문 역시 C, 자바와 매우 유사합니다. for, while, forEach, for-in, for-of-for 등이 있습니다.

#### for

> 기본 구조는 시작, 종료조건, 증감식을 가지는 형태 입니다. 다음 예제는 세개의 값을 가지는 배열을 선언하고 배열값을 모두 출력하는 예제 입니다.

```
const colors = ['red', 'blue', 'green'];
for (let i = 0; i < colors.length; i++) {
	console.log( colors[i] );
}
```

#### while

> 조건이 성립하는 경우 계속 반복하는 구문입니다. 무한 루프가 되지 않도록 코드 중간에 조건을 반드시 변경해 주어야 합니다.

```
const colors = ['red', 'blue', 'green'];
var i=0;
while (colors[i] != null) {
  console.log( colors[i] );
  i++;
}
```

#### forEach

> ES5에서 사용가능하게 된 문법으로 배열의 모든 원소에 대해 특정 코드블럭을 수행할 수 있는 방법입니다.

```
const colors = ['red', 'blue', 'green'];
colors.forEach(function(value) {
  console.log(value);
});
```

ES6 에서는 arrow 연산자를 통해 다음과 같이 간결하게 사용할수 있습니다.

```
const colors = ['red', 'blue', 'green'];
colors.forEach( value => console.log(value));
```

#### for-in, for-of

> 최근 다른 언어들에 도입된 -in 형태의 구문 입니다. 다만 -in 의 경우 배열원소의 값에 접근할 수 없고 키 혹은 인덱스만 접근이 가능하므로 다른 언어에서의 -in과 같은 형태로 사용하려면 for-of를 사용해야 합니다.

```
const colors = ['red', 'blue', 'green'];
for (var index in colors) {
	console.log( colors[index] );
}

for (var value of colors) {
	console.log( value );
}
for-in
```

- 객체의 모든 열거 가능한 속성에 대해 반복.
- 즉, 배열 뿐만 아니라 일반적인 객체의 속성들을 모두 반복할 때도 사용 가능.
- 모든 객체의 key(배열의 경우 인덱스)에 접근할 수 있지만 value에 접근할 수는 없음.

```
for-of
```

- 반복 가능한(Iterable)객체의 값을 순환. 배열 이외 `문자열 데이터`(유니코드 이모지 포함) 처리도 가능.
- `ES6`에 새로 추가된 `MAP, SET` 에도 적용 가능.
- Object를 대상으로 하지 않으며 `객체의 속성`을 순회하려면 `for-in` 을 사용.
- Object를 사용할 경우 object.keys()로 키 값을 구해서 순회하면서 출력할 수 있음.

---------------------------------



## 배열과 자료구조

기본적인 개념은 다른언어와 동일하지만 `정의하거나 사용하는 형태`는 다소 `차이`가 있습니다.

### 1) 배열

배열의 선언은 `[]` 나 `new Array()` 로 생성하고 크기의 제약이 없으며 하나의 배열에 서로 다른 타입의 변수가 들어갈 수 있습니다.

다음은 다양한 배열 선언 예 입니다.

```
var emptyArray = [];
var numbers1 = [10, 30, 50, 70, 90];
var numbers2 = new Array(20, 40, 60, 80, 100);
var mixedArr = ['a', 1, 'b', 2, new Date(), "today"];

console.log(numbers2[2]);
console.log(mixedArr[4]);
```

아직 자바스크립트 객체를 배우기 전이지만 배열에 `자바스크립트 객체`를 넣을 수 있습니다. 이를 이용하면 JSON 데이터의 집합을 만들 수 있으며 서버와의 데이터 교환에 사용할 수 있는 구조가 됩니다.

```
var objArr = [
  {
    "id" : 20192010,
    "name" : "홍길동",
    "dept" : "컴퓨터공학과"
  },
  {
    "id" : 20192011,
    "name" : "김사랑",
    "dept" : "경영학과"
  },
  {
    "id" : 20192012,
    "name" : "강동수",
    "dept" : "전자공학과"
  }
];

console.log(objArr[2].name + "," + objArr[2].dept);
```

#### 배열의 주요 메서드

> 배열 데이터를 다루기 위한 다양한 메스드(함수)가 제공되고 있습니다. 각각에 대한 구체적인 동작은 예제를 통해 확인하기 바랍니다. 

```
데이터 변경
```

- `push()`: 배열의 끝에 값을 추가.
- `pop()`: 배열 마지막 값을 제거.
- `shift()`: 배열 데이터를 왼쪽으로 하나씩 밀어 맨앞 값을 제거.
- `splice()`: 배열값을 추가하거나 제거해서 반환.
- `reverse()`: 배열을 역순으로 재배치.
- `sort()`: 배열 데이터를 정렬.

```
배열의 일부를 반환
```

- `concat()`: 두개의 배열을 합침.
- `join()`: 배열 데이터 사이에 원하는 문자열을 넣어 구분자로 사용.
- `slice()`: 배열의 일부을 지정해서 가져옴.

```
데이터 순회
```

- `map()`: 모든 배열 데이터마다 반복 처리가 필요한 경우 사용.
- `filter()`: 특정 조건을 만족하는 데이터만 처리할 경우 사용.
- `reduce()`: 모든 데이터를 순화하면서 누적 연산이 필요한 경우 사용.

### 2) Map, Set

ES6 에서 새롭게 추가된 자료 구조 입니다. 기존 자바스크립트는 배열 이외의 자료구조가 따로 없었으나 이제 다른 언어들 처럼 다양한 자료구조를 사용할 수 있게 되었습니다.

Map과 Set 의 기본적인 개념은 기존언어들과 동일하며 일반적인 자료구조에 대해서는 [공통기초->프로그래밍언어개요](http://localhost:4000/lecture/core/101_basic_4.html#m6) 를 참고하기 바랍니다.

#### Map

> Map 은 new Map() 으로 선언 하고 map.set()을 이용해 키와 값을 추가 합니다.

자바스크립트의 Map 은 Key:Value 쌍으로 구성된 Object와 비슷한 구조로 볼 수 있지만 다음과 같은 차이가 있습니다.

- Object의 키는 문자열이며, Map의 키는 모든 값을 가질 수 있다.
- Object는 크기를 수동으로 추적해야하지만, Map은 크기를 쉽게 얻을 수 있다.
- Map은 삽입된 순서대로 반복된다.
- 객체(Object)에는 prototype이 있어 Map에 기본 키들이 있다.

언제 Object 혹은 Map을 사용할까?
실행 시점까지 키를 알수 없고, 모든 키가 동일한 type이며 모든 값들이 동일한 type일 경우에는 object를 대신해서 map을 사용하는 것이 좋습니다. 만일 각 개별 요소에 대해 적용해야 하는 로직이 있다면 object를 사용하길 권장 합니다.

다음은 여러 유형의 Map 사용 예 입니다.

```
const map = new Map();
map.set("2019101","홍길동");
map.set("2019102","김사랑");
map.set("2019103","강동수");

console.log(map.get("2019101"));
map.delete("2019103")
console.log(map.has("2019103"));

map.forEach((value, key) => console.log(key+" , "+value));

for(let item of map ) {
  console.log(item[0]+" , "+item[1]);
}

for(let [key, value] of map ) {
  console.log(key+" , "+value);
}

const keys = map.keys();
for(let key of keys) {
  console.log(map.get(key));
}
```

- `forEach` 의 인자는 `value, key, map object` 입니다.
- `for-of` 형태를 사용하는 경우 배열로 키(0), 값(1)이 전달 됩니다.
- `map.keys()`로 키값의 집합인 MapIterator 객체를 받아 for-of 를 이용합니다.

#### Set

> Set 은 중복된 값을 허용하지 않고 입력된 순서에 따라 데이터를 저장하는 자료구조 입니다. set.add() 를 이용해 데이터를 추가할 수 있고 데이터 관리를 위한 메서드가 제공 됩니다.

배열과 유사하지만 다음과 같은 차이가 있습니다.

- `indexOf()`를 사용하여 배열내에 특정 요소가 존재하는지 확인하는 것은 느리다.
- 배열에선 해당 요소를 배열에서 잘라내야 하는 반면 Set은 삭제 기능을 제공한다.
- NaN은 배열에서 indexOf메서드로 찾을 수 없다.
- Set객체는 값의 유일성을 보장하기 때문에 직접 요소의 중복성을 확인할 필요가 없다.

```
const set = new Set();
set.add("홍길동");
set.add("김사랑");
set.add("강동수");

set.delete("강동수")
console.log(set.has("강동수"));

set.forEach((value) => console.log(value));

for(let item of set ) {
  console.log(item);
}
```

Set 은 배열로 배열은 Set 으로 변경이 가능합니다. 배열에서 Set 으로 변환될 경우 중복된 값은 제거 됩니다.

```
let arr = Array.from(set);

let newSet = new Set([1,2,3,4,3]);
```

-------------------------------



## 함수(Function)

함수의 개념은 대부분의 프로그램 언어에서 존재하지만 특히 자바스크립트는 함수를 변수에 할당 할수 있으며 인자로 함수를 전달하거나 콜백함수를 구현하는 형태등 다양한 함수 활용을 보여주고 있습니다.

이러한 특징들과 함께 최근의 함수형 프로그래밍(FP: Functional Programming) 개념도 자바스크립트에서 지원되고 있습니다.

#### 함수선언

> 기본적으로 function 키워드로 선언하며 인자를 가질 수 있습니다. 자바스크립트는 타입을 명시하지 않기 때문에 리턴값의 유무와 상관없이 함수 선언부에 리턴 데이터에 대한 선언은 없습니다. 필요시 함수 바디에서 return 문을 사용해 값을 반환하면 됩니다.

- 인자의 매개변수 역시 타입없이 갯수에 따라 변수명을 나열.
- 함수안에 사용되는 변수는 block-scoped 인 let 이나 const 사용을 권장.
- 함수안에 또다른 함수를 정의할 수 있습니다.

```
function calc(a, b) {
  let sum1 = a + b;
  sum2 = a + b;
	return sum1;
}

console.log(calc(20, 30));  // 50
console.log(sum2);  //50
console.log(sum1);  //Error - not defined
```

#### First Class Object

> 자바스크립트에서 함수는 일급객체라고도 하며 다음과 같은 조건을 만족하는 객체를 말합니다.

- 변수나 데이터 구조안에 담을 수 있다.
- 파라미터로 전달 할 수 있다.
- 반환값(return value)으로 사용할 수 있다.
- 할당에 사용된 이름과 관계없이 고유한 구별이 가능하다.
- 동적으로 속성 할당이 가능하다.

#### 익명함수(Anonymous Function)

> 익명함수는 이름이 없는 함수로 변수에 함수를 구현하거나 함수를 리턴하는 형태가 가능하며 이를 사용하면 소위 콜백 함수의 구현이 가능해 집니다.

```
var calc1 = function(a, b) {
  return a+b;
}

function calc2(func) {
  console.log(func(20,30));
}

console.log(calc1(20,30));
calc2(calc1);
```

#### 콜백함수(Callback Function)

> 자바스크립에서 콜백함수는 특히 이벤트 처리에 많이 사용됩니다. 특정 UI에서 이벤트가 발생되었을때 처리될 코드를 익명함수에 넣고 콜백되어 처리될 수 있도록 하는 형식 입니다.

다음은 제곱을 구하는 함수에서 콜백함수를 호출하는 예 입니다. 콜백함수의 기능은 단순히 값을 콘솔에 출력하고 있습니다. setTimeout 함수는 일정시간 후에 동작을 정의합니다. 여기서는 200밀리초 이후 callback을 호출 하며 파라미터로 제곱값을 전달하게 되어 있습니다.

```
function square(x, callback) {
    setTimeout(callback, 200, x*x);
}
 
square(2, function(number) {
    console.log(number);
});
```

#### 자료구조의 값에 함수 사용

> 앞에서 언급한것 처럼 함수를 객체의 속성으로 사용할 수 있으며 Map 의 Value 혹은 배열의 원소로도 사용할 수 있습니다.

```
// 배열원소로 함수 선언.
let funcArr = [function() {console.log("v1")},"v2"];

// 맵원소로 함수 선언.
let mapArr = new Map();
mapArr.set("calcFunc",function(n1,n2) {return n1*n2});

// 객체의 속성으로 함수 선언.
let student = {
  'id': 2019101,
  'name': '홍길동',
  'score': function() {
    alert('A+');
  }
}

console.log(funcArr[0]());
console.log(mapArr.get("calcFunc")(20,10));
console.log(student.id);
student.score();
```

------------------------------------------



## 객체와 클래스

### 1) 객체(Object)

> 객체지향에서 객체는 우리눈에 보이는 구체화된 대상을 의미합니다. 객체는 속성과 행위로 정의 할 수 있으며 객체를 정의할 수 있는 틀을 클래스(Class)라고 합니다. 클래스는 멤버변수와 메서드로 정의하게 되고 클래스로 부터 객체를 생성(인스턴스)해서 사용하는 개념 입니다.

- ES6에서 클래스가 나오기 이전에는 Object 타입을 주로 사용 해서 객체를 정의 했습니다.
- Premitive 타입과 달리 참조형이며 배열도 객체 입니다.
- 객체는 속성의 모음이며 속성은 Key:Value 구조를 가집니다.
- 속성값이 함수인 경우 메서드(Method) 라고 표현 합니다.

#### 객체 리터럴을 이용한 객체 생성(JSON)

> 최근 프로그램 개발에 많이 쓰이는 JSON은 포맷은 JavaScript Object Notation 으로 자바스크립트에서 사용하는 객체 표기법을 의미 합니다.

자바스크립트 객체를 단순화 해서 표현하면 `Key:Value` 형태의 일종의 맵 혹은 딕셔너리형태라고 할 수 있습니다. 앞에서 언급한것 처럼 객체의 값으로 함수를 사용할 수 있기 때문에 클래스와 유사한 형태가 되는 것입니다. 객체 이니셜라이저(Object Initializer)라고도 합니다.

다음은 자바스크립트 객체의 사용 예 입니다.

```
let student = {
  'id': 2019101,
  'name': '홍길동',
  'scores': [95,80,91,85],
  'getTotalScore': function() {
    return this.scores.reduce((prev, curr) => prev + curr);
  }
}

console.log(student.getTotalScore());
```

#### 생성자를 이용한 객체 생성

만일 클래스와 같이 구체적인 값을 가지지 않는 형태를 미리 선언하고 객체를 생성하려면 다음과 같이 생성자 함수를 정의하고 사용할 수 있습니다.

```
function Product(name, price) {
  this.name = name;
  this.price = price;
  this.getInfo = function() {
    return this.name + " , " + this.price;
  }
}

let p1 = new Product("애플 아이폰",1000000);
let p2 = new Product();
p2.name = "삼성 갤럭시"
p2.price = 1100000;

console.log(p1.getInfo());
console.log(p2.getInfo());
```

### 2) 클래스(Class)

ES6에서 부터 지원되기 시작했으며 좀 더 객체지향 개념에 가까운 객체 사용을 가능하게 합니다. 앞에서 생성자 기반의 객체 선언을 살펴 보았는데 객체의 함수를 `this.getInfo` 와 같이 정의 하는 방법은 사실 좋은 방법이 아닙니다.

이유는 객체를 생성할때마다 동일한 함수도 매번 생성되기 때문으로 이를 효과적으로 처리하려면 함수의 경우 `Product.prototype.getInfo = function () {}` 처럼 정의해 주어야 합니다만 이경우 객체 선언부와 함수 선언부가 분리 되어 코드 관리가 불편하게 됩니다.

당연히 클래스를 사용하면 이런 문제점들을 해결할 수 있습니다.

#### 클래스 구조

> 새로운 class 키워드로 선언 합니다. 클래스 이름은 보통 대문자로 시작합니다.

```
class 클래스명 {
  constructor(인자..) {
    this.var = 인자;
    ...
  }

  메서드() {
  }

  get 메서드() {
    return ..
  }

  set 메서드() {

  }
}
```

다음은 클래스 문법에 따른 클래스 사용 예 입니다.

```
class Product {
  constructor(name, price)  {
    this.name = name;
    this.price = price;
  }

  getInfo() {
    return this.name + " , " + this.price;
  }
}

let p1 = new Product("애플 아이폰",1000000);
let p2 = new Product();
p2.name = "삼성 갤럭시"
p2.price = 1100000;

console.log(p1.getInfo());
console.log(p2.getInfo());
```

- 함수와 마찬가지로 클래스를 익명으로 선언할수도 있고 변수에 할당할수도 있다.
- new 연산을 통해 호출되는 것은 클래스 이름이 아니라 생성자 메서드 이다.
- 클래스 바디에는 메서드 선언만 가능하고 다른 언어와 같이 필드(멤버) 선언은 불가능하다.(추후 지원예정)
- 클래스 내부에서 선언한 속성은 클래스인스턴스를 가리키는 this에 바인딩 한다.

#### getter, setter

> 보통 클래스 필드에 접근할때 직접 변수에 접근하는 형태가 아닌 getter, setter 메서드를 통한 접근방법을 사용합니다. 클래스 입장에서는 외부에 값을 전달하거나 외부로 부터 가지고 올때 추가적인 조작이 가능하기 때문이고 내부 구조를 캡슐화 하는데에도 유리하기 때문입니다.

자바스크립트 클래스에서는 get, set 메서드를 정의 할 수 있고 해당 메서드는 함수호출이 아닌 클래스의 필드개념으로 사용하게 됩니다.

```
class Product {
  constructor(name, price)  {
    this.name = name;
    this.price = price;
  }

  get printName() {
    return "제품명:"+this.name;
  }

  set downPrice(price) {
    this.price = price;
  } 
}

let p = new Product("애플아이폰",1000000);
console.log(p.printName);

p.downProce = 500000;
console.log(p.price);
```

------