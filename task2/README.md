# 학생 관리 프로그램

## 설명

### 과제 설명

학생 CRUD (Create, Read, Update, Delete) 기능 구현

### 파일 설명

- main.py : 프로그램이 실행되기 위한 메인 함수가 있는 파일
- student.py : `Student` 클래스가 있는 파일
- service.py : `StudentManagerService` 클래스가 있는 파일
- repo.py : `StudentManagerRepo` 클래스가 있는 파일
- impl.py : `StudentManageImpl` 클래스가 있는 파일
- .gitignore : terminal로 python을 실행할때마다 `__pycache__` 디렉터리 내의 파일이 업데이트 되길래 추가함
- code_review.md : 해당 과제에 대한 코드리뷰 내용이 적혀있는 파일

## 실행

### 0. 프로그램 실행

```bash
python main.py
```

![image](https://user-images.githubusercontent.com/68031450/236016328-7737af05-9bee-4c46-a239-2e17d72f0e4e.png)

### 1. 학생 추가

- 정상 입력 시

  ![image](https://user-images.githubusercontent.com/68031450/236018314-0c4d9d3e-8b6c-40d2-a561-e5a5d44d0105.png)

- 이미 존재하는 학번 입력 시

  ![image](https://user-images.githubusercontent.com/68031450/236018486-ece35919-3d81-4f05-ba9c-5f354bc42e9c.png)

### 2. 전체 학생 조회 (정렬 조건 적용)

![image](https://user-images.githubusercontent.com/68031450/236018683-a1f832f5-b7b9-4cec-ae61-b564b780e85c.png)

### 3. 학생 조회

- 존재하는 학번 입력 시

  ![image](https://user-images.githubusercontent.com/68031450/236018897-7b09cb05-b67e-4aad-9289-99ffc3066173.png)

- 존재하지 않는 학번 입력 시

  ![image](https://user-images.githubusercontent.com/68031450/236019010-08404b45-ffc1-4410-8efa-d0dc1d2521ac.png)

### 4. 학생 제거

- 존재하는 학번 입력 시

  ![image](https://user-images.githubusercontent.com/68031450/236019275-bc52d417-adfe-4954-816c-e2746e5565dc.png)

- 존재하지 않는 학번 입력 시

  ![image](https://user-images.githubusercontent.com/68031450/236019435-a5abc0a9-f6fe-4389-8962-6b51a85b574e.png)

### 5. 학생 수정

- 이미 존재하는 학번으로 수정을 시도했을 시

  ![image](https://user-images.githubusercontent.com/68031450/236020146-86e0fe52-16cf-4e5d-ac69-352d33c3d109.png)

- 존재하지 않는 학번 입력 시

  ![image](https://user-images.githubusercontent.com/68031450/236020400-2ba68ec2-80c0-414f-9bb9-9b75632de681.png)

- 학번은 그대로 유지하고 다른 정보만 수정을 시도했을 시

  ![image](https://user-images.githubusercontent.com/68031450/236020589-e9fac35a-eb78-42bf-a698-c8d3a52a95f4.png)

### 6. 프로그램 종료

![image](https://user-images.githubusercontent.com/68031450/236020959-16c5a072-3ca5-49bd-be34-acf3a401173f.png)

### 그 외의 번호 입력

![image](https://user-images.githubusercontent.com/68031450/236020872-f6c04084-92e2-4e83-9482-87696892137b.png)

## 데이터

### 테스트를 위한 학생 데이터 10개 (복사 후 Terminal에 붙여넣기)

```
1
1
홍길동
20
컴퓨터
3
1
2
김철수
21
화학
3.2
1
3
김유리
22
기계
4
1
4
정대세
23
전자
4.5
1
5
전진우
24
경영
3
1
6
유재석
25
컴공
2
1
7
박명수
20
정보통신
4.3
1
8
박주영
26
경영
3
1
9
고길동
26
회계
4.5
1
10
나천재
23
컴공
4

```
