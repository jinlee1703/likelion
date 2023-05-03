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