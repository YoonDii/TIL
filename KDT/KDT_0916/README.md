### 0916

# JavaScript-2

### 브라우저 (browser)

- URL로 웹(WWW)을 탐색하며 서버와 통신하고, HTML 문서나 파일을 출력하는 GUI 기반의 소프트웨어 
- 인터넷의 컨텐츠를 검색 및 열람하도록 함 
- “웹 브라우저”라고도 함 
- 주요 브라우저 
  - Google Chrome, Mozilla Firefox, Microsoft Edge, Opera, Safari



### DOM(Document Object Model)

브라우저에서 할 수 있는 일

- DOM 조작 
  - 문서(HTML) 조작 
-  BOM 조작  
  - navigator, screen, location, frames, history, XHR  
- JavaScript Core (ECMAScript) 
  -  Data Structure(Object, Array), Conditional Expression, Iteration



#### DOM 이란?

- HTML, XML과 같은 문서를 다루기 위한 문서 프로그래밍 인터페이스 
- 문서를 구조화하고 구조화된 구성 요소를 하나의 객체로 취급하여 다루는 논리적 트리 모델 
- 문서가 구조화되어 있으며 각 요소는 객체(object)로 취급 
- 단순한 속성 접근, 메서드 활용뿐만 아니라 프로그래밍 언어적 특성을 활용한 조작 가능 
- 주요 객체 
  - window : DOM을 표현하는 창. 가장 최상위 객체 (작성 시 생략 가능) 
  - document : 페이지 컨텐츠의 Entry Point 역할을 하며,  등과 같은 수많은 다른 요소들을 포함 
  - navigator, location, history, screen

- DOM - 해석
  - 파싱 (Parsing) 
    - 구문 분석, 해석 
    - 브라우저가 문자열을 해석하여 DOM Tree로 만드는 과정



#### BOM 이란?

- Browser Object Model  
- 자바스크립트가 브라우저와 소통하기 위한 모델 
- 브라우저의 창이나 프레임을 추상화해서 프로그래밍적으로 제어할 수 있도록 제공하는 수단 
  - 버튼, URL 입력창, 타이틀 바 등 브라우저 윈도우 및 웹 페이지 일부분을 제어 가능 
-  window 객체는 모든 브라우저로부터 지원받으며 브라우저의 창(window)를 지칭

-------------

### DOM 조작

#### 개념

- Document는 문서 한 장(HTML)에 해당하고 이를 조작 
- DOM 조작 순서 
  - 선택 (Select)  
  - 변경 (Manipulation)

<img src="https://dinfree.com/assets/img/js_3-1.png" alt="js_3-1" style="zoom: 33%;" />

#### DOM 객체의 상속 구조

-  EventTarget  
  - Event Listener를 가질 수 있는 객체가 구현하는 DOM 인터페이스 
-  Node 
  - 여러 가지 DOM 타입들이 상속하는 인터페이스

- Element 
  - Document 안의 모든 객체가 상속하는 가장 범용적인 인터페이스 
  - 부모인 Node와 그 부모인 EventTarget의 속성을 상속 
-  Document 
  - 브라우저가 불러온 웹 페이지를 나타냄 
  - DOM 트리의 진입점(entry point) 역할을 수행
-  HTMLElement
  -  모든 종류의 HTML 요소 
  - 부모 element의 속성 상속

--------------------------

#### DOM 선택

####  – 선택 관련 메서드 

- `document.querySelector(selector)`
  -  제공한 선택자와 일치하는 element 하나 선택 
  - 제공한 CSS selector를 만족하는 첫 번째 element 객체를 반환 (없다면 null) 
- `document.querySelectorAll(selector)` 
  - 제공한 선택자와 일치하는 여러 element를 선택 
  - 매칭 할 하나 이상의 셀렉터를 포함하는 유효한 CSS selector를 인자(문자열)로 받음 
  - 지정된 셀렉터에 일치하는 NodeList를 반환

- `getElementById(id)`  
- `getElementsByTagName(name)` 
- `getElementsByClassName(names)`  
- `querySelector()`, `querySelectorAll()`을 사용하는 이유 
  - `id`, `class` 그리고` tag` 선택자 등을 모두 사용 가능하므로, 더 구체적이고 유연하게 선택 가능
  -  ex) `document.querySelector('#id’)`, `document.querySelectAll(‘.class')`

