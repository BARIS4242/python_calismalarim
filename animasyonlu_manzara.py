import turtle
import time
turtle.tracer(0)
turtle.hideturtle()
def daire(x, y, renk, r):
    turtle.penup()
    turtle.goto(x, y - r)  # daire merkezden çizilsin
    turtle.pendown()
    turtle.fillcolor(renk)
    turtle.begin_fill()
    turtle.circle(r)
    turtle.end_fill()


    
def dikdortgen(x,y,renk,uzun_kenar,kısa_kenar):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.fillcolor(renk)
    turtle.begin_fill()
    for i in range(2):
        turtle.forward(uzun_kenar)
        turtle.left(90)
        turtle.forward(kısa_kenar)
        turtle.left(90)
    turtle.end_fill()

def kare(x,y,renk,kenar):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.fillcolor(renk)
    turtle.begin_fill()
    for i in range(4):
        turtle.forward(kenar)
        turtle.left(90)
        
    turtle.end_fill()


def ucgen(x,y,renk,l):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.fillcolor(renk)
    turtle.begin_fill()
    for i in range(3):
        turtle.forward(l)
        turtle.left(120)
    turtle.end_fill()


def yıldız(x,y,renk,kenar):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.fillcolor(renk)
    turtle.begin_fill()
    for i in range(5):
        turtle.forward(kenar)
        turtle.right(144)
        turtle.forward(kenar)
        turtle.right(-72)
    turtle.end_fill()


def gece_manzarası():
    turtle.bgcolor("midnightblue")
    turtle.clear()
    time.sleep(0.3)

    daire(-200,200,"grey",40)#ay

    # yıldızlar
    yıldız(-200,150,"yellow",10)
    yıldız(-150,180,"yellow",10)
    yıldız(100,160,"yellow",10)
    yıldız(-60,200,"yellow",10)
    yıldız(180,160,"yellow",10)
        
    

    ucgen(-100,100,"red",200)# çatı


    kare(-100,-100,"yellow",200)# gövdeler

    kare(-80,20,"blue",40)#pencere
    kare(40,20,"blue",40)

    dikdortgen(-25,-100,"brown",50,100)# kapı
    dikdortgen(-260,-100,"brown",20,60) #ağaç

    # yapraklar
    daire(-260,-40,"green",30)
    daire(-240,-40,"green",30)
    daire(-250,-40,"green",35)

    # dumanlar
    daire(10,120,"grey",10)
    daire(20,140,"grey",8)
    daire(30,160,"grey",6)

def gunduz_manzarası():
    turtle.bgcolor("skyblue")
    turtle.clear()
    
    ucgen(-100,100,"red",200)# çatı


    kare(-100,-100,"yellow",200)# gövdeler

    kare(-80,20,"blue",40)#pencere
    kare(40,20,"blue",40)

    dikdortgen(-25,-100,"brown",50,100)# kapı

    daire(200,200,"yellow",40)# güneş

    dikdortgen(-260,-100,"brown",20,60) #ağaç

    # yapraklar
    daire(-260,-40,"green",30)
    daire(-240,-40,"green",30)
    daire(-250,-40,"green",35)

    # dumanlar
    daire(10,120,"grey",10)
    daire(20,140,"grey",8)
    daire(30,160,"grey",6)


def gunes_animasyonu():
    for i in range(300, -300, -10):  # sağdan sola hareket
        turtle.bgcolor("skyblue")    # sadece gündüz rengi
        
        turtle.clear()               # ekranı temizle
        
        # Manzarayı tekrar çiz
        ucgen(-100, 100, "red", 200)     # çatı
        kare(-100, -100, "yellow", 200)  # gövde
        kare(-80, 20, "blue", 40)        # pencere
        kare(40, 20, "blue", 40)
        dikdortgen(-25, -100, "brown", 50, 100)  # kapı
        dikdortgen(-260, -100, "brown", 20, 60)  # ağaç
        daire(-260, -40, "green", 30)             # yapraklar
        daire(-240, -40, "green", 30)
        daire(-250, -40, "green", 35)
        daire(10, 120, "grey", 10)                 # dumanlar
        daire(20, 140, "grey", 8)
        daire(30, 160, "grey", 6)
        
        # Güneş hareket ediyor (x koordinatı = i)
        daire(i, 200, "yellow", 40)
        
        turtle.update()  # ekranı yenile
        time.sleep(0.05) # animasyon hızı




def ay_animasyonu():
    for i in range(300, -300, -10):  # sağdan sola hareket
        turtle.bgcolor("midnightblue")  # gece rengi
        turtle.clear()
        
        ucgen(-100, 100, "red", 200)     # çatı
        kare(-100, -100, "yellow", 200)  # gövde
        kare(-80, 20, "blue", 40)        # pencere
        kare(40, 20, "blue", 40)
        dikdortgen(-25, -100, "brown", 50, 100)  # kapı
        dikdortgen(-260, -100, "brown", 20, 60)  # ağaç
        
        daire(-260, -40, "green", 30)             # yapraklar
        daire(-240, -40, "green", 30)
        daire(-250, -40, "green", 35)
        
        daire(10, 120, "grey", 10)                 # dumanlar
        daire(20, 140, "grey", 8)
        daire(30, 160, "grey", 6)
        
        daire(i, 200, "grey", 40)  # ay hareket ediyor
        
        turtle.update()
        time.sleep(0.05)





#  TUŞLARLARLA GEÇİŞ SAĞLAMA    
turtle.listen()
turtle.onkey(gece_manzarası,"a") # n tuşuna bastığında gece manzarasını çizer
turtle.onkey(gunduz_manzarası,"b")# g tuşuna bastığında gündüz manzarasını çizer
turtle.onkey(gunes_animasyonu,"c")# a tuşuna bastığında güneş anımasyonunu  manzarasını çalıştırır.
turtle.onkey(ay_animasyonu,"d")# b tuşuna bastığında güneş anımasyonunu  manzarasını çalıştırır.
turtle.done()






























