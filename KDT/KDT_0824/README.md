### 0824

# ORM

> Object-Relational-Mapping 
>
> • 객체 지향 프로그래밍 언어를 사용하여 호환되지 않는 유형의 시스템 간의 데이터를 변환하는 프로그래밍 기술 
>
> • 파이썬에서는 SQLAlchemy, peewee 등 라이브러리가 있으며 Django 프레임워크 에서는 내장 Django ORM을 활용



***“객체(object)로 DB를 조작한다.”***

```python
Genre.objects.all()  {classname.manager.querysetAPI}
```



- 모델 설계 및 반영

  - 1. 클래스를 생성하여 내가 원하는 DB의 구조를 만든다

    ```python
    class Genre(models.Model):
    	name = models.CharField(max_length=30)
    ```

  - 2. 클래스의 내용으로 데이터베이스에 반영하기 위한 마이그레이션 파일을 생성한다.

    `python manage.py makemigrations`  잊지말자..이거 안하면 생성안됌..

  - 3. DB에 migrate 한다.

    ` python manage.py migrate` 잊지말자2,,,이것도 안하면 반영안됌,,,



- Migration(마이그레이션)

  - Model에 생긴 변화를 DB에 반영하기 위한 방법

  - 마이그레이션 파일을 만들어 DB 스키마를 반영한다. 

  - `makemigrations` : 마이그레이션 파일 생성

  - `migrate` : 마이그레이션을 DB에 반영

    ```python
    BEGIN;
    --
    -- Create model Genre
    --
    CREATE TABLE "db_genre" (
    	"id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    	"name" varchar(30) NOT NULL
    );
    COMMIT;
    ```



- ORM 활용시 파이썬 코드는 반드시 shell에서!!

  ```python
  python manage.py shell_plus
  ```

  

- ORM 기본조작

  - Create

  ```python
  # 1. create 메서드 활용
  Genre.objects.create(name='발라드')
  
  # 2. 인스턴스 조작
  genre = Genre()
  genre.name = '인디밴드'
  genre.save()
  ```

  

  - Read

  ```python
  # 1. 전체 데이터 조회
  Genre.objects.all()
  # <QuerySet [<Genre: Genre object (1)>, <Genre:Genre object (2)>]>
  
  # 2. 일부 데이터 조회(get)
  Genre.objects.get(id=1)
  # <Genre: Genre object (1)>
  
  # 3. 일부 데이터 조회(filter)
  Genre.objects.filter(id=1)
  # <QuerySet [<Genre: Genre object (1)>]>
  ```

  

  - Update

  ```python
  # 1. genre 객체 활용
  genre = Genre.objects.get(id=1)
  
  # 2. genre 객체 속성 변경
  genre.name = '트로트’
  
  # 3. genre 객체 저장
  genre.save()
  ```

  

  - Delete

  ```python
  # 1. genre 객체 활용
  genre = Genre.objects.get(id=1)
  
  # 2. genre 객체 삭제
  genre.delete()
  ```

  

  