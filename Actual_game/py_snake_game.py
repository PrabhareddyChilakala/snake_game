import turtle
import time
import random

WIDTH=500
HEIGHT=500
SNAKE_CELL_SIZE=20
FOOD_SIZE=10
SQUARE_SIZE = 20  # Default size of turtle "square" shape
STEP_SIZE = 10
DELAY = 200  # milliseconds

def move_snake():
    for index in range(len(segments) - 1, 0,-1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)
    # Move segment 0 to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)

    if head.direction=="up":
        head.sety(head.ycor()+SNAKE_CELL_SIZE)
    elif head.direction == "right":
        head.setx(head.xcor() + SNAKE_CELL_SIZE)
    elif head.direction == "down":
        head.sety(head.ycor() - SNAKE_CELL_SIZE)
    elif head.direction == "left":
        head.setx(head.xcor() - SNAKE_CELL_SIZE)
def check_food_collision():
    count=0
    if head.distance(food) < SNAKE_CELL_SIZE:
        x = random.randint(- WIDTH / 2 + FOOD_SIZE, WIDTH / 2 - FOOD_SIZE)
        y = random.randint(- HEIGHT / 2 + FOOD_SIZE, HEIGHT / 2 - FOOD_SIZE)
        food.goto(x, y)

        # Add new segment
        new_segment = turtle.Turtle()
        new_segment.shape("square")
        new_segment.color("green")
        new_segment.penup()
        segments.append(new_segment)
        count+=len(segments)
        print(count)
def check_head_collision():
    self_collision = False
    if head.xcor() < -240 or head.xcor() > 240 or head.ycor() < -240 or head.ycor() > 240:
        head.goto(0, 0)
        head.direction = "stop"
    for segment in segments:
        if segment.distance(head) < 20:
            head.goto(0, 0)
            head.direction = "stop"
            self_collision = True
def go_up():
    if head.direction != "down":
        head.direction = "up"
def go_right():
    if head.direction != "left":
        head.direction = "right"
def go_down():
    if head.direction != "up":
        head.direction = "down"
def go_left():
    if head.direction != "right":
        head.direction = "left"
def new_game():
    global head, food, segments
    # Set up screen
    screen.clear()
    screen.bgcolor("white")
    screen.tracer(0)

    # Event handlers
    screen.listen()
    screen.onkey(go_up, "Up")
    screen.onkey(go_right, "Right")
    screen.onkey(go_down, "Down")
    screen.onkey(go_left, "Left")

    # Snake head
    head = turtle.Turtle()
    head.speed(0)
    head.shape("square")
    head.color("black")
    head.penup()
    head.goto(100, 100)

    # food
    food = turtle.Turtle()
    food.shape("circle")
    food.color("red")
    food.shapesize(FOOD_SIZE / SQUARE_SIZE)
    food.penup()
    segments = []
    head.direction = "up"


def game_loop():
    move_snake()
    check_head_collision()
    check_food_collision()
    screen.update()
    turtle.ontimer(game_loop, DELAY)

#initialise screen
screen = turtle.Screen()
screen.title("Snake Game")
screen.setup(500, 500)

# Let's go!
new_game()
game_loop()
turtle.done()