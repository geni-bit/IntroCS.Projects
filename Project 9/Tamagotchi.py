#add this to the end of your my_tamagotchi.py file
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
