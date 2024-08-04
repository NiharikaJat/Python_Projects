import turtle
import time
import random

WIDTH,HEIGHT=500,500
COLORS=['chocolate','red','cyan','purple','pink','green','brown','aqua','orange','black']

def get_num_of_racers():
    racers=0
    while True:
        racers=input("Enter number of racers(2-10): ")
        if racers.isdigit():
            racers=int(racers)
        else:
            print('Invalid value!')
            continue

        if 2<=racers<=10:
            return racers
        else:
            print('Enter racers between 2 and 10')

def init_turtle():
    screen=turtle.Screen()
    screen.setup(WIDTH,HEIGHT)
    screen.title('Turtle Racing!')

def create_turtle(colors):
    turtles=[]
    spacingx = WIDTH//(len(colors)+1)
    for i,color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape('turtle')
        racer.left(90)
        racer.penup()
        racer.setpos(-WIDTH//2 + (i+1)*spacingx, -HEIGHT//2 + 20)
        racer.pendown()
        turtles.append(racer)
    return turtles

def race(colors):
    turtles=create_turtle(colors)
    while True:
        for racer in turtles:
            distance=random.randrange(1,20)
            racer.forward(distance)

            x,y=racer.pos()
            if y>=HEIGHT//2 - 10:
                return colors[turtles.index(racer)]

def main():
    racers=get_num_of_racers()
    init_turtle()

    random.shuffle(COLORS)
    colors=COLORS[:racers]
    winner=race(colors)
    print("The winner is the ",winner," color turtle")
    time.sleep(10)

main()
