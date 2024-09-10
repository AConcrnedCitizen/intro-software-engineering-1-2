import turtle

x = turtle.Turtle()
x.speed(100)

def draw_circle(colour):
    x.fillcolor(colour)
    x.begin_fill()
    x.circle(8)
    x.end_fill()

x.width(5)
x.color("black")

def draw_rectangle(size, filled=False):
    if filled:
        x.begin_fill()
        
    width = 100 * size
    
    height = 200 * size
    if filled:
        height += 20
    
    for i in range(2):
        x.forward(width)
        x.left(90)
        x.forward(height)
        x.left(90)
        
    if filled:
        x.end_fill()

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