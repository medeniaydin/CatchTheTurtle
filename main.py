import turtle
import random

screen = turtle.Screen()
screen.bgcolor("light blue")
screen.title("Cath The Turtle")
FONT = ('Arial',25,'normal')
score = 0
game_over = False

#turtle list
turtle_list = []

#score turtle
score_turtle = turtle.Turtle()

#countdown turtle
conuntdown_turtle = turtle.Turtle()

#make turtle properties
x_coordinates = [-20, -10, 0, 10, 20]
y_coordinates = [20, 10, 0, -10]
grid_size = 10

def setup_score_turtle():

    score_turtle.hideturtle()
    score_turtle.color("dark blue")
    score_turtle.penup()

    top_height = screen.window_height() / 2
    y = top_height * 0.8

    score_turtle.setposition(0,y)
    score_turtle.write(arg="score :0",move=False,align="center",font=FONT)


def make_turtle(x,y):
    t = turtle.Turtle()

    def handle_click(x,y):
        global score
        score += 1
        score_turtle.clear()
        score_turtle.write(arg="score : {}".format(score), move=False, align="center", font=FONT)

    t.onclick(handle_click)
    t.penup()
    t.shape("turtle")
    t.shapesize(2,2)
    t.color("dark green")
    t.goto(x * grid_size,y * grid_size )
    turtle_list.append(t)


def setup_turtle():
    for x in x_coordinates:
        for y in y_coordinates:
            make_turtle(x,y)

def hide_turtles():
    for t in turtle_list:
        t.hideturtle()

#recursive function
def show_turtle_randomly():
    if not game_over:
        hide_turtles()
        random.choice(turtle_list).showturtle()
        screen.ontimer(show_turtle_randomly,500)



def countdown(time):
    conuntdown_turtle.hideturtle()
    conuntdown_turtle.color("dark blue")
    conuntdown_turtle.penup()
    top_height = screen.window_height() / 2
    y = top_height * 0.8
    conuntdown_turtle.setposition(0, y -30)
    conuntdown_turtle.clear()
    if time > 0:
        conuntdown_turtle.clear()
        conuntdown_turtle.write(arg="Time: {}".format(time), move=False, align="center", font=FONT)
        screen.ontimer(lambda: countdown(time - 1),1000)
    else:
        global game_over
        game_over = True
        conuntdown_turtle.clear()
        hide_turtles()
        conuntdown_turtle.write(arg="Game Over!", move=False, align="center", font=FONT)


def start_game_up():
    turtle.tracer(0)

    setup_score_turtle()
    setup_turtle()
    hide_turtles()
    show_turtle_randomly()
    countdown(10)

    turtle.tracer(1)

start_game_up()
turtle.mainloop()




