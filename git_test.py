
# from typing import BinaryIO


# def hello(hi:int):
#     for i in range(hi):
#         print("Hello World!")


# hello(6)


# def open_hi (hihi:int):
#     for i in range(hihi):
#         hihihi:BinaryIO = open("test.txt")
#         for line in hihihi.readlines():
#             print(line)
#         hihihi.close()

# open_hi(9)

# star =""
# def print_star(num:int):
#     global star
#     for i in range(num):
#         star += "*"
#         print(star)

# print_star(6)



# class Student:
#     def __init__(self, name, student_id, grade):
#         self.name = name
#         self.student_id = student_id
#         self.grade = grade

#     def student(self):#不太確定
#         return f"Student(name={self.name}, student_id={self.student_id}, grade={self.grade})"
    
# student = Student("hihello", "664455", 3)
# print(student)


# class Animal():
#     def __init__(self, name):
#         self.name = name
#         print("Ok")


# class Dog(Animal):


#     def bark(self):
#         print(f"{self.name} 說：汪汪！")

# # 創建一隻狗
# my_dog = Dog("小黃")
# print(my_dog.name)  # 輸出：小黃
# my_dog.bark()       # 輸出：小黃 說：汪汪！


# class Animal():
#     def speak(self):
#         print("我是一個動物")

# class Dog(Animal):
#     def speak(self):
#         print("汪汪！")

# class Cat(Animal):
#     def speak(self):
#         print("喵喵！")

# # 讓動物們說話
# animal = Animal()
# dog = Dog()
# cat = Cat()

# animal.speak()  # 輸出：我是一個動物
# dog.speak()     # 輸出：汪汪！
# cat.speak()     # 輸出：喵喵！




class Animal():
    def __init__(self, name):
        self.name = name
    def foo(self):
        print("foo")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # 呼叫父類別的 __init__ 方法
        self.breed = breed
    
    def foo(self):
        super().foo()
        print("bar")

class Bird(Animal):
    def fly(self):
        print("I can fly.")

class Penguin(Bird):
    def fly(self):
        print("I can't fly.")

my_dog = Dog("小黃", "柴犬")
my_bird = Bird("鳥")

my_penguin=Penguin("企鵝")
my_penguin.fly()



from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def stop_engine(self):
        pass

class Car(Vehicle):
    def start_engine(self):
        print("車子已發動")

    def stop_engine(self):
        print("車子已熄火")

class Ship(Vehicle):
    def start_engine(self):
        print("船已發動")

    def stop_engine(self):
        print("船已熄火")


class Motorcycle(Vehicle):
    def start_engine(self):
        print("摩托車發動")

    def stop_engine(self):
        print("摩托車已熄火")


class Garage(Vehicle):
    def start_engine(self):
        print("全部發動")

    def stop_engine(self):
        print("全部已熄火")


car = Car()
car.start_engine()
car.stop_engine()