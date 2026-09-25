#overriding
from typing_extensions import override
class Student:
    def study(self):
        print("study")

class PythonStudent(Student):
    @override
    def study(self):
        super().study()
        print("study python")

ps=PythonStudent()
ps.study()
