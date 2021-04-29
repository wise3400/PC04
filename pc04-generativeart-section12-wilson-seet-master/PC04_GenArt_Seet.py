'''
Turtle starter code
ATLS 1300
Author: Dr. Z
Author: WILSON SEET
September 18, 2020
'''
'''
Description: I made a ridiculous messy star that scribbles
up and down with colorful colors and some objects that 
are also colorful using lists.
'''
from turtle import * #import the library of commands that you'd like to use
import random
colormode(255)
bgcolor("black")

#Create a panel to draw on. 
panel = Screen()
w = 600 # width of panel
h = 600 # height of panel
panel.setup(width=w, height=h) #600 x 600 is a decent size to work on. 
#You can experiment by making it the size of your screen or super tiny!

#Don't change this line (puts (0,0) at upper left corner)
panel.setworldcoordinates(0, w, h, 0)

#=======Add your code here======
#My 4 turtles!
randomshape1Star = Turtle()
randomshape2Square = Turtle()
justAColorfulCircle = Turtle()
randomCircle = Turtle()

#Color Lists
colors1  = ["red","blue","green","pink"] 
colors2 = ["yellow","orange","brown","red","darkblue"]


#Speed to make the Turtle go faster
randomshape1Star.speed(1000)
randomshape2Square.speed(1000)
justAColorfulCircle.speed(1000)
randomCircle.speed(1000)

randomshape1Star.penup()
#A for loop that draws a messy star 40 times. 
#Color changes based on "colors1 list" 40 times.
for i in range(40):
    color = random.choice(colors1)
    x1=random.randint(-40,430)
    y1=random.randint(-40,430)
    randomshape1Star.goto(x1,y1) #moving stars to random location
    randomshape1Star.pensize(20)
    randomshape1Star.down()
    randomshape1Star.color(color)
    randomshape1Star.forward(40)
    randomshape1Star.left(300)

randomshape2Square.penup()
randomshape2Square.goto(400,500)
#A for loop that draws a square that goes 100 times
#Color changes based on "colors2" 100 times
for m in range(100):
  color=random.choice(colors2)
  randomshape2Square.pensize(17)
  randomshape2Square.pendown()
  randomshape2Square.color(color)
  randomshape2Square.forward(50)
  randomshape2Square.left(90)

#A for loop that draws a colorful circle that goes 20 times  
#Color changes based on "colors2" 20 times
for c in range(20):
  justAColorfulCircle.goto(500,200)
  color = random.choice(colors2)
  justAColorfulCircle.color(color)
  justAColorfulCircle.pensize(20)
  justAColorfulCircle.circle(50)

#Random Circles 
randomCircle.goto(300,500)
randomCircle.begin_fill()
randomCircle.color("blue")
randomCircle.circle(25)
randomCircle.end_fill()

randomCircle.goto(100,450)
randomCircle.begin_fill()
randomCircle.color("green")
randomCircle.circle(45)
randomCircle.end_fill()
randomCircle.hideturtle()
