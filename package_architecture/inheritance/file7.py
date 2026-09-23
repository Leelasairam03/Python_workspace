#hybrid inheritance
class Employee:
    def work(self):
        print("working")

class FrontEndDeveloper(Employee):
    def render(self):
        print("render html pages")
        
class BackEndDeveloper(Employee):
    def connect_database(self):
        print("connect database")

class FullStackDeveloper(FrontEndDeveloper,BackEndDeveloper):
    def deploy(self):
        print("deploy application")

f=FullStackDeveloper()
f.work()
f.render()
f.connect_database()
f.deploy()