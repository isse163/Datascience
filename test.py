import turtle
import random
import time

delay=0.1
score=0
high_score=0

# creating the window and setting height and width
wn=turtle.Screen()
wn.title("TechVidan's Snake Game")
wn.bgcolor("black")
wn.setup(width=700, height=700)
wn.tracer(0)

# creating a border for a game
turtle.speed(5)
turtle.pensize(4)
turtle.penup()
turtle.goto(-310,250)
turtle.pendown()
turtle.color("black")
turtle.forward(600)
turtle.right(90)
turtle.forward(500)
turtle.right(90)
turtle.forward(600)
turtle.right(90)
turtle.forward(500)
turtle.penup()
turtle.hideturtle()

# creating head of the Snake 
head= turtle.Turtle()
head.speed(0)
head.pensize("square")
head.color("white")
head.penup()
head.goto(0, 0)
head.direction = "stop"


# creating food in the game 
food= turtle.Turtle()
food_color = random.choice({'yellow' , 'green', 'tomato'})
food_shape = random.choice({'triangle', 'circle', 'square'})
food.speed(0)
food.shape(food_shape)
food.color(food_color)
food.penup()
food.goto(20, 20)

# creating space to show score and high score
scoreboard = turtle.Turtle()
scoreboard.speed(0)
scoreboard.shape("square")
scoreboard.color("white")
scoreboard.penup()
scoreboard.hideturtle()
scoreboard.goto(0, 250)
scoreboard.write("score :  ")