#!/usr/bin/python

#Zambies game made by Jake Hansen in 2014
import pygame, sys, time, random
from pygame.locals import *
pygame.init()

screen=pygame.display.set_mode((800,600),0,32)
pygame.display.set_caption("ZAAAAMBIES!!!")

top=pygame.image.load("guntop.png").convert()
bottom=pygame.image.load("gunbottom.png").convert()
backg=pygame.image.load("zambiesbackg.jpg").convert()
ammo=pygame.image.load("ammocount.jpg").convert()
menu=pygame.image.load("menu.jpg").convert()
lose=pygame.image.load("z_death.jpg").convert()
win=pygame.image.load("z_win.jpg").convert()
easy=pygame.image.load("level_easy.jpg").convert()
medium=pygame.image.load("level_medium.jpg").convert()
hard=pygame.image.load("level_hard.jpg").convert()
health=pygame.image.load("z_health.jpg").convert()
reloading=pygame.image.load("z_reloading.jpg").convert()

bean=True
go=False
shoot=False
shots=12
rel_time=0

class player:
    def __init__(self,urlives):
        self.urlives=urlives

class zambies:
    def __init__(self,life,speed):
        zx=random.randint(50,750)
        loop=True
        timer=5
        hits=0

        self.speed=speed
        self.hits=hits
        self.timer=timer
        self.life=life
        self.zx=zx
        self.loop=loop

    def dostuff(self):
        if self.loop==True:

            if self.timer<=203:
                self.timer+=milliseconds/self.speed

            pygame.draw.rect(screen,(0,200,0),Rect((self.zx-self.timer/2+self.timer*.055,100+self.timer*.3),(self.timer*.9,self.timer*.8)))
            pygame.draw.rect(screen,(0,0,0),Rect((self.zx-self.timer/2,100+self.timer),(self.timer,self.timer*1.5)))
            pygame.draw.rect(screen,(0,200,0),Rect(((self.zx-self.timer/2)-self.timer/5,100+self.timer+self.timer/5),(self.timer/3,self.timer/3)))
            pygame.draw.rect(screen,(0,200,0),Rect(((self.zx-self.timer/2)+self.timer*.85,100+self.timer+self.timer/5),(self.timer/3,self.timer/3)))
            pygame.draw.rect(screen,(240,0,0),Rect((self.zx-self.timer/4+self.timer*.055,100+self.timer*.55),(self.timer*.1,self.timer*.1)))
            pygame.draw.rect(screen,(240,0,0),Rect((self.zx-self.timer/-15+self.timer*.055,100+self.timer*.55),(self.timer*.1,self.timer*.1)))
            
            if shoot==True:      
                if mx>=self.zx-self.timer/2+self.timer*.055 and mx<=(self.zx-self.timer/2+self.timer*.055)+self.timer*.9 and my>=100+self.timer*.3 and my<=(100+self.timer*.3)+self.timer*.8:
                    self.life-=2
                elif mx>=(self.zx-self.timer/2)-self.timer/5 and mx<=((self.zx-self.timer/2)-self.timer/5)+self.timer and my>=100+self.timer and my<=(100+self.timer)+self.timer*1.5:
                    self.life-=1
                    
            if self.life<=0:
                self.loop=False

            if self.timer>=203:
                milliseconds2=clock.tick()
                self.hits+=milliseconds2/40.
                if self.hits>=3.5:
                    you.urlives-=1
                    self.hits=0

