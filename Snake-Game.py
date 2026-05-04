import turtle
import time
import random

delay     = 0.12
grid_size = 20
window_w  = 600
window_h  = 600
boundary  = (window_w // 2) - grid_size

# Game state
state = "menu"  # "menu", "playing", "gameover"

# Set up the Screen
window = turtle.Screen()
window.title("Snake Game by @Mannooma_0")
window.bgcolor("black")
window.setup(width=window_w, height=window_h)
window.tracer(0)

# Score display
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()

score      = 0
high_score = 0

def update_score():
    pen.clear()
    pen.goto(0, 265)
    pen.write(
        f"Score: {score}   High Score: {high_score}",
        align="center",
        font=("Courier", 16, "bold")
    )

# Set up the Snake
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("lime green")
head.penup()
head.goto(0, 0)
head.direction = "stop"
head.hideturtle()

# Set up the Food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(1000, 1000)
food.hideturtle()

# Snake body segments
segments = []

def add_segment():
    seg = turtle.Turtle()
    seg.speed(0)
    seg.shape("square")
    seg.color("dark green")
    seg.penup()
    segments.append(seg)

# Direction functions
def go_up():
    if state == "playing" and head.direction != "down":
        head.direction = "up"

def go_down():
    if state == "playing" and head.direction != "up":
        head.direction = "down"

def go_left():
    if state == "playing" and head.direction != "right":
        head.direction = "left"

def go_right():
    if state == "playing" and head.direction != "left":
        head.direction = "right"

# Keyboard bindings
window.listen()
window.onkeypress(go_up,    "Up")
window.onkeypress(go_down,  "Down")
window.onkeypress(go_left,  "Left")
window.onkeypress(go_right, "Right")
window.onkeypress(go_up,    "w")
window.onkeypress(go_down,  "s")
window.onkeypress(go_left,  "a")
window.onkeypress(go_right, "d")

# Move the snake
def move():
    if head.direction == "up":
        head.sety(head.ycor() + grid_size)
    elif head.direction == "down":
        head.sety(head.ycor() - grid_size)
    elif head.direction == "left":
        head.setx(head.xcor() - grid_size)
    elif head.direction == "right":
        head.setx(head.xcor() + grid_size)

# Spawn food at a random position
def spawn_food():
    limit = (window_w // 2 - grid_size * 2) // grid_size
    x = random.randint(-limit, limit) * grid_size
    y = random.randint(-limit, limit) * grid_size
    food.goto(x, y)

# Draw a button using a turtle
def draw_button(btn_turtle, x, y, label):
    btn_turtle.goto(x, y)
    btn_turtle.shape("square")
    btn_turtle.shapesize(stretch_wid=2, stretch_len=6)
    btn_turtle.color("lime green")
    btn_turtle.showturtle()
    btn_turtle.goto(x, y - 10)
    # Label drawn by pen separately

# Show the start menu
def show_start_menu():
    pen.clear()
    pen.goto(0, 100)
    pen.color("lime green")
    pen.write("SNAKE GAME", align="center", font=("Courier", 36, "bold"))
    pen.goto(0, 30)
    pen.color("white")
    pen.write("by @Mannooma_0", align="center", font=("Courier", 14, "normal"))

    # Draw start button box
    start_btn.goto(0, -50)
    start_btn.shape("square")
    start_btn.shapesize(stretch_wid=2.2, stretch_len=7)
    start_btn.color("lime green")
    start_btn.showturtle()

    pen.goto(0, -62)
    pen.color("black")
    pen.write("PLAY", align="center", font=("Courier", 18, "bold"))

    pen.goto(0, -130)
    pen.color("gray")
    pen.write("Arrow Keys or WASD to move", align="center", font=("Courier", 11, "normal"))

    window.update()

# Show the game over screen
def show_game_over_screen():
    pen.clear()
    pen.goto(0, 80)
    pen.color("red")
    pen.write("GAME OVER", align="center", font=("Courier", 36, "bold"))
    pen.goto(0, 10)
    pen.color("white")
    pen.write(f"Score: {score}", align="center", font=("Courier", 20, "normal"))
    pen.goto(0, -30)
    pen.write(f"High Score: {high_score}", align="center", font=("Courier", 16, "normal"))

    # Draw retry button box
    retry_btn.goto(0, -100)
    retry_btn.shape("square")
    retry_btn.shapesize(stretch_wid=2.2, stretch_len=7)
    retry_btn.color("lime green")
    retry_btn.showturtle()

    pen.goto(0, -112)
    pen.color("black")
    pen.write("RETRY", align="center", font=("Courier", 18, "bold"))

    window.update()

# Start the game
def start_game():
    global state, score
    state = "playing"
    score = 0

    start_btn.hideturtle()
    retry_btn.hideturtle()
    pen.color("white")

    head.goto(0, 0)
    head.direction = "stop"
    head.showturtle()
    food.showturtle()

    for seg in segments:
        seg.goto(1000, 1000)
    segments.clear()

    spawn_food()
    update_score()
    window.update()

# Handle button clicks
def on_click(x, y):
    global state
    if state == "menu":
        if -70 <= x <= 70 and -70 <= y <= -30:
            start_game()
    elif state == "gameover":
        if -70 <= x <= 70 and -120 <= y <= -80:
            start_game()

window.onclick(on_click)

# Also allow Enter key to start/retry
def on_enter():
    if state in ("menu", "gameover"):
        start_game()

window.onkeypress(on_enter, "Return")

# Set up button turtles (invisible squares used as buttons)
start_btn = turtle.Turtle()
start_btn.speed(0)
start_btn.penup()
start_btn.hideturtle()

retry_btn = turtle.Turtle()
retry_btn.speed(0)
retry_btn.penup()
retry_btn.hideturtle()

# Show the start menu first
show_start_menu()

# Main game loop
while True:
    window.update()

    if state != "playing":
        time.sleep(0.05)
        continue

    # Check wall collision
    if abs(head.xcor()) > boundary or abs(head.ycor()) > boundary:
        state = "gameover"
        head.hideturtle()
        food.hideturtle()
        for seg in segments:
            seg.hideturtle()
        show_game_over_screen()
        continue

    # Check self collision
    for seg in segments:
        if seg.distance(head) < grid_size:
            state = "gameover"
            head.hideturtle()
            food.hideturtle()
            for seg in segments:
                seg.hideturtle()
            show_game_over_screen()
            break
    else:
        # Check food collision
        if food.distance(head) < grid_size:
            spawn_food()
            score += 10
            if score > high_score:
                high_score = score
            update_score()
            add_segment()

        # Move body segments
        for i in range(len(segments) - 1, 0, -1):
            segments[i].goto(segments[i - 1].pos())
        if segments:
            segments[0].goto(head.pos())

        move()

    time.sleep(delay)
