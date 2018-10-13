import random
# random.randint(1,101)

class Person:
    def __init__(self, name):
        self.name = name
        self.life =  10
        self.strength = 1
        self.pointsToAssign = 5

    def assignPoints(self):
        while self.pointsToAssign > 0:
            print("remaining points to assign :")
            print(self.pointsToAssign)
            x = int(input("how may points do you want to assign in life? "))
            self.life += x
            self.pointsToAssign -= x 
            print("remaining points to assign: ")
            print(self.pointsToAssign)
            x = int(input("how may points do you want to assign in strength? ")) 
            self.strength += x
            self.pointsToAssign -= x
    
    def hit(self, opponent):
        opponent.life -= self.strength
        if opponent.life <= 0:
            opponent.life = 0
            print(opponent.name + " has been defeated")

    def strength(self):
        print("strength: ")
        print(self.strength)

    def remainingPV(self):
        print("life: ")
        print(self.life)

class Game:
    def __init__(self):
        print("Welcome to hit and defeat")
        self.player1 = self.setPlayer("1")
        self.player2 = self.setPlayer("2")
        self.currentPlayer = self.player1
        self.opponent = self.player2
        self.playGame()

    def playGame(self):
        while (self.player1.life > 0 or self.player2.life > 0):
            print(self.player1.name)
            print(self.player1.life)
            print(self.player2.name)
            print(self.player2.life)
            self.turn()
    
    def setPlayer(self, playerNum):
        x = str(input("What is the name of Player" + playerNum + "? "))
        self.player = Person(x)
        self.player.assignPoints()
        return self.player

    def turn(self):
        print(self.currentPlayer.name + ", do you want to attack or to pass? ")
        x = str(input())
        if x == "attack":
            self.currentPlayer.hit(self.opponent)

        self.changeTurn()

    def changeTurn(self):
        if self.currentPlayer == self.player1:
            self.currentPlayer = self.player2
            self.opponent = self.player1
        else:
            self.currentPlayer = self.player1
            self.opponent =self.player2

Game()