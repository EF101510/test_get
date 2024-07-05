
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