from Domain.utils.DataGateway import DataGateway
import uuid

class Classroom:
  def __init__(self, name, description, max_student, creator_email, is_private, id=uuid.uuid4()):
    if len(name) < 2:
      raise ValueError("Name must be longer than 2 characters!")
    elif len(description) < 3:
      raise ValueError("Description must be longer than 3 characters!")
    elif max_student < 0:
      raise ValueError("Max number of student must be larger than 0!")
    self.__id = str(id)
    self.__name = name
    self.__description = description
    self.__max_student_number = max_student
    self.__student_list = {}
    self.__professor_list = []
    self.__creator = creator_email
    self.__classwork_list = {}
    self.__is_private = is_private
    DataGateway.save_data("Classroom", self.__name, self)
  
  def get_id (self):
    return self.__id
  
  def set_id (self, id):
    self.__id = id
  
  def get_name(self):
    return self.__name
  
  def set_name(self, name):
    self.__name = name

  def get_description(self):
    return self.__description
  
  def set_description(self, description):
    self.__description = description
  
  def get_max_student_number(self):
    return self.__max_student_number
  
  def set_max_student_number(self, number):
    self.__max_student_number = number
  
  def get_student_list(self):
    return self.__student_list
  
  def set_student_list(self, list):
    self.__student_list = list
  
  def get_professor_lsit(self):
    return self.__professor_list
  
  def set_professor_list(self, list):
    self.__professor_list = list

  def get_creator(self):
    return self.__creator
  
  def set_creator(self, creator):
    self.__creator = creator
  
  def get_classwork(self):
    return self.__classwork_list
  
  def set_classwork(self, classwork_list):
    self.__classwork_list = classwork_list
  
  def is_private(self):
    return self.__is_private
  
  def set_private(self, private):
    self.__is_private = private
  
  def add_student(self, student_email):
    self.__student_list[student_email] = { "score": 0 }
  
  def add_professor(self, professor_email):
    self.__professor_list.append(professor_email)
  
  def remove_student(self, student_email):
    del self.__student_list[student_email]
  
  def remove_professor(self, professor_email):
    if (professor_email == self.__creator):
      raise ValueError("The professor is the creator of the class!")
    self.__professor_list.remove(professor_email)
  
  def check_enrollment(self, student_email):
    if (student_email in self.__student_list):
      return True
    else:
      return False