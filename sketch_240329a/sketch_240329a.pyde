# size(1000,1000)
# i = 0
# a = 75
# for i in range(8):
#     ellipse(75,a,150,150)
#     a += 150

# size(1000,1000)
# i = 0
# a = 75
# b = 75
# for i in range(10):
#     ellipse(b,a,150,150)
#     a += 106
#     b += 106

# def setup():
#     size(255,255)
# def draw():
#     i = 0
#     a = 20
#     x = mouseX
#     y = mouseY
#     background(1)
#     fill(x)
#     for i in range(8):
#         ellipse(20,a,40,40)
#         a += 40
#     ellipse(x,y,1,1)

# def setup():
#     size(1000,1000)
# def draw():
#     i = 0
#     a = 5
#     b = 5
#     c = 10
#     for i in range(20):
#         ellipse(b,a,c,c)
#         a += c
#         b += c
#         c += 9

# i = 0
# x = 0
# y = 0
# def setup():
#     size(900,90)
# def draw():
#     global i,x,y
#     for i in range(90):
#         rect(x,y,30,30)
#         x += 30
#         if x > 899:
#             x = 0
#             y += 30

# i = 0
# x = 0
# y = 0
# def setup():
#     size(900,90)
#     frameRate(1)
# def draw():
#     global i,x,y
#     for i in range(90):
#         fill(random(1,255),random(1,255),random(1,255))
#         rect(x,y,30,30)
#         x += 30
#         if x > 899:
#             x = 0
#             y += 30
#         if y > 89:
#             x = 0
#             y = 0

def col(x,y,w,z,x2,y2,w2,z2):
    if (x + w >= x2) and (x <= x2 + w2) and (y + z >= y2) and (y <= y2 + z2):
        return True
    return False
i = 0
x = 0
y = 0
def setup():
    size(900,90)
    rectMode(CENTER)
def draw():
    global i,x,y
    if col(x,y,30,30,mouseX,mouseY,30,30):
        fill(1)
        rect(x,y,30,30)
        fill(255)
    else:
        for i in range(90):
            fill(255)
            rect(x,y,30,30)
            fill(255)
            x += 30
            if x > 899:
                x = 0
                y += 30
    noFill()
    noStroke()
    rect(mouseX,mouseY,30,30)
    
