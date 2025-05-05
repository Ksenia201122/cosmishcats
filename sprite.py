import pygame
import random
import nastroici
class Corabl:
    def __init__(self):
        self.cartinca=pygame.image.load("resursi/корабль.png")
        self.cartinca=pygame.transform.scale(self.cartinca,[300,300]) 
        shirina=self.cartinca.get_width()
        visota=self.cartinca.get_height()
        self.pramougol=pygame.rect.Rect([100,100],[shirina,visota])
        self.skorost=3
        self.hp=3
        self.sbitmeteor=0
    def otrisovca(self,okno):
        okno.blit(self.cartinca,self.pramougol)
    def dvizjenie(self):
        clavishi=pygame.key.get_pressed()
        if clavishi[pygame.K_UP]==True:
            self.pramougol.y=self.pramougol.y-3
        if clavishi[pygame.K_DOWN]==True:
            self.pramougol.y=self.pramougol.y+3
class Meteorit:
    def __init__(self):
        self.cartina=pygame.image.load("resursi/метеорт.png")
        self.cartina=pygame.transform.scale(self.cartina,[300,300])
        shirina=self.cartina.get_width()
        visota=self.cartina.get_height()
        self.pramougolnic=pygame.rect.Rect([1400,random.randint(0,nastroici.VISOTA)],[shirina,visota])
        self.scorostx=random.randint(1,5)
        self.scorosty=random.randint(-1,1)
    def otrisovca(self,okno):
        okno.blit(self.cartina,self.pramougolnic)
    def dvizgenie(self):
        self.pramougolnic.x=self.pramougolnic.x-self.scorostx
        self.pramougolnic.y=self.pramougolnic.y-self.scorosty
class Lazer:
    def __init__(self,x,y):
        self.cartina=pygame.image.load("resursi/лазер.png")
        self.cartina=pygame.transform.rotate(self.cartina,-90)
        self.cartina=pygame.transform.scale(self.cartina,[300,300])
        shirina=self.cartina.get_width()
        visota=self.cartina.get_height()
        self.pramougolnic=pygame.rect.Rect([x,y],[shirina,visota])
        self.scorostx=5
    def otrisovca(self,okno):
        okno.blit(self.cartina,self.pramougolnic)
    def dvizgenie(self):
        self.pramougolnic.x=self.pramougolnic.x+self.scorostx

class Zizni:
    def __init__(self):
        self.serdce=pygame.image.load("resursi/сердце.png")
        self.serdce=pygame.transform.scale(self.serdce,[150,150])
        shirina=self.serdce.get_width()
        visota=self.serdce.get_height()
        self.pramougol=pygame.rect.Rect([1300,100],[shirina,visota])
        self.hp=3
    def otrisovca(self,okno,f):
         self.pramougol.x=1300
         while f>0:
            okno.blit(self.serdce,self.pramougol)
            f=f-1 
            self.pramougol.x=self.pramougol.x-150
class Cnopca:
    def __init__(self,x,y):
        self.cartina=pygame.image.load("resursi/PNG/UI/buttonBlue.png")
        self.cartina=pygame.transform.scale(self.cartina,[300,100])
        shirina=self.cartina.get_width()
        visota=self.cartina.get_height()
        self.pramougolnic=pygame.rect.Rect([x,y],[shirina,visota])
    def otrisovca(self,okno):
        okno.blit(self.cartina,self.pramougolnic)

            


        

        
        

        

        