####  

#### - 선택 메서드별 반환 타입

1. 단일 element
   - `getElementById() `
   - `querySelector()` 
2. HTMLCollection  
   - `getElementsByTagName()`  
   - `getElementsByClassName()`
3. NodeList 
   - `querySelectorAll()`

```html
document.getElementsByTagName("tag_name")
document.getElementById("id_name")
document.getElementsByClassName("class_name")
document.getElementsByName("name_attribute")

/*모든 getElementsByXXX() 함수의 경우 동일 조건의 모든 노드를 목록으로 가져옴.
getElementByName()의 경우 태그의 name 속성으로 노드를 찾음.*/

let elist = document.getElementsByTagName("h2");

for(let el of elist) {
	console.log("##"+el.tagName);	
}
-------------------------------------------------------------------------------
document.querySelector("#main, #title, #footer");
document.querySelectorAll("p.note, p.tip")
콤마로 구분된 여러 셀렉터를 나열 할 수 있으며 해당 조건에 맞는 첫번째 노드만 가져옴.
해당 조건의 모든 노드를 가지고 오려면 querySelectorAll()을 사용 함.
```



#### \- HTMLCollection & NodeList

- 둘 다 배열과 같이 각 항목에 접근하기 위한 index를 제공 (유사 배열) 
- HTMLCollection 
  - name, id, index 속성으로 각 항목에 접근 가능 
- NodeList 
  - index로만 각 항목에 접근 가능 
  - 단, HTMLCollection과 달리 배열에서 사용하는 forEach 메서드 및 다양한 메서드 사용 가능  
- 둘 다 Live Collection으로 DOM의 변경사항을 실시간으로 반영하지만, 
  - `querySelectorAll()`에 의해 반환되는 NodeList는 Static Collection으로 실시간으로 반영되지 않음



#### \- Collection

- Live Collection 
  - 문서가 바뀔 때 실시간으로 업데이트 됨 
  - DOM의 변경사항을 실시간으로 collection에 반영 
  - ex) HTMLCollection, NodeList 
- Static Collection (non-live)  
  - DOM이 변경되어도 collection 내용에는 영향을 주지 않음 
  - `querySelectorAll()`의 반환 NodeList만 static collection

----------------------------------------

### DOM 변경

#### \- 변경 관련 메서드 (Creation)

- `document.createElement()`  
  - 작성한 태그 명의 HTML 요소를 생성하여 반환

#### \- 변경 관련 메서드 (append DOM)

- `Element.append()`
  - 특정 부모 Node의 자식 NodeList 중 마지막 자식 다음에 Node 객체나 DOMString을 삽입  
  - 여러 개의 Node 객체, DOMString을 추가 할 수 있음 
  - 반환 값이 없음 
- `Node.appendChild()` 
  - 한 Node를 특정 부모 Node의 자식 NodeList 중 마지막 자식으로 삽입 (Node만 추가 가능) 
  - 한번에 오직 하나의 Node만 추가할 수 있음 
  - 만약 주어진 Node가 이미 문서에 존재하는 다른 Node를 참조한다면 새로운 위치로 이동



#### `ParentNode.append()` vs `Node.appendChild()`

- append()를 사용하면 DOMString 객체를 추가할 수도 있지만, `.appendChild()`는 Node 객체만 허용 
- append()는 반환 값이 없지만, `.appendChild()`는 추가된 Node 객체를 반환 
- append()는 여러 Node 객체와 문자열을 추가할 수 있지만, `.appendChild()`는 하나의 Node 객체만 추가할 수 있음



#### – 변경 관련 속성 (property)

- `Node.innerText`
  - Node 객체와 그 자손의 텍스트 컨텐츠(DOMString)를 표현 (해당 요소 내부의 raw text) (사람이 읽을 수 있는 요소만 남김) 
  - 즉, 줄 바꿈을 인식하고 숨겨진 내용을 무시하는 등 최종적으로 스타일링이 적용된 모습으로 표현  
- `Element.innerHTML` 
  - 요소(element) 내에 포함된 HTML 마크업을 반환 
  - [참고] XSS 공격에 취약하므로 사용 시 주의



