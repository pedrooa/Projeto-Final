import pygame as pg
import math
from settings import *
vetor = pg.math.Vector2


class Trave(pg.sprite.Sprite):
    def __init__(self,imagem,x,y):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.transform.scale(imagem, (TRAVE_W,TRAVE_H))
        self.image.set_colorkey(RED)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Bola(pg.sprite.Sprite):
    def __init__(self,x,y,raio,imagem):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.transform.scale(imagem, (BOLA_W,BOLA_H))
        self.image.set_colorkey(RED)
        self.rect = self.image.get_rect()
        self.radius = int(raio)
        self.rect.centerx = x
        self.rect.centery = y
        self.pos = vetor(x,self.rect.centery)
        self.vel = vetor(0,0)
        self.acc = vetor(0,0)
        self.mask = pg.mask.from_surface(self.image)

    def update(self):
        self.acc = vetor(0,0.4)
        self.quicar()
        self.vel*= arrasto
        self.vel += self.acc
        self.pos += self.vel

        self.rect.center = self.pos

    #Bola quica na tela
    def quicar(self):
        if self.pos.x > WIDTH - self.radius:
            self.pos.x = 2*(WIDTH - self.radius) - self.pos.x
            self.vel.x = -self.vel.x
            self.vel*= elasticidade

        elif self.pos.x < self.radius:
            self.pos.x = 2*self.radius - self.pos.x
            self.vel.x = -self.vel.x
            self.vel*=elasticidade

        if self.pos.y > HEIGHT-30 - self.radius:
            self.pos.y = 2*(HEIGHT-30 - self.radius) - self.pos.y
            self.vel.y = -self.vel.y
            self.vel*=elasticidade

        elif self.pos.y < self.radius:
            self.pos.y = 2*self.radius - self.pos.y
            self.vel.y = -self.vel.y
            self.vel*=elasticidade

    def collide(self,other):
        dx = self.rect.x - other.rect.x
        dy = self.rect.y - other.rect.y

        dist = math.hypot(dx,dy)
        soma_raios = self.radius + other.radius
        if dist < soma_raios:
            force = 3*(soma_raios - dist)
            v = vetor(other.rect.x-self.rect.x,other.rect.y-self.rect.y)
            versor = v/dist
            FEL = force*versor
            self.vel -= 0.12*FEL

class Jogador(pg.sprite.Sprite):
    def __init__(self,game,x,imagem,teclas):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.transform.scale(imagem, (PLAYER_W, PLAYER_H))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.radius = PLAYER_RAIO
       #pg.draw.circle(self.image, RED, self.rect.center, self.radius)
        self.rect.center = (x, HEIGHT - PLAYER_H)
        self.pos = vetor(x, self.rect.centery)
        self.vel = vetor(0, 0)
        self.acc = vetor(0, 0)
        self.teclas = teclas
        self.mask = pg.mask.from_surface(self.image)
        self.game = game
        #self.group = game.all_sprites

    def jump(self):
        self.rect.y += 1
        hits = pg.sprite.spritecollide(self, self.game.plataformas, False)
        self.rect.y -= 1
        if hits:
            self.vel.y = -12

    def update(self):
        self.acc = vetor(0, gravidade)
        keystate = pg.key.get_pressed()
        if self.teclas == 0:
            if keystate[pg.K_a]:
                self.acc.x = -aceleração_maxima
            if keystate[pg.K_d]:
                self.acc.x = aceleração_maxima
        elif self.teclas ==1:

            if keystate[pg.K_LEFT]:
                self.acc.x = -aceleração_maxima
            if keystate[pg.K_RIGHT]:
                self.acc.x = aceleração_maxima

       #aplicando atrito
        self.acc.x += self.vel.x *  atrito
        #equacao de movimento
        self.vel += self.acc
        self.pos += self.vel + 0.5 *self.acc

        #bater na parede
        if self.pos.x + 25 > WIDTH:
            self.pos.x = WIDTH - 25
        if self.pos.x - 25 < 0:
            self.pos.x =  25
        self.rect.midbottom = self.pos

    def dash(self):
        self.vel.x = self.vel.x * 4

class Campo(pg.sprite.Sprite):
    def __init__(self, x , y, w, h):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((w,h))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
