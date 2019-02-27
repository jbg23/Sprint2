import sys
import random
import pygame

myndaskra = "minamikki.jpg"
myndastaerd = (200, 160)
puslbreidd = 40
puslhaed = 40
dalkar = 5
radir = 4

# Tómt púsl í neðra hægra horni
tomur = (dalkar-1, radir-1)

svartur = (0, 0, 0)

# horizontal and vertical borders for tiles
larettur_rammi = pygame.Surface((puslbreidd, 1))
larettur_rammi.fill(svartur)
lodrettur_rammi = pygame.Surface((1, puslhaed))
lodrettur_rammi.fill(svartur)

# load the image and divide up in tiles
# putting borders on each tile also adds them to the full image
mynd = pygame.image.load(myndaskra)
pusl = {}
for c in range(dalkar) :
    for r in range(radir) :
        pusl = mynd.subsurface (
            c*puslbreidd, r*puslhaed,
            puslbreidd, puslhaed)
        pusluspil [(c, r)] = pusl
        if (c, r) != tomur:
            tile.blit(larettur_rammi, (0, 0))
            tile.blit(larettur_rammi, (0, puslhaed-1))
            tile.blit(lodrettur_rammi, (0, 0))
            tile.blit(lodrettur_rammi, (puslbreidd-1, 0))
            # make the corners a bit rounded
            tile.set_at((1, 1), svartur)
            tile.set_at((1, puslhaed-2), svartur)
            tile.set_at((puslbreidd-2, 1), svartur)
            tile.set_at((puslbreidd-2, puslhaed-2), svartur)
pusluspil[tomur].fill(svartur)

# keep track of which tile is in which position
stadan = {(col, row): (col, row)
            for col in range(dalkar) for row in range(radir)}

# keep track of the position of the empty tyle
(emptyc, emptyr) = tomur

# start game and display the completed puzzle
pygame.init()
display = pygame.display.set_mode(myndastaerd)
pygame.display.set_caption("shift-puzzle")
display.blit (image, (0, 0))
pygame.display.flip()

# swap a tile (c, r) with the neighbouring (emptyc, emptyr) tile
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

# shuffle the puzzle by making some random shift moves
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

# process mouse clicks
at_start = True
showing_solution = False
while True:
    event = pygame.event.wait()
    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
    elif event.type == pygame.MOUSEBUTTONDOWN :
        if at_start:
            # shuffle after the first mouse click
            shuffle()
            at_start = False
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
            display.blit(image, (0, 0))
            pygame.display.flip()
            showing_solution = True
    elif showing_solution and (event.type == pygame.MOUSEBUTTONUP):
        # stop showing the solution
        display.blit (saved_image, (0, 0))
        pygame.display.flip()
        showing_solution = False