#### XSS (Cross-site Scripting)

- 공격자가 입력요소를 사용하여 웹 사이트 클라이언트 측 코드에 악성 스크립트를 삽입 해 공격하는 방법  
- 피해자(사용자)의 브라우저가 악성 스크립트를 실행하며 공격자가 엑세스 제어를 우회하고 사용자를 가장 할 수 있도록 함

---------------------

### DOM 삭제 

#### - 삭제 관련 메서드

- `ChildNode.remove()` 
  - Node가 속한 트리에서 해당 Node를 제거  
- `Node.removeChild()`  
  - DOM에서 자식 Node를 제거하고 제거된 Node를 반환 
  - Node는 인자로 들어가는 자식 Node의 부모 Node

```html
document.createElement(element)        
document.removeChild(element)          
document.appendChild(element)          
document.replaceChild(element)                    
```



-------------

### DOM 속성 

#### – 속성 관련 메서드

- `Element.setAttribute(name, value)` 
  - 지정된 요소의 값을 설정 
  - 속성이 이미 존재하면 값을 갱신, 존재하지 않으면 지정된 이름과 값으로 새 속성을 추가 
- `Element.getAttribute(attributeName)` 
  - 해당 요소의 지정된 값(문자열)을 반환 
  - 인자(attributeName)는 값을 얻고자 하는 속성의 이름

----------------------------------------

### 디자인 요소 변경

자바스크립트에서의 이벤트 처리는 대부분 화면을 동적으로 변경하는것과 관련이 있습니다. DOM 요소를 이용해 특정 영역에 데이터를 표현하거나 혹은 감출 수 있으며 CSS 디자인 속성을 변경해 모양이나 색상등을 변경하는 것도 가능합니다.

#### 1) 디자인 요소 변경

디자인 변경은 CSS의 기본적인 구조와 동작원리를 이해하고 있다면 어려울것이 없다. 해당 요소의 style 속성변경, style 객체변경, 클래스 지정등의 방법으로 변경이 가능합니다.

#### style 속성변경

> 모든 HTML 태그는 style 속성을 가질수 있으므로 다음과 같이 setAttribute로 style 속성을 변경할 수 있습니다.

```
document.getElementById('box1').setAttribute('style','background-color:yellow');
```

- 이 방법은 인라인 스타일시트와 같은 방법이며 구조적이지 않아 권장되지 않음.

#### style 객체 변경

> style 속성 대신 요소의 style 객체의 속성값들을 변경하는 형식 입니다.

```
document.getElementById('box1').style.backgroundColor = 'yellow';
```

- 이방법은 좀 더 구조적인 방법이며 프로그램 친화적인 형태임.
- css 디자인 속성 이름은 `-` 로 연결되지만 이경우 `Camel Case`로 연결해야 함.
- 예를 들어 `background-color` 속성은 `backgroundColor` 와 같이 사용.
- style 속성 변경보다는 좋은 방법이지만 많은 디자인 속성을 변경할때는 바람직 하지 않음.

#### 클래스 지정

> 별도의 디자인 클래스를 지정해 놓고 해당 요소의 class 속성을 지정하는 형태 입니다.

```
document.getElementById('box1').className = 'bgyellow';
```

- 이경우 별도의 디자인 클래스가 정의 되어 있어야 함.
- 가장 권장되는 방법임.



#### 2) 화면 숨기기

화면 구성요소를 상황에 따라 숨기거나 보여주는 방법은 UI 측면에서 매우 유용합니다. CSS 를 이용해 요소를 보여주거나 숨기는 두가지 방법은 다음과 같습니다.

#### display:none

> 요소를 숨기며 요소가 차지하는 공간도 함께 사라집니다. 다시 보이게 하려면 속성을 block 으로 변경하면 됩니다.

```
document.getElementById('box1').style.display = 'none';
```

#### visibility:hidden

> 요소를 숨기며 차지하는 공간도 유지하는 속성 입니다. width, height 가 지정되어 있으면 내용은 보이지 않아도 공간은 존재하게 됩니다. 다시 보이게 하려면 visible 이라고 하면 됩니다.

```
document.getElementById('box1').style.visibility = 'hidden';
```

------