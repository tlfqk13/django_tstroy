코딩 컨벤션
코드를 작성할 때, 사용되는 일정한 기준

PEP -> 파이썬 개선 제안서
PEP8 -> 파이썬 코드 가이드 라인

모델링 설계하는 방법
1. 어떤 필드가 필요한지 생각
2. 생각이되면 적어본다
3. 각 필드는 어떤 타입이 되어야하는지 생각 혹은 논의한다

포스트 모델링
* 글 번호 (pk)
* 유저-작성자 번호 (relation-pk)
* 글 내용 (TextField)
* 글 쓴 날짜 (DatetimeField auto_now_add=True)
* 글 수정한 날짜 (DatetimeField auto_add=True, Null=True)

댓글(Comment) 모델링
* 댓글 단 사람
* 댓글 쓴 날짜
* 댓글 수정한 날짜 
* 댓글 내용
//
* 유저 이름 (CharField(max_length=30,Null=False))
* 이메일 주소(CharField(max_length=50,Null=True))
* 댓글 내용(TextField(max_length=200,Null=False))

-------------------------------------------------------------------------
Primary Key(기본키, pk)

* 테이블에 저장된 각각의 데이트를 유일하게 구분하는 키
* 바꾸어 말하면, DB 테이블에 각 행의 식별 기준인 기본키가 필요하다
* django 에는 기본키로 id가 디폴트로 지정되어있다.

ForeignKey(외래키)

* 각 테이블 간에 연결하기 위해서 특정 테이블에서 다른 테이블의 참조되는 기본키 

auto_now_add : 데이터가 "처음" 생성되어 저장할 때
auto_now : 데이터가 저장될 때 (update)

Model Relationship ?
Many-to-Many
Many-to-One : 댓글 to 게시글 
One-to-One

User 모델 확장하기 
--> User 모델 커스텀하기 위해서 
확정 방법
1. proxy model(프로식 모델) 사용하기
2. 하나의 모델을 정의 후, User 모델과 One-to-One(일대일) 관계 형성
3. AbstractBaseUser
4. AbstractUser - 내장 유저 모델을 살짝 살짝 수정해서 사용

django tips

1. 코드에 프로젝트 이름 넣지 않는 것을 추천
2. 배포할 때 DEBUG=False 를 잊지 맙시다.