while bean==True:
    mx,my=pygame.mouse.get_pos()
    
    screen.blit(menu,(0,0))
    
    time.sleep(0.005)
    pygame.display.update()

    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
            
        if event.type==MOUSEBUTTONDOWN:            
            if mx>=375 and mx<=450 and my>=150 and my<=170:
                you=player(20)

                zam1=zambies(10,100.)
                zam2=zambies(9,100.)
                zam3=zambies(9,100.)
                zam4=zambies(10,80.)
                zam5=zambies(9,80.)
                zam6=zambies(10,90.)
                zam7=zambies(10,90.)
                zam8=zambies(10,80.)
                zam9=zambies(10,80.)
                zam10=zambies(12,70.)
                zam11=zambies(12,70.)
                zam12=zambies(12,60.)
                zam13=zambies(12,60.)
                zam14=zambies(12,55.)
                zam15=zambies(14,55.)
                zam16=zambies(14,50.)
                zam17=zambies(14,50.)
                zam18=zambies(14,40.)
                zam19=zambies(16,40.)
                zam20=zambies(16,40.)
                zam21=zambies(14,40.)
                zam22=zambies(14,35.)
                zam23=zambies(14,30.)
                zam24=zambies(14,30.)
                
                level=easy
                bean=False
                go=True

            elif mx>=375 and mx<=450 and my>=175 and my<=195:
                you=player(15)

                zam1=zambies(10,100.)
                zam2=zambies(10,100.)
                zam3=zambies(10,100.)
                zam4=zambies(10,80.)
                zam5=zambies(12,80.)
                zam6=zambies(12,90.)
                zam7=zambies(12,90.)
                zam8=zambies(12,80.)
                zam9=zambies(12,80.)
                zam10=zambies(14,70.)
                zam11=zambies(14,80.)
                zam12=zambies(14,60.)
                zam13=zambies(14,60.)
                zam14=zambies(14,50.)
                zam15=zambies(14,50.)
                zam16=zambies(15,50.)
                zam17=zambies(14,40.)
                zam18=zambies(14,40.)
                zam19=zambies(16,35.)
                zam20=zambies(16,35.)
                zam21=zambies(16,35.)
                zam22=zambies(16,30.)
                zam23=zambies(18,30.)
                zam24=zambies(18,30.)
                
                level=medium
                bean=False
                go=True

            elif mx>=375 and mx<=450 and my>=200 and my<=220:
                you=player(12)

                zam1=zambies(12,100.)
                zam2=zambies(12,100.)
                zam3=zambies(12,100.)
                zam4=zambies(12,70.)
                zam5=zambies(12,70.)
                zam6=zambies(14,90.)
                zam7=zambies(14,90.)
                zam8=zambies(14,80.)
                zam9=zambies(14,60.)
                zam10=zambies(14,60.)
                zam11=zambies(16,80.)
                zam12=zambies(16,50.)
                zam13=zambies(16,50.)
                zam14=zambies(16,40.)
                zam15=zambies(16,40.)
                zam16=zambies(16,40.)
                zam17=zambies(18,40.)
                zam18=zambies(18,40.)
                zam19=zambies(18,40.)
                zam20=zambies(18,35.)
                zam21=zambies(18,35.)
                zam22=zambies(20,35.)
                zam23=zambies(20,30.)
                zam24=zambies(20,28.)
                
                level=hard
                bean=False
                go=True

pygame.mouse.set_visible(0)

clock=pygame.time.Clock()

