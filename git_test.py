
from typing import BinaryIO


def hello(hi:int):
    for i in range(hi):
        print("Hello World!")


hello(6)


def open_hi (hihi:int):
    for i in range(hihi):
        hihihi:BinaryIO = open("test.txt")
        for line in hihihi.readlines():
            print(line)
        hihihi.close()

open_hi(9)

star =""
def print_star(num:int):
    global star
    for i in range(num):
        star += "*"
        print(star)

print_star(6)



class Student:
    def __init__(self, name, student_id, grade):
        self.name = name
        self.student_id = student_id
        self.grade = grade

    def student(self):#不太確定
        return f"Student(name={self.name}, student_id={self.student_id}, grade={self.grade})"
    
student = Student("hihello", "664455", 3)
print(student)
