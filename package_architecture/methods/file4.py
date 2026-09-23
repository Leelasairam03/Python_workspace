class Student:

    @staticmethod
    def calc_percent(marks,total):
        return (marks/total)*100
    
print(Student.calc_percent(80,100))
s1=Student()
print(s1.calc_percent(582,625))