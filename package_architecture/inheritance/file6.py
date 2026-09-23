#multiple inheritance
class Batsman:
    def bat(self):
        print("runs")
class Bowler:
    def bowl(self):
        print("wickets")

class AllRounder(Batsman,Bowler):
    def field(self):
        print("catches")

hardik=AllRounder()
hardik.bat()
hardik.bowl()
hardik.field()
print(AllRounder.__mro__)

