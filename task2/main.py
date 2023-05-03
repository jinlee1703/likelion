from abc import *
from student import Student
from service import StudentManagerService

def print_manual():
  print("===============")
  print("1. 학생 추가")
  print("2. 전체 학생 조회")
  print("3. 학생 조회")
  print("4. 학생 제거")
  print("5. 학생 수정")
  print("6. 종료")
  print("===============")

def input_student_info():
  student_id = input("학번: ")
  name = input("이름: ")
  age = input("나이: ")
  dept = input("전공: ")
  gpa = input("학점: ")

  return Student(student_id, name, age, dept, gpa)

def main(manager):
  while True:
    print_manual()

    n = int(input())

    # 학생 추가
    if n == 1:
      new_student = input_student_info()
      student = manager.add_student(new_student)
      if student is not None:
        print(f"{student.name} 학생이 추가되었습니다.")
      else:
        print("이미 존재하는 학번입니다.")
    # 전체 학생 조회
    elif n == 2:
      print("학번\t이름\t나이\t전공\t학점")
      for student in manager.list_student():
        print(student)
    # 학생 조회
    elif n == 3:
      name = input("조회할 학생의 학번: ")
      print()
      
      find_student = manager.search_student(name)

      if find_student is not None:
        print(find_student)
      else:
        print("존재하지 않는 학번입니다.")
    # 학생 제거
    elif n == 4:
      student_id = input("삭제할 학생의 학번: ")
      print()

      deleted_student = manager.delete_student(student_id)
      
      if deleted_student is not None:
        print(f"{deleted_student.name} 학생이 삭제되었습니다.")
      else:
        print("존재하지 않는 학번입니다.")
    # 학생 수정
    elif n == 5:
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
    elif n == 6:
      print("프로그램 종료.")
      break
    # 그 외 명령 시
    else:
      print("잘못된 명령입니다.")
    

if __name__ == '__main__':
    manager = StudentManagerService()
    main(manager)