#__repr__
class Book:
    def __init__(self,name,author):
        self.name=name
        self.author=author

    def __repr__(self):
        return f"book name {self.name} and author {self.author}"

b1=Book("maths","rd sharma")
b2=Book("physics","hc verma")
b3=Book("python","sai ram")
print(b1)

l=[b1,b2,b3]
print(l)

