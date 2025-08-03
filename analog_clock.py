import turtle
import math
turtle.title("ANALOG SAAT")
turtle.screensize(1000,1000)
turtle.hideturtle()

def daire(x,y,renk,r):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.fillcolor(renk)
    turtle.begin_fill()
    turtle.circle(r)
    turtle.end_fill()


def rakam():
    r=250## saatin yarı çapı
    for i in range(1,13):
        acı=90-i*30 # saat yönünde yerleştirme
        x=r*math.cos(math.radians(acı))+10 # fazladan eklediğim 10 ve 25 dereceler sayıları tam orasntılı olamsı için
        y=r*math.sin(math.radians(acı))+25
        turtle.penup()
        turtle.goto(x,y)
        turtle.pendown()
        turtle.write(i,align="center",font=("arial",20,"normal"))

def akrep_yelkovan(aci,kalınlık,renk,uzunluk):
        
    turtle.penup()
    turtle.goto(0,0)
    turtle.pendown()
    turtle.pensize(kalınlık)
    turtle.pencolor(renk)
    turtle.setheading(aci)
    turtle.forward(uzunluk)
    
# dış siyah çerçevesi
daire(0,-300,"black",350)

# iç beyaz kısmı

daire(0,-250,"white",300)

# sayıları yerleştirme
rakam()
# saat ve dakika al
saat = int(turtle.numinput("Saat","Saati giriniz (0-23)", 12, minval=0, maxval=23))
dakika = int(turtle.numinput("Dakika","Dakikayı giriniz (0-59)", 0, minval=0, maxval=59))
# Açı hesaplamaları
aci_akrep = 90 - (saat % 12) * 30 - (dakika / 60) * 30
aci_yelkovan = 90 - dakika * 6

# akrep çizimi
akrep_yelkovan(aci_akrep,12,"blue",100)
# yelkovan
akrep_yelkovan(aci_yelkovan,6,"red",225)

turtle.done()




















