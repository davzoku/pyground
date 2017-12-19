import turtle

#draw cloud

obj= turtle.Turtle()
turtle.bgcolor('lightblue')
obj.speed(100)
obj.forward(150)
obj.left(90)
obj.forward(20)
for x in range (1, 15):
  obj.left(10)
  obj.forward(10)

obj.left(220)
for y in range (1,18):
  obj.left(10)
  obj.forward(12)

obj.left(200)
for z in range (1,18):
  obj.left(10)
  obj.forward(15)


obj.forward(18)
obj.left(90)
obj.forward(260)

turtle.done()
#window exit on click