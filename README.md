# 간단한 게시판 RESTAPI server

RESTAPI를 사용하여 CRUD를 할 수 있는 간단한 게시판 입니다.  
간단하게 계정을 생성하여 로그인 할 수 있고, 게시판의 제목과 글을 생성, 읽기, 수정, 삭제가 가능합니다.  
Python 언어와 Django, Django Rest Framework 를 사용하여 구현하였습니다.

---

## 사용 언어, 프레임 워크 및 개발 환경

---

- Python v3.9
- Django v3.2.8
- DjangoRestFramework v3.12.4
- SQLite3
- MacOS v11.6

## 설치 방법

---

1. Python 설치  
   최신 버전(3.9이상)의 Python을 설치합니다.  
    설치는 다음을 참고하여 합니다.  
    [MacOS에 파이썬3 설치.](https://python-guide-kr.readthedocs.io/ko/latest/starting/install3/osx.html#install3-osx)  
    [Windows에 파이썬3 설치.](https://python-guide-kr.readthedocs.io/ko/latest/starting/install3/win.html#install3-windows)  
    [Linux에 파이썬3 설치.](https://python-guide-kr.readthedocs.io/ko/latest/starting/install3/linux.html#install3-linux)

2. Python 가상환경 설치  
   본 프로젝트는 Python 가상환경을 사용하여 동작합니다. 두가지 이상의 방법으로 가상환경을 설치 및 사용 할 수 있습니다. Pipenv를 사용하여 할 것을 추천합니다. python2 에 pip 가 설치되어 있는 경우 pip 대신 pip3명령어를 사용하여 설치합니다.

   - Pipenv

     1. Pipenv 설치

     ```bash
     pip install pipenv
     ```

   - Virtualenv

     1. Virtualenv 설치

     ```bash
     pip install virtualenv
     ```

3. 프로젝트 다운로드  
   Github에서 직접 ZIP파일을 다운로드하여 압축을 해제하거나, Git clone명령어를 사용하여 다운로드 합니다.

   ```bash
   git clone https://github.com/miranaky/board.git
   ```

4. 가상환경 생성 및 활성화  
   프로젝트를 실행하기 위해서는 우선 가상 환경을 생성/활성화 해야 합니다.
   다운로드 한 프로젝트 디렉토리로 들어갑니다.

   ```bash
   cd board
   ```

   이후 가상환경을 생성/활성화 하고 필요한 패키지들을 설치해 줍니다.

   - Pipenv 사용시

     1. Pipenv 환경 생성 및 활성화

        ```bash
        pipenv shell
        ```

     2. 패키지 설치

        ```bash
        pipenv install
        ```

   - Virtualenv 사용시

     1. 가상환경 생성  
        board 디렉토리에서 가상환경을 생성합니다.

        ```bash
        virtualenv venv
        ```

     2. 가상환경 활성화  
        생성한 가상환경을 활성화 합니다.

        ```bash
        source venv/bin/activate
        ```

     3. 패키지 설치  
        필요한 패키지들을 설치합니다

        ```bash
        pip install -r requirements.txt
        ```

5. DB 초기화  
   가상환경 준비 및 필요한 패키지가 모두 설치되었다면 DB초기화를 해야 합니다.  
   Pipenv shell 혹은 가상환경이 활성화 되어 있는 상태로 실행합니다.

   ```bash
   python manage.py makemigration
   python manage.py migrate
   ```

   관리자 계정이 별도로 필요하다면 Username과 Password등을 넣고 생성해줍니다.

   ```bash
   python manage.py createsuperuser
   ```

## 실행 방법

---

실제 배포가 아닌 간단한 확인을 하기 위해서 다음과 같이 실행합니다.
실행시에는 Pipenv shell 혹은 가상환경이 활성화 되어 있는 상태로 실행합니다.

```bash
python manage.py localhost:8800
```

### 추가 사항

테스트를 위해서 django-seed를 이용한 가짜 파일 생성 가능합니다.  
다음 명령어를 통하여 가짜 계정 30개와 가짜 게시글 100 개를 생성합니다.  
실행시에는 Pipenv shell 혹은 가상환경이 활성화 되어 있는 상태로 실행합니다.

    # 가짜 계정 30개 생성
    python manage.py user_seed

    # 가짜 게시글 100개 생성
    python manage.py post_seed

---

# REST API

## Get list of posts

> 게시물 목록 가져오기  
> 저장되어 있는 게시물들을 기본 30개 단위로 보여줍니다.  
> limit와 offset 파라미터를 이용하여 조절 가능합니다.

### Request

`GET /api/v1/posts/`

    curl -i -H 'Accept: applicatino/json' http://localhost:8800/api/v1/posts/

### Response

    HTTP/1.1 200 OK
    Date: Wed, 20 Oct 2021 13:29:20 GMT
    Server: WSGIServer/0.2 CPython/3.9.6
    Content-Type: application/json
    Vary: Accept, Cookie
    Allow: GET, POST, HEAD, OPTIONS
    X-Frame-Options: DENY
    Content-Length: 10304
    X-Content-Type-Options: nosniff
    Referrer-Policy: same-origin

    {
    "count": 55,
    "next": "http://localhost:8800/api/v1/posts/?limit=30&offset=30",
    "previous": null,
    "results": [
    {
    "id": 2,
    "author": {
    "id": 1,
    "username": "SuperUser"
    },
    "created": "2021-10-20T14:55:27.873918+09:00",
    "updated": "2021-10-20T15:25:36.871146+09:00",
    "title": "second",
    "content": "second post content"
    },
    {
    "id": 3,
    "author": {
    "id": 1,
    "username": "SuperUser"
    },
    "created": "2021-10-20T15:37:49.704321+09:00",
    "updated": "2021-10-20T15:38:09.608786+09:00",
    "title": "title update",
    "content": "contents update"
    },
    ... 중략
    ]
    }

---

## Create a new post by authenticated user

> 새로운 게시물 생성하기  
> 인증된 사용자(로그인 된 사용자)를 통해서 새로운 게시물을 1개 생성합니다.

### Request

`POST /api/v1/posts/`

> Header 에 Authorization: X-JWT {TOKEN} 을 추가해서 보낸다.  
> 데이터는"title"과 "content"를 작성해서 보낸다.

    curl -i -H 'Accept: application/json' -H 'Authorization: X-JWT {TOKEN}' -d 'title=New Post with kaengkaeng&content=Content created by kaengkaeng'  http://localhost:8800/api/v1/posts/

### Response

    HTTP/1.1 201 Created
    Date: Wed, 20 Oct 2021 14:11:32 GMT
    Server: WSGIServer/0.2 CPython/3.9.6
    Content-Type: application/json
    Vary: Accept
    Allow: GET, POST, HEAD, OPTIONS
    X-Frame-Options: DENY
    Content-Length: 218
    X-Content-Type-Options: nosniff
    Referrer-Policy: same-origin

    {"id":58,"author":{"id":2,"username":"kaengkaeng"},"created":"2021-10-20T23:11:32.923112+09:00","updated":"2021-10-20T23:11:32.923161+09:00","title":"New Post with kaengkaeng","content":"Content created by kaengkaeng"}

---

## Create a new post by anonymous user

> 새로운 게시물 생성하기  
> 인증되지 않은 사용자를 통해서 새로운 게시물을 1개 생성할 경우.

### Request

`POST /api/v1/posts/`

    curl -i -H 'Accept: application/json'  -d 'title=New Post with kaengkaeng&content=Content created by kaengkaeng'  http://localhost:8800/api/v1/posts/

### Response

    HTTP/1.1 401 Unauthorized
    Date: Wed, 20 Oct 2021 14:18:47 GMT
    Server: WSGIServer/0.2 CPython/3.9.6
    Vary: Accept, Cookie
    Allow: GET, POST, HEAD, OPTIONS
    X-Frame-Options: DENY
    Content-Length: 0
    X-Content-Type-Options: nosniff
    Referrer-Policy: same-origin

---

## Get a post

> 존재하는 특정한 게시글 가져오기

### Request

`GET /api/v1/posts/{id}`

     curl -i -H 'Accept: application/json'  http://localhost:8800/api/v1/posts/57

### Response

    HTTP/1.1 200 OKDate: Wed, 20 Oct 2021 14:12:46 GMT
    Server: WSGIServer/0.2 CPython/3.9.6
    Content-Type: application/json
    Vary: Accept, Cookie
    Allow: GET, PUT, DELETE, HEAD, OPTIONS
    X-Frame-Options: DENY
    Content-Length: 218
    X-Content-Type-Options: nosniff
    Referrer-Policy: same-origin

    {"id":58,"author":{"id":2,"username":"kaengkaeng"},"created":"2021-10-20T23:11:32.923112+09:00","updated":"2021-10-20T23:11:32.923161+09:00","title":"New Post with kaengkaeng","content":"Content created by kaengkaeng"}

---

## Get a non-existent post

> 존재하지 않는 게시글 가져오는 경우

### Request

`GET /api/v1/posts/{id}`

     curl -i -H 'Accept: application/json'  http://localhost:8800/api/v1/posts/99999

### Response

    HTTP/1.1 404 Not Found
    Date: Wed, 20 Oct 2021 14:14:35 GMT
    Server: WSGIServer/0.2 CPython/3.9.6
    Vary: Accept, Cookie
    Allow: GET, PUT, DELETE, HEAD, OPTIONS
    X-Frame-Options: DENY
    Content-Length: 0
    X-Content-Type-Options: nosniff
    Referrer-Policy: same-origin

---

## Update a post by created user

> 게시글을 작성한 유저가 게시글을 수정

### Request

`PUT /api/v1/posts/{id}`

> title,content 동시 수정  
> {TOKEN} 은 [Get token by login](#get-token-by-login) 에서 받은 값을 사용.

     curl -i -H 'Accept: application/json' -H 'Authorization: X-JWT {TOKEN}' -d 'title= Post update with kaengkaeng&content=Content updated by kaengkaeng' -X PUT http://localhost:8800/api/v1/posts/58

### Response

    HTTP/1.1 200 OK
    Date: Wed, 20 Oct 2021 14:28:58 GMT
    Server: WSGIServer/0.2 CPython/3.9.6
    Content-Type: application/json
    Vary: Accept
    Allow: GET, PUT, DELETE, HEAD, OPTIONS
    X-Frame-Options: DENY
    Content-Length: 221
    X-Content-Type-Options: nosniff
    Referrer-Policy: same-origin

    {"id":58,"author":{"id":2,"username":"kaengkaeng"},"created":"2021-10-20T23:11:32.923112+09:00","updated":"2021-10-20T23:28:58.551622+09:00","title":"Post update with kaengkaeng","content":"Content updated by kaengkaeng"}

---

## Update a post by different user

> 게시글을 작성하지 않은 유저가 게시글을 수정  
> {TOKEN} 은 [Get token by login](#get-token-by-login) 에서 받은 값을 사용.

### Request

`PUT /api/v1/posts/{id}`

     curl -i -H 'Accept: application/json' -H 'Authorization: X-JWT {TOKEN~}' -d 'title= Post update with kaengkaeng&content=Content updated by kaengkaeng' -X PUT http://localhost:8800/api/v1/posts/58

### Response

    HTTP/1.1 401 Unauthorized
    Date: Wed, 20 Oct 2021 14:35:43 GMT
    Server: WSGIServer/0.2 CPython/3.9.6
    Vary: Accept
    Allow: GET, PUT, DELETE, HEAD, OPTIONS
    X-Frame-Options: DENY
    Content-Length: 0
    X-Content-Type-Options: nosniff
    Referrer-Policy: same-origin

---

## Delete a post by created user

> 게시글을 작성한 유저가 게시글을 삭제

### Request

`PUT /api/v1/posts/{id}`

> {TOKEN} 은 [Get token by login](#get-token-by-login) 에서 받은 값을 사용.

     curl -i -H 'Accept: application/json' -H 'Authorization: X-JWT {TOKEN}' -X DELETE http://localhost:8800/api/v1/posts/57

### Response

    HTTP/1.1 200 OK
    Date: Wed, 20 Oct 2021 14:38:10 GMT
    Server: WSGIServer/0.2 CPython/3.9.6
    Vary: Accept
    Allow: GET, PUT, DELETE, HEAD, OPTIONS
    X-Frame-Options: DENY
    Content-Length: 0
    X-Content-Type-Options: nosniff
    Referrer-Policy: same-origin

---

## Delete a post by different user

> 게시글을 작성하지 않은 유저가 게시글을 삭제

### Request

`PUT /api/v1/posts/{id}`

> {TOKEN} 은 [Get token by login](#get-token-by-login) 에서 받은 값을 사용.

     curl -i -H 'Accept: application/json' -H 'Authorization: X-JWT {TOKEN~}' -X DELETE http://localhost:8800/api/v1/posts/58

### Response

    HTTP/1.1 401 Unauthorized
    Date: Wed, 20 Oct 2021 14:39:30 GMT
    Server: WSGIServer/0.2 CPython/3.9.6
    Vary: Accept
    Allow: GET, PUT, DELETE, HEAD, OPTIONS
    X-Frame-Options: DENY
    Content-Length: 0
    X-Content-Type-Options: nosniff
    Referrer-Policy: same-origin

---

## Delete a non-existent post

> 존재하지 않는 게시글을 삭제

### Request

`PUT /api/v1/posts/{id}`

> {TOKEN} 은 [Get token by login](#get-token-by-login) 에서 받은 값을 사용.

     curl -i -H 'Accept: application/json' -H 'Authorization: X-JWT {TOKEN}' -X DELETE http://localhost:8800/api/v1/posts/99999

### Response

    HTTP/1.1 404 Not Found
    Date: Wed, 20 Oct 2021 14:39:54 GMT
    Server: WSGIServer/0.2 CPython/3.9.6
    Vary: Accept
    Allow: GET, PUT, DELETE, HEAD, OPTIONS
    X-Frame-Options: DENY
    Content-Length: 0
    X-Content-Type-Options: nosniff
    Referrer-Policy: same-origin

---

## Create a new user

> 새로운 계정 생성하기

### Request

`POST /api/v1/users/`

> 데이터는 "username", "first_name","last_name","email","password"를 작성해서 보낸다.

    curl -i -H 'Accept: application/json' -d 'username=kaengkaeng2&first_name=Sungmuk&last_name=Kang&email=kaengkaeng2@kaengkaeng.com&password=654321'  http://localhost:8800/api/v1/users/

### Response

    HTTP/1.1 201 Created
    Date: Wed, 20 Oct 2021 14:46:39 GMT
    Server: WSGIServer/0.2 CPython/3.9.6
    Content-Type: application/json
    Vary: Accept, Cookie
    Allow: POST, OPTIONS
    X-Frame-Options: DENY
    Content-Length: 113
    X-Content-Type-Options: nosniff
    Referrer-Policy: same-origin

    {"id":24,"username":"kaengkaeng2","first_name":"Sungmuk","last_name":"Kang","email":"kaengkaeng2@kaengkaeng.com"}

---

## Get token by login

> 로그인 하고 jwt token 얻기  
> X-JWT token은 게시글 생성,수정,삭제에 사용됩니다.

### Request

`POST /api/v1/users/login`

> 데이터는 "username", "password"를 작성해서 보낸다.  
> X-JWT Token을 받게된다.

    curl -i -H 'Accept: application/json' -d 'username=kaengkaeng2&password=654321'  http://localhost:8800/api/v1/users/login

### Response

    HTTP/1.1 200 OK
    Date: Wed, 20 Oct 2021 14:50:22 GMT
    Server: WSGIServer/0.2 CPython/3.9.6
    Content-Type: application/json
    Vary: Accept, Cookie
    Allow: OPTIONS, POST
    X-Frame-Options: DENY
    Content-Length: 105
    X-Content-Type-Options: nosniff
    Referrer-Policy: same-origin

    {"token":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJwayI6MjR9.BM1dUlV1apYiIqKPwtjWF5QAapsKvlRwgQ1h8dWW28o"}

---
