import pygame
import nastroici 
import sprite

okno=pygame.display.set_mode([nastroici.SHIRINA,nastroici.VISOTA])
chaci=pygame.time.Clock()

sostoanie="igra"

fon=pygame.image.load("resursi/фон.png")
fon=pygame.transform.scale(fon,[nastroici.SHIRINA,nastroici.VISOTA])
menu=pygame.image.load("resursi/меню.jpg")
menu=pygame.transform.scale(menu,[nastroici.SHIRINA,nastroici.VISOTA])


corabl=sprite.Corabl()
cnopcastart=sprite.Cnopca(600,250)
cnopcavixot=sprite.Cnopca(600,450)
zizni=sprite.Zizni()
spisoclazer=[]
spisocmeteorit=[]
m=1
meteoritsob=pygame.USEREVENT
pygame.time.set_timer(meteoritsob,1000)
lazersob=pygame.USEREVENT+1
pygame.time.set_timer(lazersob,1000)

while m==1:
    sobitia=pygame.event.get()  
    for sobitie in sobitia:
        if sobitie.type==pygame.QUIT:
            m=2
        if sobitie.type==meteoritsob:
            meteorit=sprite.Meteorit()
            spisocmeteorit.append(meteorit)
        if sobitie.type==pygame.KEYDOWN:
            if sobitie.key==pygame.K_RIGHT:
                lazer=sprite.Lazer(corabl.pramougol.x,corabl.pramougol.y)
                spisoclazer.append(lazer)
            if sobitie.key==pygame.K_ESCAPE:
                if sostoanie=="igra":
                    sostoanie="menu"
                else:
                    sostoanie="igra"
        if sobitie.type==pygame.MOUSEBUTTONDOWN:
            if cnopcastart.pramougolnic.collidepoint(sobitie.pos):
                sostoanie="igra"
                corabl.hp=3
                spisocmeteorit=[]
                spisoclazer=[]
            if cnopcavixot.pramougolnic.collidepoint(sobitie.pos):
                m=2
            
    
    if sostoanie=='igra':
        for otdelmeteor in spisocmeteorit:
            if corabl.pramougol.colliderect(otdelmeteor.pramougolnic)==True:
                corabl.hp=corabl.hp-1
                spisocmeteorit.remove(otdelmeteor)
                break
        if corabl.hp==0:
            sostoanie="menu"
        for otdelmeteor in spisocmeteorit:
            for otdellazer in spisoclazer:
                if otdelmeteor.pramougolnic.colliderect(otdellazer.pramougolnic)==True:
        
                    spisocmeteorit.remove(otdelmeteor)
                    spisoclazer.remove(otdellazer)
                    corabl.sbitmeteor=corabl.sbitmeteor+1
                    break

                
            
        corabl.dvizjenie()
        for met in spisocmeteorit:
            met.dvizgenie()
        for laz in spisoclazer:
            laz.dvizgenie()

        


        okno.blit(fon,[0,0])
        corabl.otrisovca(okno)
        zizni.otrisovca(okno,corabl.hp)
        for meteor in spisocmeteorit:
            meteor.otrisovca(okno)
        for laz in spisoclazer:
            laz.otrisovca(okno)
    else:
        okno.blit(menu,[0,0])
        cnopcastart.otrisovca(okno)
        cnopcavixot.otrisovca(okno)
    pygame.display.update()
    

    
    chaci.tick(100)
    
