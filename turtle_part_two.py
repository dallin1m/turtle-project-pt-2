import turtle

# Picture: Your code generates an image when we test it.
# Functions: If we count 3 basic shape functions + 1 main function + 2 functions for 2 different complex shapes then your program should have at least 6 functions. You could have more, but you should not have less.
# Main function: your top-level code is in the main function.
# No global variables: all variables are defined inside main or another function. No global variables.
# Complex Shapes: Your drawing includes several complex shapes of different sizes and colors.
# Scaling: Use a scaling factor to make drawing different sizes easier.
# Input: The program takes one command line parameter, which alters the scene in some way
# Snake Case All variable names and the code follows Python snake case or camelcase.


t = turtle.Turtle()

t.speed(0)


def draw_star(size, color):
    t.fillcolor(color)
    t.begin_fill()
    for i in range(5):
        t.forward(size)
        t.right(144)
        t.forward(size)
        t.left(72)
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

def red_rectangle(forward, left, height, color):
    if color == 'red':
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

def draw_alien():

    t.penup()
    t.goto(0, -50)
    t.pendown()
    t.fillcolor("green")
    t.begin_fill()
    t.circle(100)  
    t.end_fill()

    t.penup()
    t.goto(-35, 30)
    t.pendown()
    t.fillcolor("gray")
    t.begin_fill()
    t.circle(20)  
    t.end_fill()

    t.penup()
    t.goto(35, 30)
    t.pendown()
    t.begin_fill()
    t.circle(20)  
    t.end_fill()

    t.penup()
    t.goto(-35, 35)
    t.pendown()
    t.fillcolor("black")
    t.begin_fill()
    t.circle(10)  
    t.end_fill()

    t.penup()
    t.goto(35, 35)
    t.pendown()
    t.begin_fill()
    t.circle(10)  
    t.end_fill()

    t.penup()
    t.goto(-40, -10)
    t.pendown()
    t.setheading(-60)
    t.circle(40, 100)  


def draw_shapes():
    t.penup()
    t.goto(450,-300)
    t.pendown()
    orange_triangle(100, 120, 'orange')

    t.penup()
    t.goto(400,350)
    t.pendown()
    red_rectangle(150, 90, 200, 'red')

    t.penup()
    t.goto(500,-300)
    t.pendown()
    blue_square(400, 90, 'blue')
   
    t.penup()
    t.goto(-400,100)
    t.pendown()
    draw_star(100, 'yellow')
    draw_alien()
   
draw_shapes()

turtle.mainloop()