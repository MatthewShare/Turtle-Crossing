from turtle import Turtle
import random
COLORS = ["pink", "blue", "green", "purple", "orange", "red", "yellow"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.cars = []
        self.distance_moving = STARTING_MOVE_DISTANCE

    def create_car(self):
        car = Turtle()
        car.penup()
        car.shape("square")
        car.color(random.choice(COLORS))
        car.setheading(270)
        car.shapesize(2, 1)
        car.goto(300, random.randint(-250, 250))
        self.cars.append(car)

    def move(self):
        for each_car in self.cars:
            each_car.goto(each_car.xcor() - self.distance_moving, each_car.ycor())

    def level_up(self):
        self.distance_moving += MOVE_INCREMENT



