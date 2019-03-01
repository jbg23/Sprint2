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
larettur_rammi.fill(svartur) #vitum ekki hvers vegna virkar ekki
lodrettur_rammi = pygame.Surface((1, puslhaed))
lodrettur_rammi.fill(svartur)

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
pygame.display.set_caption("Púslaðu Mikka!")
display.blit(mynd, (0, 0))
pygame.display.flip()
"""while True:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
    pygame.display.update()"""

#Skipta á tóma púslinu og púsli (d,r)
def skipti (d,r):
    global tomurD
    global tomurR
    print('test1')
    display.blit(pusl[stada[(d,r)]], tomurD*puslbreidd, tomurR*puslhaed)
    print('test2')
    #display.blit(pusl[tomur], (d*puslbreidd, r*puslhaed))
    stada[(tomurD, tomurR)]=stada[(d,r)]
    stada[(d,r)] = tomur
    (tomurD, tomurR) = (d,r)
    pygame.display.flip()

#Rugla púslbitum
def rugla():
    global tomurD
    global tomurR
    sidastaR = 0
    for i in range(75): #ATH 75?
        pygame.time.delay(50)
        while True:
            #Veljum random átt til að færa púslin í.
            r=random.randint(1,4)
            if(sidastaR + r == 5):
                continue
            if r == 1 and (tomurD>0):
                skipti(tomurD-1, tomurR) #vinstri
            elif r == 4 and (tomurD<0):
                skipti(tomurD+1, tomurR) #hægri
            elif r == 2 and (tomurR > 0):
                skipti(tomurD, tomurR-1) #upp
            elif r == 3 and (tomurR < radir-1):
                skipti(tomurD, tomurR+1) #niður
            else:
                sidastaR = r
                continue
            break #Búið að rugla púslunum

def main():
#Hreyfa púsl með mús
    byrjun = True
    synilausn = False
    while True:
        event = pygame.event.wait()
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if byrjun: #Rugla eftir að ýtt er á mús í fyrsta sinn
                rugla()
                byrjun = False
            elif event.dict['Hnappur'] == 1: #Ef ýtt á músina (vinstri), á púsl við hliðina á tómu púsli þá færist púslið.
                mouse_pos = pygame.mouse.get_pos()
                d = mouse_pos[0] / puslbreidd
                r = mouse_pos[1] / puslhaed
                if((abs(d-tomurD)==1 and r==tomurR)or (abs(r-tomurR) == 1 and d == tomurD)):
                    skipti(d, r)
            elif event.dict["Hnappur"] == 3:
                #Hægri klikk, sýnir lausn myndar
                vistud_mynd=display.copy()
                display.blit(mynd, (0, 0))
                pygame.display.flip()
                synilausn = True
        elif synilausn and (event.type == pygame.MOUSEBUTTONUP):
            #Hætta að sýna lausnina
            display.blit(vistud_mynd, (0, 0))
            pygame.display.flip()
            synilausn = False

if __name__ == "__main__":
    main()
