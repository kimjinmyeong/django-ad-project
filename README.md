<img width="839" alt="image" src="https://github.com/kimjinmyeong/django-ad-project/assets/84405002/a67fecd9-7e39-409d-aea2-84c6e7d49356">


# django-ad-project
2023 국민대학교 웹서버컴퓨팅 AD 프로젝트입니다.

## 프로젝트 설명
`django` 를 활용하여 질문, 답변, 댓글 기능이 포함된 게시판 웹 애플리케이션 완성으로, 웹 애플리케이션 이름은 'Pybo' 입니다.

## 기술 스택
- python3
- django
- bootstrap
- sqlite3

## 팀 구성원
- [@kimjinmyeong](https://github.com/kimjinmyeong)
- [@scarleter99](https://github.com/scarleter99)
- [@yonghoya](https://github.com/yonghoya)

## 프로젝트 구조
```
├── common
│   └── migrations
├── config
├── pybo
│   ├── migrations
│   ├── templatetags
│   ├── tests
│   └── views
├── static
└── templates
    ├── common
    └── pybo
```
common : 사용자 로그인 관련 view, url 

config : 프로젝트 설정 및 주 url path 라우팅

pybo : 게시판 관련

static : bootstrap, css, jquery 파일 저장

templates : html 파일 저장

# 수행 과제
- [X] 1. 질문 및 답변 수정에 대한 히스토리 viewing (예를 들어, 질문이 n번 수정이 되었음을 나타내는 수치를 표시)

- [X] 2. 질문 댓글에 대한 페이지네이션과 정렬 기능 (질문 1개에 댓글이 여러 개 달릴 수 있다. 댓글이 100개라고 가정해 보자. 성능을 위해서라도 댓글 페이지는 반드시 필요할 것이다. 또 댓글을 보여 줄 때 최신순, 추천순 등으로 정렬하여 보여줄 기능도 필요하다. 답변 댓글에 대한 페이지네이션과 정렬 기능은 하지 않는다)

- [X] 3. 댓글 추천 기능 (질문댓글 추천과 답변 댓글 추천 기능이 필요하다)

- [X] 4. 댓글 수정 횟수 표시 기능   (예를 들어, 질문과 답변 댓글에 대해 n번 수정이 되었음을 나타내는 수치를 표시)

- [X] 5. comment view 분리 (03-11 챕터에서 comment view를 comment_question_view와  comment_answer_view 로 두 개의 view 파일로 분리하세요)

# 추가 구현
- 댓글 검색 기능 구현
- '/' path 로 이동할 때 보여주는 홈페이지 구현
- 이미 추천한 글을 다시 추천할 경우 에러 메시지 출력
- UnitTest 코드 작성
- Github Actions를 활용하여 CI 구현 (build, test)


