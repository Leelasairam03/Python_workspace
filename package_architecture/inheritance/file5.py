#hierarchical inheritance
class Player:
    def play():
        print("player plays to win")

class CricketPlayer(Player):
    def bat(self):
        print("score century")

class FootBallPlayer(Player):
    def goalkeep(self):
        print("stop the ball")

class KabaddiPlayer(Player):
    def raid(self):
        print("super raid")

c=CricketPlayer()
f=FootBallPlayer()
k=KabaddiPlayer()
c.bat()
f.goalkeep()
k.raid()
Player.play()  #play() can be accessed by any child class that inherits player class