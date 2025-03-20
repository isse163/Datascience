import turtle
import random
import time

# Fördröjning och poäng
DELAY = 0.1
score = 0
high_score = 0

# Skapa fönster
wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("black")
wn.setup(width=700, height=700)
wn.tracer(0)

# Skapa spelgräns
grid = turtle.Turtle()
grid.speed(0)
grid.color("white")
grid.penup()
grid.goto(-310, 250)
grid.pendown()
for _ in range(2):
    grid.forward(600)
    grid.right(90)
    grid.forward(500)
    grid.right(90)
grid.hideturtle()

# Skapa ormens huvud
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("white")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Skapa mat
food = turtle.Turtle()
food.speed(0)
food.shape(random.choice(["triangle", "circle", "square"]))
food.color(random.choice(["yellow", "green", "red"]))
food.penup()
food.goto(20, 20)

# Skapa poängtavla
scoreboard = turtle.Turtle()
scoreboard.speed(0)
scoreboard.color("white")
scoreboard.penup()
scoreboard.hideturtle()
scoreboard.goto(0, 260)

def update_score():
    scoreboard.clear()
    scoreboard.write(f"Score: {score}  High Score: {high_score}", align="center", font=("Courier", 24, "normal"))
update_score()

# Funktioner för rörelse
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        head.sety(head.ycor() + 20)
    if head.direction == "down":
        head.sety(head.ycor() - 20)
    if head.direction == "left":
        head.setx(head.xcor() - 20)
    if head.direction == "right":
        head.setx(head.xcor() + 20)

# Tangentbordsstyrning
wn.listen()
wn.onkey(go_up, "Up")
wn.onkey(go_down, "Down")
wn.onkey(go_left, "Left")
wn.onkey(go_right, "Right")

# Spelets huvudloop
segments = []
while True:
    wn.update()
    
    # Kollision med gränserna
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 240 or head.ycor() < -240:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"
        for segment in segments:
            segment.goto(1000, 1000)  # Skicka bort segmenten
        segments.clear()
        score = 0
        update_score()

    # Kollision med mat
    if head.distance(food) < 20:
        x = random.randint(-290, 290)
        y = random.randint(-240, 240)
        food.goto(x, y)
        
        # Lägg till segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("gray")
        new_segment.penup()
        segments.append(new_segment)
        
        score += 10
        if score > high_score:
            high_score = score
        update_score()
    
    # Flytta svansen
    for i in range(len(segments) - 1, 0, -1):
        x = segments[i - 1].xcor()
        y = segments[i - 1].ycor()
        segments[i].goto(x, y)
    if segments:
        segments[0].goto(head.xcor(), head.ycor())
    
    move()
    
    # Kollision med kroppen
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"
            for segment in segments:
                segment.goto(1000, 1000)
            segments.clear()
            score = 0
            update_score()
    
    time.sleep(DELAY)

wn.mainloop()