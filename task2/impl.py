import copy
from repo import StudentManagerRepo

class StudentManageImpl(StudentManagerRepo):
    __student_list = []

    # 학생 추가 기능 구현
    def add_student(self, student): # 학생 추가
        # 학생 목록에서 학번 조회 => 이미 존재할 경우 => 추가 실패
        for i in range(len(self.__student_list)):
            if self.__student_list[i].student_id == student.student_id:
                return None
        # 존재하는 학번이 없을 경우 => 학생 추가
        else:
            self.__student_list.append(student)
            self.__student_list.sort(key=lambda stu: -float(stu.gpa))   # 학점에 따른 내림차순 정렬
            return student

    # 전체 학생 조회 기능 구현
    def list_student(self): # 전체 학생 조회
        return copy.deepcopy(self.__student_list)

    # 학생 조회 기능 구현
    def search_student(self, student_id): # 학생 조회
        for student in self.__student_list:
            if student.student_id == student_id:
                return copy.deepcopy(student)
        else:
            return None

    # 학생 제거 기능 구현
    def delete_student(self, student_id): # 학생 제거
        for i in range(len(self.__student_list)):
            if self.__student_list[i].student_id == student_id:
                return self.__student_list.pop(i)
        else:
            return None

    # 학셍 수정 기능 구현
    def update_student(self, student_id, student): # 학생 수정
        # 기존 학번에서 이미 존재하는 학번으로 수정하려 할 경우 => 수정 불가능
        if (self.search_student(student_id) is not None) and student_id != student.student_id:
            return False

        for i in range(len(self.__student_list)):
            if self.__student_list[i].student_id == student_id:
                self.__student_list[i] = student
                self.__student_list.sort(key=lambda stu: -float(stu.gpa))   # 학점에 따른 내림차순 정렬
                return copy.deepcopy(self.__student_list[i])
        else:
            return None