import random

class Pet:
    """A class representing a tamagotchi pet with its actions"""

    def __init__(self, n:str):
        """Initializes a new pet with the given name and attributes below"""
        #The name of the pet
        self.name = n
        #The fullness of the pet, starting at 8
        self.fullness = 8
        #The happiness of the pet, starting at 8
        self.happiness = 8
        #The cleanliness of the pet, starting at 8
        self.cleanliness = 8
        #The pet status of alive or dead
        self.alive = True
        #The stage of life of the pet, starting as "egg"
        self.stage = "egg"
        #The pet's progress, starting at 1
        self.progress = 1

    def feed(self):
        """The function feeds the pet"""
        
        #increasing the pet's fullness by 3
        self.fullness += 3

        #If fullness reaches 10, cleanliness decreases by 2
        if self.fullness == 10:
            self.cleanliness = self.cleanliness - 2

            #The cleanliness can't drop below 1
            if self.cleanliness < 1:
                self.cleanliness = 1

        #fullness can't exceed 10
        else:
            if self.fullness > 10:
                self.fullness = 10
                
    def play(self):
        """Function plays with the pet""" 

        #Increasing the pet's happiness by 3
        self.happiness += 3

        #If happiness reaches 10, fullness decreases by 2
        if self.happiness == 10:
            self.fullness = self.fullness - 2

            #The fullness can't drop below 1
            if self.fullness < 1:
                self.fullness = 1

        #The happiness can't exceed 10
        else:
            if self.happiness > 10:
                self.happiness = 10

    def bathe(self):
        """The function bathes the pet"""

        #Increasing the pet's cleanliness by 3
        self.cleanliness += 3

        #If cleanliness reaches 10, happiness decreases by 2
        if self.cleanliness == 10:
            self.happiness = self.happiness - 2

            # The happiness can't drop below 1
            if self.happiness < 1:
                 self.happiness = 1

        #The cleanliness can't exceed 10
        else:
            if self.cleanliness > 10:
                self.cleanliness = 10
  

    def age_up(self):
        """Ages the pet up to different stages of life"""

        #The pet progresses from "egg" to "baby", then "child", and finally to "adult".
        if self.stage == "egg":
            self.stage = "baby"

        elif self.stage == "baby":
            self.stage = "child"

        else:
            self.stage = "adult"

        #Resets the progress to 1 after each stage
        self.progress = 1


    def status(self):
        """Returns the current status of the pet based on its fullness, happiness, and cleanliness levels."""

        #If fullness, happiness, and cleanliness is greater than 5 than returns fine
        if self.fullness and self.happiness and self.cleanliness > 5:
            return "fine"

        #If fullness, happiness, and cleanliness equal 1 changes alive to False and returns dead 
        elif self.fullness or self.happiness or self.cleanliness == 1:
            self.alive = False
            return "dead"

        #If fullness, happiness, and cleanliness is equal or less than 5 returns distress
        elif self.fullness and self.happiness and self.cleanliness <= 5:
            return "distress"

    def time_step(self):
        """Simulates the passage of time for the pet, randomly decreasing one of the pet's attributes (fullness, happiness, cleanliness)."""

        #Random module choices between fullness, happiness, and cleanliness
        choice = random.choice(["fullness","happiness", "cleanliness"])
        
        #If choice equals fullness, the fullness decreases by 1, and increases progress by 1
        if choice == "fullness":
            self.fullness -= 1
            self.progress += 1
            
        #If choice equals happiness, the happiness decreases by 1, and increases progress by 1
        elif choice == "happiness":
            self.happiness -= 1
            self.progress += 1
            
        #If choice equals cleanliness, the cleanliness decreases by 1, and increases progress by 1
        elif choice == "cleanliness":
            self.cleanliness -= 1
            self.progress += 1

        #If progress equals 20, calls the age up and status function then return the status
        if self.progress == 20:
            self.age_up(status())

            return self.status

import turtle
import time

def fill_circle(turtle, color, radius, position):
        turtle.up()
        turtle.goto(position)
        turtle.down()
        turtle.fillcolor(color)
        turtle.begin_fill()
        turtle.circle(radius)
        turtle.end_fill()
        turtle.up()
        turtle.goto(0,0)
        
