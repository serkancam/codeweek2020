


# -*- coding: utf-8 -*-
import turtle
import urllib.request
import time
turtle.speed(4)
#istiklal marşı ilk başlık ve ilk iki kıtası intenetten alınıyor
baglanti="https://raw.githubusercontent.com/serkancam/codeweek2020/master/istiklal_marsi.txt"
mars = urllib.request.urlopen(baglanti).readlines()

#bayrak için uygun konuma gidiliyor
turtle.Screen().setup(800,600)
turtle.shape("turtle")
turtle.penup()
turtle.goto(-300,100)
turtle.pendown()
turtle.color("red","red")
#dikdörtgen
turtle.begin_fill()
for i in range(2):
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(100)
	turtle.left(90)
turtle.end_fill()
turtle.penup()
turtle.goto(-240,120)
turtle.color("white","white")
#hilal
turtle.begin_fill()
turtle.circle(30)
turtle.end_fill()
turtle.goto(-230,125)
turtle.pendown()
turtle.color("red","red")
turtle.begin_fill()
turtle.circle(25)
turtle.end_fill()


#yıldız
#yildiz
turtle.penup()
turtle.goto(-200,155)
turtle.pendown()
turtle.color("white","white")
turtle.color("white")
turtle.begin_fill()
for _ in range(5):
    turtle.forward(10)
    turtle.right(120)
    turtle.forward(10)
    turtle.left(48)
turtle.end_fill()
#yıldız bitiş
#istiklal marşı yazılıyor
turtle.penup()
turtle.color("red","red")
turtle.goto(200,250)

x,y=turtle.position()
for misra in mars:
	turtle.write(misra.decode("utf-8"),align="center",font=("Arial",14,"italic"))
	time.sleep(1)
	y-=30
	turtle.goto(x,y)

turtle.hideturtle()
turtle.done()
