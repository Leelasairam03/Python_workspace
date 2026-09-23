class Dish:
    def __init__(self,dish_name,ingredients,is_veg):
        self.dish_name=dish_name
        self.ingredients=ingredients
        self.is_veg=is_veg

d1=Dish('biryani',['rice','chicken','masala'],False)
d2=Dish('pulav',['rice','paneer','masala'],True)



