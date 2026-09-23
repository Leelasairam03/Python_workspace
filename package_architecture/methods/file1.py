class Student:
    school_name="shri chaitanya"
    principal="Gunde Gowda"
    location="Pandavapura"

    def __init__(self,name):
        self.name=name

    @classmethod
    def get_school(cls):
        print(cls.school_name)
        print(cls.location)
        print(cls.principal)

    @classmethod
    def change_principal(cls,new_principal):
        cls.principal=new_principal
        

Student.get_school()
print("--------------------------------")
Student.change_principal("Suresh")
print(Student.principal)