while go==True:    
    mx,my=pygame.mouse.get_pos()
    milliseconds=clock.tick()

    screen.blit(backg,(0,0))

    zam1.dostuff()
    zam2.dostuff()
    if zam1.loop==False and zam2.loop==False:
        zam3.dostuff()
        zam4.dostuff()
        zam5.dostuff()
    if zam3.loop==False and zam4.loop==False and zam5.loop==False:
        zam6.dostuff()
        zam7.dostuff()
    if zam6.loop==False and zam7.loop==False:
        zam8.dostuff()
        zam9.dostuff()
        zam10.dostuff()
    if zam8.loop==False and zam9.loop==False and zam10.loop==False:
        zam11.dostuff()
        zam12.dostuff()
        zam13.dostuff()
    if zam11.loop==False and zam12.loop==False and zam13.loop==False:
        zam14.dostuff()
        zam15.dostuff()
        zam16.dostuff()
        zam17.dostuff()
    if zam14.loop==False and zam15.loop==False and zam16.loop==False and zam17.loop==False:
        zam18.dostuff()
        zam19.dostuff()
        zam20.dostuff()
    if zam18.loop==False and zam19.loop==False and zam20.loop==False:
        zam21.dostuff()
        zam22.dostuff()
        zam23.dostuff()
        zam24.dostuff()
    if zam21.loop==False and zam22.loop==False and zam23.loop==False and zam24.loop==False:
        screen.blit(backg,(0,0))
        screen.blit(health,(0,0))
        screen.blit(level,(0,30))
        pygame.draw.rect(screen,(200,0,0),Rect((63,1),(you.urlives*10,15)))
        screen.blit(win,(295,200))
        pygame.display.update()
        time.sleep(1.75)
        pygame.quit()
        sys.exit()

    shoot=False

    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
        if event.type==MOUSEBUTTONDOWN:
            if event.button==1 and shots>=1:
                pygame.draw.circle(screen,(150,0,0),(mx,my),20,0)
                shoot=True
                shots-=1
                
            if event.button==3 and shots!=12:
                shots=0
    
        elif event.type!=MOUSEBUTTONUP:
            shoot=False

    if you.urlives<=0:
        screen.blit(backg,(0,0))
        screen.blit(lose,(280,200))
        screen.blit(level,(0,30))
        pygame.display.update()
        time.sleep(1.75)
        pygame.quit()
        sys.exit()

    if shots<=0:
        rel_time+=milliseconds/1000.
        if rel_time>=.65:
            shots=12
            rel_time=0
    
    screen.blit(top,(mx-16,my))
    screen.blit(bottom,(mx-12,my+31))
    pygame.draw.rect(screen,(40,40,40),Rect((mx-15,my-10),(10,10)))
    pygame.draw.rect(screen,(40,40,40),Rect((mx+7,my-10),(10,10)))
    pygame.draw.rect(screen,(0,0,0),Rect((mx-2,my-5),(5,5)))
    screen.blit(health,(0,0))
    screen.blit(level,(0,30))

    if shots==12:
        screen.blit(ammo,(788,2))
        screen.blit(ammo,(773,2))
        screen.blit(ammo,(758,2))
        screen.blit(ammo,(743,2))
        screen.blit(ammo,(728,2))
        screen.blit(ammo,(713,2))
        screen.blit(ammo,(698,2))
        screen.blit(ammo,(683,2))
        screen.blit(ammo,(668,2))
        screen.blit(ammo,(653,2))
        screen.blit(ammo,(638,2))
        screen.blit(ammo,(623,2))
    elif shots==11:
        screen.blit(ammo,(788,2))
        screen.blit(ammo,(773,2))
        screen.blit(ammo,(758,2))
        screen.blit(ammo,(743,2))
        screen.blit(ammo,(728,2))
        screen.blit(ammo,(713,2))
        screen.blit(ammo,(698,2))
        screen.blit(ammo,(683,2))
        screen.blit(ammo,(668,2))
        screen.blit(ammo,(653,2))
        screen.blit(ammo,(638,2))
    elif shots==10:
        screen.blit(ammo,(788,2))
        screen.blit(ammo,(773,2))
        screen.blit(ammo,(758,2))
        screen.blit(ammo,(743,2))
        screen.blit(ammo,(728,2))
        screen.blit(ammo,(713,2))
        screen.blit(ammo,(698,2))
        screen.blit(ammo,(683,2))
        screen.blit(ammo,(668,2))
        screen.blit(ammo,(653,2))
    elif shots==9:
        screen.blit(ammo,(788,2))
        screen.blit(ammo,(773,2))
        screen.blit(ammo,(758,2))
        screen.blit(ammo,(743,2))
        screen.blit(ammo,(728,2))
        screen.blit(ammo,(713,2))
        screen.blit(ammo,(698,2))
        screen.blit(ammo,(683,2))
        screen.blit(ammo,(668,2))
    elif shots==8:
        screen.blit(ammo,(788,2))
        screen.blit(ammo,(773,2))
        screen.blit(ammo,(758,2))
        screen.blit(ammo,(743,2))
        screen.blit(ammo,(728,2))
        screen.blit(ammo,(713,2))
        screen.blit(ammo,(698,2))
        screen.blit(ammo,(683,2))
    elif shots==7:
        screen.blit(ammo,(788,2))
        screen.blit(ammo,(773,2))
        screen.blit(ammo,(758,2))
        screen.blit(ammo,(743,2))
        screen.blit(ammo,(728,2))
        screen.blit(ammo,(713,2))
        screen.blit(ammo,(698,2))
    elif shots==6:
        screen.blit(ammo,(788,2))
        screen.blit(ammo,(773,2))
        screen.blit(ammo,(758,2))
        screen.blit(ammo,(743,2))
        screen.blit(ammo,(728,2))
        screen.blit(ammo,(713,2))
    elif shots==5:
        screen.blit(ammo,(788,2))
        screen.blit(ammo,(773,2))
        screen.blit(ammo,(758,2))
        screen.blit(ammo,(743,2))
        screen.blit(ammo,(728,2))
    elif shots==4:
        screen.blit(ammo,(788,2))
        screen.blit(ammo,(773,2))
        screen.blit(ammo,(758,2))
        screen.blit(ammo,(743,2))
    elif shots==3:
        screen.blit(ammo,(788,2))
        screen.blit(ammo,(773,2))
        screen.blit(ammo,(758,2))
    elif shots==2:
        screen.blit(ammo,(788,2))
        screen.blit(ammo,(773,2))
    elif shots==1:
        screen.blit(ammo,(788,2))
    elif shots==0:
        screen.blit(reloading,(695,2))
    
    pygame.draw.rect(screen,(200,0,0),Rect((63,1),(you.urlives*10,15)))

    time.sleep(0.005)
    pygame.display.update()
