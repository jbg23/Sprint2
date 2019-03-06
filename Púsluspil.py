import sys
import random
import pygame

myndaskra = "minamikki.jpg"
myndastaerd = (640, 640)
puslbreidd = 128
puslhaed = 128
dalkar = 5
radir = 5

# Tómt púsl í neðra hægra horni sem er svart
tomur = (dalkar, radir)
svartur = (0, 0, 0)

# Set ramma á hvert púsl
larettur_rammi = pygame.Surface((puslbreidd, 1))
larettur_rammi.fill(svartur)
lodrettur_rammi = pygame.Surface((1, puslhaed))
lodrettur_rammi.fill(svartur)

# Set myndaskrána inn í breytuna mynd
mynd = pygame.image.load(myndaskra)
pusluspil = {}
for c in range(4) :
    for r in range(4) :
        pusl = mynd.subsurface (
            c*puslbreidd, r*puslhaed,
            puslbreidd, puslhaed)
        pusluspil[(c, r)] = pusl
        if (c, r) != tomur:
            pusl.blit(larettur_rammi, (0, 0))
            pusl.blit(larettur_rammi, (0, puslhaed-1))
            pusl.blit(lodrettur_rammi, (0, 0))
            pusl.blit(lodrettur_rammi, (puslbreidd-1, 0))
            #rúnuð horn
            pusl.set_at((1, 1), svartur)
            pusl.set_at((1, puslhaed-2), svartur)
            pusl.set_at((puslbreidd-2, 1), svartur)
            pusl.set_at((puslbreidd-2, puslhaed-2), svartur)
pusluspil[tomur].fill(svartur)

# hvaða púsl er í hvaða stöðu
stadan = {(col, row): (col, row)
            for col in range(dalkar) for row in range(radir)}

# hvar er tóma púslið
(emptyc, emptyr) = tomur

# hefja leik
pygame.init()
display = pygame.display.set_mode(myndastaerd)
pygame.display.set_caption("shift-puzzle")
display.blit (mynd, (0, 0))
pygame.display.flip()

# víxla púslum (c, r) við púslið við hliðina
def shift (c, r) :
    global emptyc, emptyr
    display.blit(
        pusluspil[stadan[(c, r)]],
        (emptyc*puslbreidd, emptyr*puslhaed))
    display.blit(
        pusluspil[tomur],
        (c*puslbreidd, r*puslhaed))
    stadan[(emptyc, emptyr)] = stadan[(c, r)]
    stadan[(c, r)] = tomur
    (emptyc, emptyr) = (c, r)
    pygame.display.flip()

# hræri í púsluspilinu með random skiptingum
def shuffle() :
    global emptyc, emptyr
    # keep track of last shuffling direction to avoid "undo" shuffle moves
    last_r = 0
    for i in range(75):
        # slow down shuffling for visual effect
        pygame.time.delay(50)
        while True:
            # pick a random direction and make a shuffling move
            # if that is possible in that direction
            r = random.randint(1, 4)
            if (last_r + r == 5):
                # don't undo the last shuffling move
                continue
            if r == 1 and (emptyc > 0):
                shift(emptyc - 1, emptyr) # shift left
            elif r == 4 and (emptyc < dalkar - 1):
                shift(emptyc + 1, emptyr) # shift right
            elif r == 2 and (emptyr > 0):
                shift(emptyc, emptyr - 1) # shift up
            elif r == 3 and (emptyr < radir - 1):
                shift(emptyc, emptyr + 1) # shift down
            else:
                # the random shuffle move didn't fit in that direction
                continue
            last_r=r
            break # a shuffling move was made

# músaklikk
byrjunarstada = True
lausn = False
while True:
    event = pygame.event.wait()
    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
    elif event.type == pygame.MOUSEBUTTONDOWN :
        if byrjunarstada:
            # shuffle after the first mouse click
            shuffle()
            byrjunarstada = False
        elif event.dict['button'] == 1:
            # mouse left button: move if next to the empty tile
            mouse_pos = pygame.mouse.get_pos()
            c = mouse_pos[0] / puslbreidd
            r = mouse_pos[1] / puslhaed
            if (    (abs(c-emptyc) == 1 and r == emptyr) or
                    (abs(r-emptyr) == 1 and c == emptyc)):
                shift (c, r)
        elif event.dict['button'] == 3:
            # mouse right button: show solution image
            saved_image = display.copy()
            display.blit(mynd, (0, 0))
            pygame.display.flip()
            lausn = True
    elif lausn and (event.type == pygame.MOUSEBUTTONUP):
        # stop showing the solution
        display.blit (saved_image, (0, 0))
        pygame.display.flip()
        lausn = False
