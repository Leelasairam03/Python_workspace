#multi level
class FootWear:
    def protect(self):
        print("foot protection...")
class Shoe(FootWear):
    def comfort(self):
        print("foot comfort...")
class SportShoe(Shoe):
    def cushion_impact(self):
        print("better grip...")

s1=SportShoe()
s1.protect()
s1.comfort()
s1.cushion_impact()

