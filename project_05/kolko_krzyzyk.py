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
ObrazekO = pg.image.load('O.png')

#zmiana wymiarow obrazka

PlanszaStartowa = pg.transform.scale(PlanszaStartowa, (Szerokosc, Wysokosc+200))
ObrazekX = pg.transform.scale(ObrazekX, (80,80))
ObrazekO = pg.transform.scale(ObrazekO, (80,80))



def RysujPlansze():
    Ekran.blit(PlanszaStartowa, (0,0))
    pg.display.update()
    time.sleep(3)
    Ekran.fill(Bialy)

    pg.draw.line(Ekran, Czarny, (Szerokosc/3,0), (Szerokosc/3, Wysokosc),7)
    pg.draw.line(Ekran, Czarny, (Szerokosc / 3*2, 0), (Szerokosc / 3*2, Wysokosc), 7)

    pg.draw.line(Ekran, Czarny,(0, Wysokosc/3), (Szerokosc, Wysokosc/3),7)
    pg.draw.line(Ekran, Czarny,(0, Wysokosc / 3*2), (Szerokosc, Wysokosc / 3*2), 7)


    pg.display.update()

def RysujDodatkoweInformacje():

    global Remis

    if KtoWygral is None:

        TrescWiadomosci = 'Twoja tura' + CzyjaTura.upper()
    else:
        TrescWiadomosci = KtoWygral.upper() + 'wygrałeś'




RysujPlansze()


