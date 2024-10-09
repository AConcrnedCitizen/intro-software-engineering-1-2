'''
*******************************
Author:
u3275885
Assignment:
Assessment 2 - Problem 4
4/10/2024
*******************************
'''
import turtle

x = turtle.Turtle()
x.speed(100)

# Function to draw a circle with a specified colour
def draw_circle(colour):
    x.fillcolor(colour)
    # Fill the circle with the specified colour
    x.begin_fill()
    x.circle(8)
    x.end_fill()

x.width(5)
x.color("black")

def draw_rectangle(size, filled=False):
    if filled:
        x.begin_fill()
        
    # Caluclate the width and height of the rectangle
    width = 100 * size
    height = 200 * size
    
    if filled:
        height += 20 # Increase the height if the rectangle is filled
    
    for i in range(2):
        x.forward(width)
        x.left(90)
        x.forward(height)
        x.left(90)
        
    if filled:
        x.end_fill()

# Draw the traffic light
draw_rectangle(1)
x.penup()
x.goto(10, 10)
x.pendown()
draw_rectangle(0.8, True)
x.penup()
x.goto(50, 30)
draw_circle("green")
x.goto(50, 90)
draw_circle("yellow")
x.goto(50, 150)
draw_circle("red")
x.hideturtle()
turtle.done()