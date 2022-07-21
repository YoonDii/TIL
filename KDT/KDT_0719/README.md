### 0719

# 객체지향 프로그래밍

> 프로그램을 여러 개의 독립된 객체들과 그 객체들 간의 상호작용으로 파악하는 프로그래밍 방법

- ***파이썬은 모두 객체(object)로 이뤄져 있다.***

- ***객체(object)는 특정 타입의 인스턴스(instance) 이다.***
- 객체 지향 프로그래밍은 프로그램을 유연하고 변경이 용이하게 만들기 때문에 대규모 소프트웨어 개발에 많이 사용됨.
- 프로그래밍을 더 배우기 쉽게 하고 소프트웨어 개발과 보수를 간편하게 하며, 보다 직관적인 코드 분석을 가능하게 하는 장점이 있음.
- 절차지향 프로그래밍 ---> 테이터와 함수로 인한 변화
- 객체지향 프로그래밍 ---> 데이터와 기능(메소드) 분리, 추상화된 구조(인터페이스)

#### 1. 객체(odject)

- 타입(type) : 어떤 연산자(operator)와 조작(method)이 가능한가? 
- 속성(attribute) : 어떤 상태(데이터)를 가지는가? 
- 조작법(method) : 어떤 행위(함수)를 할 수 있는가?

```python
•사각형 - 클래스(class)
• 각 사각형 (R1,R2) – 인스턴스(instance)
• 사각형의 정보 - 속성(attribute)
• 가로 길이, 세로 길이
• 사각형의 행동/기능 – 메소드(method)
• 넓이를 구한다. 높이를 구한다.
```

#### 2. OOP

```python
# 클래스 정의 :객체들의 분류(class)
class MyClass:
pass
# 인스턴스 생성 :하나하나의 실체/예(instance)
my_instance = MyClass()
# 메서드 호출 :특정 데이터 타입/클래스의 객체에 공통적으로 적용 가능한 행위(함수)
my_instance.my_method()
# 속성 :특정 데이터 타입/클래스의 객체들이 가지게 될 상태/데이터를 의미
my_instance.my_attribute
```

##### 2-1. 객체비교

-  ==  --동등한(equal) 
  - 변수가 참조하는 객체가 동등한(내용이 같은) 경우 True 
  - 두 객체가 같아 보이지만 실제로 동일한 대상을 가리키고 있다고 확인해 준 것은 아님 
-  is -- 동일한(identical) 
  -  두 변수가 동일한 객체를 가리키는 경우 True 

```python
a = [1, 2, 3]
b = [1, 2, 3]
print(a == b , a is b) #Ture , False

a = [1, 2, 3]
b = a
print(a == b , a is b) #Ture, Ture
```

##### 2-2. 인스턴스

- 인스턴스 변수 
  -  인스턴스가 개인적으로 가지고 있는 속성(attribute) 
  - 각 인스턴스들의 고유한 변수 
  - 생성자 메소드에서 self.으로 정의 
  - 인스턴스가 생성된 이후 .으로 접근 및 할당

- 인스턴스 메소드

  - 인스턴스 변수를 사용하거나, 인스턴스 변수에 값을 설정하는 메소드  

  - 클래스 내부에 정의되는 메소드의 기본 

  -  호출 시, 첫번째 인자로 인스턴스 자기자신(self)이 전달됨

    ```python
    class Myclass
    	def instance_method(self,arg1, ...)
    #my_instance = MyClass()
    #my_instance.instance_method(…)
    ```

- self  

  - 인스턴스 자기자신 
  - 파이썬에서 인스턴스 메소드는 호출 시 첫번째 인자로 인스턴스 자신이 전달되게 설계 
    -  매개변수 이름으로 self를 첫번째 인자로 정의 
    -  다른 단어로 써도 작동하지만, 파이썬의 암묵적인 규칙

- 생성자(constructor) 메소드

  -  인스턴스 객체가 생성될 때 자동으로 호출되는 메소드 

  -  인스턴스 변수들의 초기값을 설정 

    - 인스턴스 생성 

    - ```python
      _init_메서드 자동호출
      ```

      ```python
      class Person:
          def _init_(self):
              print()
      person1 = Person()
      ```

- 소멸자(destructor) 메소드  

  - 인스턴스 객체가 소멸(파괴)되기 직전에 호출되는 메소드

    ```python
    class Person:
        def_del_(self):
            print()
    person1 = Person()
    del person1
    ```

    
    *심화*