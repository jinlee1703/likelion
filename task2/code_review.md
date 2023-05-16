## 코드리뷰1 내용

- reviewer : 김경민
- date : `23. 5. 9.(화)

---

### 1. 클래스별로 파일을 분할하여 가독성이 좋았음.

### 2. Student 클래스에서 객체 지향 프로그래밍의 원칙 중 하나인 캡슐화를 잘 지키고 있음.

그러나, 현재 코드에서는 속성들을 수정하거나 검증하는 기능이 존재하지 않음.
setter메서드를 추가하면 더 좋을 것 같음!
→ 속성 값을 변경할 때 검증 로직을 추가하면, 객체의 불완전한 상태를 방지하고, 객체를 사용하는 측에서 발생할 수 있는 오류를 줄일 수 있음. 코드의 안정성과 신뢰성을 높일 수 있는 방법

    ```python
    class Student:
        def __init__(self, student_id, name, age, dept, gpa):
            self.__student_id = student_id
            self.__name = name
            self.__age = age
            self.__dept = dept
            self.__gpa = gpa

        @property
        def student_id(self):
            return self.__student_id

        @property
        def name(self):
            return self.__name

        @property
        def age(self):
            return self.__age

        @property
        def dept(self):
            return self.__dept

        @property
        def gpa(self):
            return self.__gpa

        def __str__(self):
            return f"{self.__student_id}\t{self.__name}\t{self.__age}\t{self.__dept}\t{self.__gpa}"
    ```

### 3. lmpl.py

1. ‘copy.deepcopy()’를 사용하여 객체를 반환할 때 객체의 본사본을 반홤함으로써, 캡슐화유지를 잘 한 것 같음.

2. 그러나, 위에서 말했듯이 예외 처리가 부족하여 ‘add_student()’나 ‘update_student()에서 불완전 할 수 있음.
3. 코드중복 → 학생 목록을 학점에 따른 내림차순으로 정렬하는 코드가 두 번 중복되어 사용되었음. 중복 코드는 유지보수를 어렵게 만들 수 있으니, 별도의 메서드로 분리하는 것은 어떨지 ?
4. ‘StudentManageImpl’클래스가 ‘StudentManagerRepo’클래스를 상속받고 있으나 부모 클래스의 기능 활용하거나 오버라이딩하는 부분이 없어 상속의 이점 활용이 부족함→ 부모 클래스에 추상 메소드를 정의하여 구현하는 것이 좋음 !

   ```python
   import copy
   from repo import StudentManagerRepo

   class StudentManageImpl(StudentManagerRepo):
       __student_list = []

       # 학생 추가 기능 구현
       def add_student(self, student):  # 학생 추가
           # 학생 목록에서 학번 조회 => 이미 존재할 경우 => 추가 실패
           for i in range(len(self.__student_list)):
               if self.__student_list[i].student_id == student.student_id:
                   return None
           # 존재하는 학번이 없을 경우 => 학생 추가
           else:
               self.__student_list.append(student)
               self.__student_list.sort(
                   key=lambda stu: -float(stu.gpa))   # 학점에 따른 내림차순 정렬
               return student

       # 전체 학생 조회 기능 구현
       def list_student(self):  # 전체 학생 조회
           return copy.deepcopy(self.__student_list)

       # 학생 조회 기능 구현
       def search_student(self, student_id):  # 학생 조회
           for student in self.__student_list:
               if student.student_id == student_id:
                   return copy.deepcopy(student)
           else:
               return None

       # 학생 제거 기능 구현
       def delete_student(self, student_id):  # 학생 제거
           for i in range(len(self.__student_list)):
               if self.__student_list[i].student_id == student_id:
                   return self.__student_list.pop(i)
           else:
               return None

       # 학셍 수정 기능 구현
       def update_student(self, student_id, student):  # 학생 수정
           # 기존 학번에서 이미 존재하는 학번으로 수정하려 할 경우 => 수정 불가능
           if (self.search_student(student_id) is not None) and student_id != student.student_id:
               return False

           for i in range(len(self.__student_list)):
               if self.__student_list[i].student_id == student_id:
                   self.__student_list[i] = student
                   self.__student_list.sort(
                       key=lambda stu: -float(stu.gpa))   # 학점에 따른 내림차순 정렬
                   return copy.deepcopy(self.__student_list[i])
           else:
               return None
   ```

### 4. main.py

1. 각 기능별로 함수를 구분하여 코드 구조가 명확하고 가독성이 좋은 듯.

2. 마찬가지로 입력 값에 대한 예외 처리를 추가하면 좋을 듯함.

3. 사용자 입력을 처리하는 부분에서 ‘int(input())’를 사용하여 정수를 바로 입력받으면, 정수가 아닌 값을 입력했을 때 오류가 발생 → 방지하기 위해 문자열로 입력 받은 후에 정수로 변환하는 것은 더 좋은 방안이 아닐까 생각함.
4. ‘name’변수를 사용하여 학번을 입력받고 있는데 변수명을 ‘student_id’로 변경하면 더 좋을 것 같음 !

   ```python
   from abc import *
   from student import Student
   from service import StudentManagerService

   """
   print_manual() : 명령어 리스트를 출력하기 위한 함수
   """
   def print_manual():
       print("===============")
       print("1. 학생 추가")
       print("2. 전체 학생 조회")
       print("3. 학생 조회")
       print("4. 학생 제거")
       print("5. 학생 수정")
       print("6. 종료")
       print("===============")

   """
   input_student_info() : 학생 정보를 입력받기 위한 함수
   """
   def input_student_info():
       student_id = input("학번: ")
       name = input("이름: ")
       age = input("나이: ")
       dept = input("전공: ")
       gpa = input("학점: ")

       return Student(student_id, name, age, dept, gpa)

   """
   main() : 학생 관리 프로그램을 실행시키기 위한 함수
   """
   def main(manager):
       while True:
           print_manual()

           mode = int(input())

           # 학생 추가
           if mode == 1:
               new_student = input_student_info()
               student = manager.add_student(new_student)
               if student is not None:
                   print(f"{student.name} 학생이 추가되었습니다.")
               else:
                   print("이미 존재하는 학번입니다.")
           # 전체 학생 조회
           elif mode == 2:
               print("학번\t이름\t나이\t전공\t학점")
               for student in manager.list_student():
                   print(student)
           # 학생 조회
           elif mode == 3:
               name = input("조회할 학생의 학번: ")
               print()

               find_student = manager.search_student(name)

               if find_student is not None:
                   print(find_student)
               else:
                   print("존재하지 않는 학번입니다.")
           # 학생 제거
           elif mode == 4:
               student_id = input("삭제할 학생의 학번: ")
               print()

               deleted_student = manager.delete_student(student_id)

               if deleted_student is not None:
                   print(f"{deleted_student.name} 학생이 삭제되었습니다.")
               else:
                   print("존재하지 않는 학번입니다.")
           # 학생 수정
           elif mode == 5:
               student_id = input("수정할 학생의 학번: ")
               print()

               student = input_student_info()
               updated_student = manager.update_student(student_id, student)

               if not updated_student:
                   print("이미 존재하는 학번으로 수정할 수 없습니다.")
               elif updated_student is not None:
                   print(f"{updated_student.name} 학생이 수정되었습니다.")
               else:
                   print("존재하지 않는 학번입니다.")
           # 프로그램 종료
           elif mode == 6:
               print("프로그램 종료.")
               break
           # 그 외 명령 시
           else:
               print("잘못된 명령입니다.")

   if __name__ == '__main__':
       manager = StudentManagerService()
       main(manager)
   ```

---

## 코드리뷰2 내용

- reviewer : 김경민
- date : `23. 5. 9.(화)

### 학생 추가할 때마다 계속 정렬 => 추가 시 자리 찾아서 정렬

    ```python
    def add_student(self, student):
            # 학생 목록에서 학번 조회 => 이미 존재할 경우 => 추가 실패
            for i in range(len(self.__student_list)):
            if self.__student_list[i].student_id == student.student_id:
            return None

            # 새로운 학생 정보를 학점순으로 적절한 위치에 삽입
            if self.__student_list[i].gpa < student.gpa:
            self.__student_list.insert(i, student)
            return student

            # 학번이 모두 다를 경우 => 리스트 맨 뒤에 새로운 학생 정보 추가
            self.__student_list.append(student)
            return student
    ```
