import turtle

# Have at least one if statement in the code.
# Use at least one for loop to draw shapes. [DIT IT]
# Use at least one while loop to draw shapes.
# Make a function for each basic shape. [DIT IT]
# Draw some basic shapes with colors on the screen.
# Draw shapes with different sizes and colors.
# All variable names and the code follows Python snake case or camelcase.


t = turtle.Turtle()

t.speed(0)
def red_circle(size, color):
    if color == 'red':
        t.fillcolor(color)
        t.begin_fill()
        forward = 0
        while forward < 360:
            t.forward(size)
            t.rt(size)
            forward += 1
        t.end_fill()

def orange_triangle(forward, left, color):
    if color == 'orange':
        t.fillcolor(color)
        t.begin_fill()
        for j in range(3):
            t.forward(forward)
            t.lt(left)
            t.forward(forward)
        t.end_fill()

def yellow_rectangle(forward, left, height, color):
    if color == 'yellow':
        t.fillcolor(color)
        t.begin_fill()
        for k in range(6):
            t.forward(forward)
            t.lt(left)
            t.forward(height)
            t.lt(left)
        t.end_fill()

def blue_square(forward, left, color):
    if color == 'blue':
        t.fillcolor(color)
        t.begin_fill()
        for l in range(4):
            t.forward(forward)
            t.lt(left)
        t.end_fill()

t.penup()
t.goto(10,0)
t.pendown()
red_circle(1, 'red')

t.penup()
t.goto(80,90)
t.pendown()
orange_triangle(100, 120, 'orange')

t.penup()
t.goto(-200,90)
t.pendown()
yellow_rectangle(150, 90, 200, 'yellow')

t.penup()
t.goto(400,-300)
t.pendown()
blue_square(400, 90, 'blue')

turtle.mainloop()