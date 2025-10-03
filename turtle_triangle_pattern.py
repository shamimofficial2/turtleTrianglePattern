import turtle as t

screen = t.Screen()
screen.setup(width = 1.0, height = 1.0)

t.title("Turtle Triangle Pattern")
t.color("red")
t.bgcolor("black")
t.speed(0)
t.pensize(2)
t.hideturtle()

i = 0
while i < 36:
    for j in range(3):
        t.forward(200)
        t.left(120)
    t.right(10)
    i += 1

t.exitonclick()