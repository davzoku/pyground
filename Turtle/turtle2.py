import turtle
#rainbow turtle
#https://www.safaribooksonline.com/library/cover/9781491951071/360h/
colors=['red','purple','blue','green','yellow', 'orange']

obj=turtle.Pen()
obj.speed(100)
turtle.bgcolor('black')

def drawRainbow():
    for x in range(360):
        obj.pencolor(colors[x%6])
        obj.width(x/100)
        obj.forward(x)
        obj.right(59)

drawRainbow()
turtle.done()
#window exit on click