'''
Turtle starter code
ATLS 1300
Author: Dr. Z
Author: WILSON SEET
September 10, 2020
'''

from turtle import * 
setup()

#=======Add your code here======

DRAW = Turtle()

panel = Screen()

def squareSprial(x,y):
    "Draws a square sprial at a location"
    DRAW.up()
    DRAW.goto(x,y)
    DRAW.down()
    
    startSize = 1
    inc = 10
    size = 1
    angle = 93
    maxSize = 150
    
    while size <= maxSize:
        DRAW.forward(size)
        DRAW.right(angle)
        size += inc 
        

panel.onclick(squareSprial)
panel.mainloop()

done()