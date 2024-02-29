import turtle
import random as r
import time as tm

sc = turtle.Screen()

def start():
    sc.clearscreen()
    sc.bgcolor("green")
    sc.tracer(0)
    go = turtle.Turtle("circle")
    go.shapesize(1,1,1)
    go.penup()
    go.color("black")
    go.goto(165,-120)
    go.write("Reset", font=["Arial", 15, "bold"])
    go.color("red")
    go.goto(185,-90)
    go.onclick(lambda x,y: start())
    
    
    pen = turtle.Turtle()
    pen.speed("fastest")

    pen.penup()
    pen.hideturtle()
    pen.goto(-200,75)

    pen.pendown()
    pen.fillcolor("peru")
    pen.begin_fill()
    pen.goto(200,75)
    pen.goto(200,-75)
    pen.goto(-200,-75)
    pen.goto(-200,75)
    pen.end_fill()
    pen.penup()

    pen.goto(170, -75)
    pen.pendown()
    pen.goto(170, 75)
    pen.goto(170, -75)

    pen.goto(160,-75)
    pen.goto(160, 75)
    pen.goto(160,-75)

    pen.goto(150,-75)
    pen.goto(150, 75)
    pen.goto(150,-75)

    pen.goto(140,-75)
    pen.goto(140, 75)
    line = 0
    pen.fillcolor("black")
    for x in range(75,-75,-10):
        if line == 0:
            pen.sety(x)
            pen.setx(140)
            pen.begin_fill()
            pen.setx(pen.xcor() + 10)
            pen.sety(pen.ycor() - 10)
            pen.setx(pen.xcor() - 10)
            pen.sety(pen.ycor() + 10)
            pen.end_fill()
            pen.setx(pen.xcor() + 20)
            pen.begin_fill()
            pen.setx(pen.xcor() + 10)
            pen.sety(pen.ycor() - 10)
            pen.setx(pen.xcor() - 10)
            pen.sety(pen.ycor() + 10)
            pen.end_fill()
            pen.setx(140)
            line += 1
        else:
            pen.sety(x)
            pen.setx(pen.xcor() + 10)
            pen.begin_fill()
            pen.setx(pen.xcor() + 10)
            pen.sety(pen.ycor() - 10)
            pen.setx(pen.xcor() - 10)
            pen.sety(pen.ycor() + 10)
            pen.end_fill()
            pen.setx(140)
            line -= 1

    pen.sety(-75)
    pen.goto(140, 75)
    line = 0
    pen.fillcolor("white")

    for x in range(75,-75,-10):
        if line == 1:
            pen.sety(x)
            pen.setx(140)
            pen.begin_fill()
            pen.setx(pen.xcor() + 10)
            pen.sety(pen.ycor() - 10)
            pen.setx(pen.xcor() - 10)
            pen.sety(pen.ycor() + 10)
            pen.end_fill()
            pen.setx(pen.xcor() + 20)
            pen.begin_fill()
            pen.setx(pen.xcor() + 10)
            pen.sety(pen.ycor() - 10)
            pen.setx(pen.xcor() - 10)
            pen.sety(pen.ycor() + 10)
            pen.end_fill()
            pen.setx(140)
            line -= 1
        else:
            pen.sety(x)
            pen.setx(pen.xcor() + 10)
            pen.begin_fill()
            pen.setx(pen.xcor() + 10)
            pen.sety(pen.ycor() - 10)
            pen.setx(pen.xcor() - 10)
            pen.sety(pen.ycor() + 10)
            pen.end_fill()
            pen.setx(140)
            line += 1

    pen.penup()


    racers = []

    def createRacer(name, color, number):
        racer = turtle.Turtle("turtle")
        racer.color(color)
        racer.penup()
        position = (-190, (65 - (21 * number)))
        racer.goto(position)
        racers.append([racer, name])

    createRacer("Kondrat", "red", 0)

    createRacer("Zach", "blue", 1)

    createRacer("Cory", "green", 2)

    createRacer("Megan", "pink", 3)

    createRacer("Jason", "purple", 4)
    
    createRacer("Trey", "dark orange", 5)

    createRacer("Ryleigh", "yellow", 6)

    pen.goto(-200,75)
    pen.fillcolor("black")
    pen.begin_fill()
    pen.goto(-200,115)
    pen.goto(-115,115)
    pen.goto(-115,75)
    pen.goto(-200,75)
    pen.end_fill()

    green = turtle.Turtle("circle")
    green.color("green")
    green.penup()
    green.goto(-130, 95)

    yellow = turtle.Turtle("circle")
    yellow.color("dark goldenrod")
    yellow.penup()
    yellow.goto(-157, 95)

    red = turtle.Turtle("circle")
    red.color("maroon")
    red.penup()
    red.goto(-185, 95)

    sc.tracer(1)

    tm.sleep(2)

    red.color("red")

    tm.sleep(1)
    red.color("maroon")
    yellow.color("yellow")

    tm.sleep(1)
    yellow.color("dark goldenrod")
    green.color("lime")

    winner = False

    while not winner:
        num = r.randint(0,6)
        Turt = racers[num][0]
        Name = racers[num][1]
        direction = r.randint(0,2)
        if Turt.ycor() >= 65:
            Turt.setheading(0)
            Turt.right(10)
        elif Turt.ycor() <= -65:
            Turt.setheading(0)
            Turt.left(10)
        elif direction == 0:
            Turt.left(5)
        elif direction == 1:
            Turt.right(5)
        Turt.forward(5)
        if Turt.xcor() >= 180:
            text = f"{Name} has won!"
            pen.goto(-200,-95)
            pen.write(text, font=["Arial", 15, "bold"])
            winner = True
    

start()
sc.mainloop() 
