from turtle import Turtle,Screen
import random
import pyfiglet
ascii_banner = pyfiglet.figlet_format("Welcome to Dice Roll Simulator")
print(ascii_banner)



print("there is a change")



roll_dice = True
while roll_dice:

    user = input("do you want to roll the dice?(yes/no)").lower()
    if user == 'yes':
        def dice():
            roll.speed(0)
            roll.begin_fill()
            roll.circle(10)
            roll.color("red")
            roll.end_fill()
            roll.hideturtle()

        roll = Turtle()
        roll.color("red")
        screen = Screen()
        screen.bgcolor("white")
        screen.setup(height=300, width=300)

        border_pen = Turtle()
        border_pen.speed(0)
        border_pen.color("black")
        border_pen.pensize(5)
        border_pen.up()
        border_pen.goto(-100, -100)
        for i in range(4):
            border_pen.down()
            border_pen.forward(200)
            border_pen.left(90)
            border_pen.up()
            border_pen.hideturtle()

        dice_number = random.randint(1,6)
        if dice_number == 1:
            POSITIONS = [(0,0)]
            for position in POSITIONS:
                roll.penup()
                roll.goto(position)
                roll.pendown()
                dice()
                roll.hideturtle()



        elif dice_number == 2:
            POSITIONS = [(-60, -60), (60, 60)]
            for position in POSITIONS:
                roll.penup()
                roll.goto(position)
                roll.pendown()
                dice()
                roll.hideturtle()
        elif dice_number == 3:
            POSITIONS = [(-60, -60), (0, 0), (60, 60)]
            for position in POSITIONS:
                roll.penup()
                roll.goto(position)
                roll.pendown()
                dice()
                roll.hideturtle()
        elif dice_number == 4:
            POSITIONS = [(-60, -60), (60, -60), (-60, 60), (60, 60)]
            for position in POSITIONS:
                roll.penup()
                roll.goto(position)
                roll.pendown()
                dice()
                roll.hideturtle()
        elif dice_number == 5:
            POSITIONS = [(-60, -60), (60, -60), (0, 0), (-60, 60), (60, 60)]
            for position in POSITIONS:
                roll.penup()
                roll.goto(position)
                roll.pendown()
                dice()
                roll.hideturtle()
        elif dice_number == 6:
            POSITIONS = [(-60, -60), (60, -60), (-60, 0), (60, 0), (-60, 60), (60, 60)]
            for position in POSITIONS:
                roll.penup()
                roll.goto(position)
                roll.pendown()
                dice()
                roll.hideturtle()
        screen.exitonclick()


    elif user == 'no':
        roll dice = False