class TamagotchiGame:
    def __init__(self, name: str):
        """Creates a Tamagotchi Pet with the given name"""
        turtle.tracer(0,0)
        self.pet = Pet(name)
        self.pen = turtle.Turtle()
        self.pen.up()
        self.pen.hideturtle()

    def draw_egg(self):
        fill_circle(self.pen, "PeachPuff", 20, (0,0))
        fill_circle(self.pen, "white", 5, (10,20))
        fill_circle(self.pen, "white", 5, (-10,20))
        fill_circle(self.pen, "black", 2, (10,22))
        fill_circle(self.pen, "black", 2, (-10,22))
        turtle.update()

    def draw_baby(self):
        fill_circle(self.pen, "tomato", 10, (15,0))
        fill_circle(self.pen, "tomato", 10, (-15,0))
        fill_circle(self.pen, "tomato", 30, (0,0))
        fill_circle(self.pen, "white", 8, (15,30))
        fill_circle(self.pen, "white", 8, (-15,30))
        fill_circle(self.pen, "black", 4, (15,34))
        fill_circle(self.pen, "black", 4, (-15,34))
        turtle.update()

    def draw_child(self):
        fill_circle(self.pen, "PowderBlue", 14, (20,0))
        fill_circle(self.pen, "PowderBlue", 14, (-20,0))
        fill_circle(self.pen, "PowderBlue", 10, (40,40))
        fill_circle(self.pen, "PowderBlue", 10, (-40,40))
        fill_circle(self.pen, "PowderBlue", 40, (0,0))
        fill_circle(self.pen, "white", 10, (15,40))
        fill_circle(self.pen, "white", 10, (-15,40))
        fill_circle(self.pen, "black", 5, (15,44))
        fill_circle(self.pen, "black", 5, (-15,44))
        turtle.update()

    def draw_adult(self):
        fill_circle(self.pen, "thistle", 18, (25,0))
        fill_circle(self.pen, "thistle", 18, (-25,0))
        fill_circle(self.pen, "thistle", 12, (50,50))
        fill_circle(self.pen, "thistle", 12, (-50,50))
        fill_circle(self.pen, "thistle", 50, (0,0))
        fill_circle(self.pen, "purple", 5, (0,35))
        fill_circle(self.pen, "white", 12, (15,50))
        fill_circle(self.pen, "white", 12, (-15,50))
        fill_circle(self.pen, "black", 6, (15,55))
        fill_circle(self.pen, "black", 6, (-15,55))
        turtle.update()

    def draw_tombstone(self):
        self.pen.fillcolor("burlywood")
        self.pen.begin_fill()
        self.pen.forward(50)
        for i in range(2):
            self.pen.left(90)
            self.pen.forward(200)
            self.pen.left(90)
            self.pen.forward(100)
        self.pen.end_fill()
        self.pen.up()
        self.pen.goto(0,160)
        self.pen.write("RIP", align = "center", font=("Arial", 20, "normal"))
        self.pen.goto(0,140)
        self.pen.write(self.pet.name, align = "center", font=("Arial", 15, "normal"))
        self.pen.goto(0,120)
        self.pen.write("you were the best <3", align = "center", font=("Arial", 9, "normal"))
        self.pen.goto(0,0)
        turtle.update()

    def display(self):
        self.pen.clear()
        self.pen.up()
        self.pen.goto(0,-30)
        self.pen.write(self.pet.name, align = "center", font=("Arial", 20, "normal"))
        turtle.update()
        self.pen.goto(0,0)
        if self.pet.stage == "egg":
                self.draw_egg()
        elif self.pet.stage == "baby":
                self.draw_baby()
        elif self.pet.stage == "child":
                self.draw_child()
        else:
                self.draw_adult()
        if self.pet.status() == "distress":
                self.pen.goto(0,120)
                self.pen.write("*crying*", align = "center", font=("Arial", 30, "normal"))
                self.pen.goto(0,0)
                turtle.update()

    def feed(self):
        self.pet.feed()
        self.display()
        self.pen.goto(0,90)
        self.pen.write("~nom-nom-nom~", align = "center", font=("Arial", 30, "normal"))
        turtle.update()
        self.pen.goto(0,0)
        time.sleep(2)
        self.display()

    def play(self):
        self.pet.play()
        self.display()
        self.pen.goto(0,90)
        self.pen.write("~weeee~", align = "center", font=("Arial", 30, "normal"))
        turtle.update()
        self.pen.goto(0,0)
        time.sleep(2)
        self.display()

    def bathe(self):
        self.pet.bathe()
        self.display()
        self.pen.goto(0,90)
        self.pen.write("~scrub-a-dub~", align = "center", font=("Arial", 30, "normal"))
        turtle.update()
        self.pen.goto(0,0)
        time.sleep(2)
        self.display()
        

    def run(self) -> None:
        """Runs the Tamagotchi game"""
        self.display()
        time.sleep(2)
        state = self.pet.time_step()
        while state != "dead":
            self.display()
            self.pen.goto(0,-50)
            self.pen.write("Type 1 to feed, 2 to play, 3 to bathe", align = "center", font=("Arial", 15, "normal"))
            turtle.update()
            self.pen.goto(0,0)
            turtle.listen()
            turtle.onkey(self.feed, "1")
            turtle.onkey(self.play, "2")
            turtle.onkey(self.bathe, "3")
            time.sleep(1)
            state = self.pet.time_step()
        self.pen.clear()
        self.draw_tombstone()
        turtle.exitonclick()

        
def play_tmagotchi():
    """The function gets the name for a Tamagotchi pet from the user, and then create
    and run a Tamagotchi game for a pet with the given name."""

    #Asking the for the pet's name
    pet_name = input("What would you like to name your Tamagotchi?: ")

    #Creating the instance of the class TamagotchiGame with the given name
    game = TamagotchiGame(pet_name)

    #Call the member function run for the instance of TamagotchiGame.
    game.run()

    

    
        
            
    
            
   
