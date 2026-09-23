class MovieTicket:
    theatre="cinepolis"
    location="nagpur"

    def __init__(self,seatno,moviename,price):
        self.seatno=seatno
        self.moviename=moviename
        self.price=price
    
    @classmethod
    def display_theatre(cls):
        print("theatre",cls.theatre)
        print("location",cls.location)

    
    def display_ticket(self):
        print("seatno",self.seatno)
        print("moviename",self.moviename)
        print("price",self.price)
    
    def change_seat(self,newseatno):
        self.seatno=newseatno
    
    @staticmethod
    def display_offers():
        print("15% discount on tuesdays")
    
    @staticmethod
    def check_age(movie_rating):
        if movie_rating=="A":
            print("age proof should be provided")
        elif movie_rating=="U/A":
            print("you can watch movie under parents guidance")
        else:
            print("you are a kid")


m1=MovieTicket(101,"avatar",500)
m1.display_ticket()
MovieTicket.display_theatre()
m1.display_offers()
m1.check_age("A")


