import pygame as pg, sys, time
from pygame.locals import *

#ustawienia poczatkowe


CzyjaTura = 'x'
KtoWygral = None
Remis = False
Szerokosc = 400
Wysokosc  = 400

Bialy = (255,255,255)
Czarny = (0,0,0)
Czerwony = (255,0,0)

PunktyX = 0
PunktyO = 0

#ustawiamy plansze

Plansza = [ [None]*3, [None]*3, [None]*3]

#okno programu

pg.init()
FPS = 30

Zegar = pg.time.Clock()

Ekran = pg.display.set_mode((Szerokosc, Wysokosc+200), 0, 32)

pg.display.set_caption("Kolko i krzyzyk")

PlanszaStartowa = pg.image.load('PlanszaStartowa.png')
ObrazekX = pg.image.load('X.png')
ObrazekY = pg.image.load('O.png')
