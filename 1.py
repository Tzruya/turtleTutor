import turtle
win=turtle.Screen()
p1=turtle.Turtle()
p2=turtle.Turtle()
turtle.mainloop

arr=["red","yellow","green","pink","broun"]

def triangular(d,color,x,y):
  p1.color("white")
  p1.goto(x,y)
  p1.color(color)
  for i in range(3):
    p1.forward(d)
    p1.left(120)
def square(d,color,x,y):
    p1.color("white")
    p1.goto(x,y)
    p1.color(color)
    for i in range(4):
      p1.forward(d)
      p1.left(90)
def circle(r,color,x,y):
  p1.color("white")
  p1.goto(x,y)
  p1.color(color)
  p1.circle(r)
def rectangle(size1,size2,color,x,y):
  p1.color("white")
  p1.goto(x,y)
  p1.color(color) 
  i=0
  while i<2:
    p1.forward(size1)
    p1.left(90)
    p1.forward(size2)
    p1.left(90)
    i=i+1
