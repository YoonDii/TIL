### 0728

# 딕셔너리(Dictionary)

> 딕셔너리는 해시테이블(Hash Table)을 이용하여 Key와 Value을 저장함.
>
> 해시함수 : 임의 길이의 데이터를 고정 길이의 데이터로 매핑하는 함수.
>
> 해시 : 해시 함수를 통해 얻어진 값.

#**파이썬의 딕셔너리는 해시 함수와 해시 테이블을 이용하여 삽입, 삭제, 수정, 조회 연산의 속도가 리스트보다 빠르다.**#



#### 📢딕셔너리 기본 문법

##### 1. 선언 

변수를 선언해줘야함.

***변수 = { "a":"apple"  ....}***

```python
a = {
    "a" : "apple"
    "b" : "banana"
    "c" : "charry"
}
print(a) 
#{"a" : "apple", "b" : "banana", "c" : "charry"}
```

##### 2.삽입/수정

내부에 해당 key가 없으면 삽입, 있으면 수정.

***딕셔너리[key] = Value***

```python
a = {
    "a" : "apple"
    "b" : "banana"
    "c" : "charry"
}
a["d"] = "durian"

print(a) 
#{"a" : "apple", "b" : "banana", "c" : "charry", "d" = "durian"}
```

##### 3. 삭제

내부에 존재하는 key에 대한 value 삭제 및 반환, 존재하지 않는 key에 대해서는 KeyError발생.

***딕셔너리.pop(key)***

```python
a = {
    "a" : "apple"
    "b" : "banana"
    "c" : "charry"
}
c = a.pop("c")

print(a) #{"a" : "apple", "b" : "banana", "c" : "charry"}
print(c) # charry
```

##### 3-1. 삭제(KeyError방지)

```python
a = {
    "a" : "apple"
    "b" : "banana"
    "c" : "charry"
}
d = a.pop("d" , "durian")

print(a) #{"a" : "apple", "b" : "banana", "c" : "charry"}
print(d) #durian
```

##### 4. 조회

 key에 해당하는 value반환

딕셔너리[key]  / 딕셔너리.get[key]

```python
a = {
    "a" : "apple"
    "b" : "banana"
    "c" : "charry"
}
print(a["a"])
#apple   ---->키가없으면 keyerror를 알려줌.
----------------------------------------------------------------------------
a = {
    "a" : "apple"
    "b" : "banana"
    "c" : "charry"
}
print(a.get("a"))
#apple  ---->키가 없으면 NONE을 알려주고 value가 있으면 value를 나타내줌.
```



#### 📢딕셔너리 메서드

##### 1. .keys()

딕셔너리의 key목록이 담긴 dict_keys 객체 반환

```python
a = {
    "a" : "apple"
    "b" : "banana"
    "c" : "charry"
}
print(a.keys())
#dict_keys(['a', 'b', 'c'])

--------------------------------------------------------------------------
a = {
    "a" : "apple"
    "b" : "banana"
    "c" : "charry"
}
for key in a.keys():
    print(key)
    #a
    #b
    #c
--------------------------------------------------------------------------    
a = {
    "a" : "apple"
    "b" : "banana"
    "c" : "charry"
}
for key in a:
    print(key)
    #a
    #b
    #c
```

##### 2. .values()

딕셔너리의 value 목록이 담긴 dict_values 객체 반환

```python
a = {
    "a" : "apple"
    "b" : "banana"
    "c" : "charry"
}
print(a.values())
#dict_values(['apple', 'banana', 'charry'])

--------------------------------------------------------------
a = {
    "a" : "apple"
    "b" : "banana"
    "c" : "charry"
}
for value in a.values():
    print(value)
    #apple
    #banana
    #charry
```

##### 3. .items()

딕셔너리의 (key,value) 쌍 목록이 담긴 dict_items 객체 반환

```python
a = {
    "a" : "apple"
    "b" : "banana"
    "c" : "charry"
}
print(a.items())
#dict_items([('a',apple'),('b', 'banana'), ('c','charry')])
------------------------------------------------------------------------
a = {
    "a" : "apple"
    "b" : "banana"
    "c" : "charry"
}
for item in a.item():
    print(item)
    #('a',apple')
    #('b', 'banana')
    #('c','charry')
  
--------------------------------------------------------------------------
a = {
    "a" : "apple"
    "b" : "banana"
    "c" : "charry"
}
for key, value in a.items():
    print(key, value)
    #a apple
    #b banana
    #c charry   
```



