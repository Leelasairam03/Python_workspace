from sys import exception
from ast import excepthandler
print("start")
try:
    try:
        print(10/0)
    except exception as e:
        print("inner except")
except exception as e:
    print("outer except")
print("end")
