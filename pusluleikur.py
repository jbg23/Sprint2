import sys
import random
import pygame

myndaskra = "mikkinyr.jpg"
myndastaerd = (480, 360)
puslbreidd = 96
puslhaed = 72
dalkar = 5
radir = 5

#Tómt, svart púsl í neðra hægra horni
tomur = (dalkar-1, radir-1) #kemur þá í (5,1)
svartur = (0, 0, 0)

#Rammi á hvert púsl
larettur_rammi = pygame.Surface((puslbreidd, 1))
lodrettur_rammi = pygame.Surface((1, puslhaed))

#Setja myndaskrá inn í mynd og skipta í púsl
mynd = pygame.image.load(myndaskra)
pusluspil = {}
for d in range(0, dalkar):
    for r in range(0, radir):
        pusl = mynd.subsurface(d*puslbreidd, r*puslhaed, puslbreidd, puslhaed) #Ath, vitum ekki hvað seinni tveir gera
        pusluspil[(d,r)] = pusl
        if (d,r) != tomur:
            pusl.blit(larettur_rammi, (1, 1))
            pusl.blit(larettur_rammi, (0, radir-1))
            pusl.blit(lodrettur_rammi, (1, 1))
            pusl.blit(lodrettur_rammi, (dalkar-1,0))
pusluspil[tomur].fill(svartur)

#Hvaða púsl er hvar
stada = {(dal, rad): (dal, rad)
    for dal in range(dalkar)
        for rad in range(radir)}

#Hvar er tómi ?
(tomurD, tomurR)= tomur

#Byrjum leikinn og birtum upphaflega mynd
pygame.init()
display = pygame.display.set_mode(myndastaerd)
pygame.display.set_caption("Hreyfa púsl")
display.blit(mynd, (0, 0))
pygame.display.flip()

#Skipta á tóma púslinu og púsli (d,r)
def skipti (d,r):
    global tomurD
    global tomurR
    display.blit(pusl[stada[(d,r)]], (tomurD*puslbreidd, tomurR*puslhaed))
    display.blit(pusl[tomur], (d*puslbreidd, r*puslhaed))
    stada[(tomurD, tomurR)]=stada[(d,r)]
    stada[(d,r)] = tomur
    (tomurD, tomurR) = (d,r)
    pygame.display.flip()
