from pygame import*

okno = display.set_mode((800,800))
fps = time.Clock() 
game = True

font.init()
wr = font.Font(None, 35)


class gameobj(sprite.Sprite):
    def __init__(self, img, x,y,w,h):
        super().__init__()
        self.image = transform.scale(image.load(img), (w,h))
        self.rect = self.image.get_rect() 
        self.rect.x = x
        self.rect.y = y
    def ris(self):
        okno.blit(self.image, (self.rect.x, self.rect.y))

from random import choice, randint


with open('karta.txt') as file:
    karta = file.readlines()


x1 =0
y1 = 0 
mymap = []


for y in karta:
    line = y.split(' ')
    for x in line:
        if '1' in x:
            w = gameobj('rbhgbx.jpeg' ,x1,y1,50,50)
            mymap.append(w)
        if '2' in x:
            w = gameobj('ff.png' ,x1,y1,50,50)
            mymap.append(w)
        x1 +=50
    x1 = 0
    y1 +=50





class pl(sprite.Sprite):
    def __init__(self, img, x,y,w,h):
        super().__init__()
        self.image = transform.scale(image.load(img), (w,h))
        self.rect = self.image.get_rect() 
        self.rect.x = x
        self.rect.y = y
        self.napr = 'vverh'
    def ris(self):
        self.image1 = transform.scale(self.image,(40,40))
        self.image2 = transform.rotate(self.image,180)
        self.image3= transform.rotate(self.image, 90)
        self.image4 = transform.rotate(self.image, -90)
        if self.napr == 'vverh':
            okno.blit(self.image1, (self.rect.x, self.rect.y))
        elif self.napr =='vniz':
            okno.blit(self.image2, (self.rect.x, self.rect.y))
        elif self.napr =='levo':
            okno.blit(self.image3, (self.rect.x, self.rect.y))
        elif self.napr =='pravo':
            okno.blit(self.image4, (self.rect.x, self.rect.y))






class vr(sprite.Sprite):
    def __init__(self, img, x,y,w,h):
        super().__init__()
        self.image = transform.scale(image.load(img), (w,h))
        self.rect = self.image.get_rect() 
        self.rect.x = x
        self.rect.y = y
        self.napr = 'vverh'
    def ris(self):
        self.image1 = transform.scale(self.image,(40,40))
        self.image2 = transform.rotate(self.image,180)
        self.image3= transform.rotate(self.image, 90)
        self.image4 = transform.rotate(self.image, -90)
        if self.napr == 'vverh':
            okno.blit(self.image1, (self.rect.x, self.rect.y))
        elif self.napr =='vniz':
            okno.blit(self.image2, (self.rect.x, self.rect.y))
        elif self.napr =='levo':
            okno.blit(self.image3, (self.rect.x, self.rect.y))
        elif self.napr =='pravo':
            okno.blit(self.image4, (self.rect.x, self.rect.y))





    def move(self):
        self.ris()
        kn = key.get_pressed()
        if kn[K_UP]:
            self.napr = 'vverh':
            self.rect.y -=3
        elif kn[K_DOWN]:
            self.napr = 'vniz':
            self.rect.y +=3
        elif kn[K_LEFT]:
            self.napr = 'levo':
            self.rect.x -=3
        elif kn[K_RIGHT]:
            self.napr = 'pravo':
            self.rect.x +=3



def move(self):
        self.ris()
        kn = key.get_pressed()
        if kn[K_W]:
            self.napr = 'vverh':
            self.rect.y -=3
        elif kn[K_S]:
            self.napr = 'vniz':
            self.rect.y +=3
        elif kn[K_A]:
            self.napr = 'levo':
            self.rect.x -=3
        elif kn[K_D]:
            self.napr = 'pravo':
            self.rect.x +=3

tank = pl('tanchiki.png',100,100,30,30)
tnk = vr('тнк.png',100,100,30,30)







class pula(sprite.Sprite):
    def __init__(self, img, x,y):
        super().__init__()
        self.image = transform.scale(image.load(img), (10,10))
        self.rect = self.image.get_rect() 
        self.rect.x = x
        self.rect.y = y
        self.napr = tank.napr
    def ris(self):
        okno.blit(self.image, (self.rect.x, self.rect.y))
        if self.napr == 'vverh':
            self.rect.y -=8
        elif self.napr == 'vniz':
            self.rect.y +=8
        elif self.napr =='levo':
            self.rect.x -=8
        elif self.napr == 'pravo':
            self.rect.x +=8



class pulavr(sprite.Sprite):
    def __init__(self, img, x,y):
        super().__init__()
        self.image = transform.scale(image.load(img), (10,10))
        self.rect = self.image.get_rect() 
        self.rect.x = x
        self.rect.y = y
        self.napr = tank.napr
    def ris(self):
        okno.blit(self.image, (self.rect.x, self.rect.y))
        if self.napr == 'vverh':
            self.rect.y -=8
        elif self.napr == 'vniz':
            self.rect.y +=8
        elif self.napr =='levo':
            self.rect.x -=8
        elif self.napr == 'pravo':
            self.rect.x +=8


def move(self):
        self.ris()
        kn = key.get_pressed()
        if self.napr == 'vverh':
            self.rect.y -=6
        elif self.napr == 'vniz':
            self.rect.y +=6
        elif self.napr =='levo':
            self.rect.x -=6
        elif self.napr == 'pravo':
            self.rect.x +=6





bull = []

while game:
    for e in event.get(): 
        if e.type == QUIT:
            game = False 
        if e.type == KEYDOWN:
            if e.key == K_SPACE:
                p = pula('зщ.png', tank.rect.x , tank.rect.y )
                bull.append(p)
    okno.fill((0,0,0))
    for pp in bull:
        pp.ris()
    for w1 in mymap:
        w1.ris()
        try:
            for pp in bull:
                if sprite.collide_rect(w1,pp)
                bull.remove(pp)
                mymap.remove(w1)
        except:
            pass
        if sprite.collide_rect(w1,tank):
            if tank.napr == 'vverh':
                tank.rect.y +=4
            if tank.napr == 'vniz':
                tank.rect.y -=4
            if tank.napr == 'levo':
                tank.rect.x +=4
            if tank.napr == 'pravo':
                tank.rect.x -=4

    kol.move()
    fps.tick(60)
    display.update()
