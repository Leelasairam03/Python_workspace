from calculation.mul import mul
from calculation.add import add

def sq_area(side):
    return mul(side,side)

def sq_perimeter(side):
    return 2*(add(side,side))

print(sq_area(5))