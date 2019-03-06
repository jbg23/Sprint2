import sys
import random
import pygame

<<<<<<< HEAD
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
=======
IMAGE_FILE = "mikkipusl.jpg"
IMAGE_SIZE = (750, 500)
TILE_WIDTH = 187.5
TILE_HEIGHT = 166.67
COLUMNS = 4
ROWS = 3

# bottom right corner contains no tile
EMPTY_TILE = (COLUMNS-1, ROWS-1)

BLACK = (0, 0, 0)

# horizontal and vertical borders for tiles
hor_border = pygame.Surface((TILE_WIDTH, 1))
hor_border.fill(BLACK)
ver_border = pygame.Surface((1, TILE_HEIGHT))
ver_border.fill(BLACK)

# load the image and divide up in tiles
# putting borders on each tile also adds them to the full image
image = pygame.image.load(IMAGE_FILE)
tiles = {}
for c in range(COLUMNS) :
    for r in range(ROWS) :
        tile = image.subsurface (
            c*TILE_WIDTH, r*TILE_HEIGHT,
            TILE_WIDTH, TILE_HEIGHT)
        tiles [(c, r)] = tile
        if (c, r) != EMPTY_TILE:
            tile.blit(hor_border, (0, 0))
            tile.blit(hor_border, (0, TILE_HEIGHT-1))
            tile.blit(ver_border, (0, 0))
            tile.blit(ver_border, (TILE_WIDTH-1, 0))
            # make the corners a bit rounded
            tile.set_at((1, 1), BLACK)
            tile.set_at((1, TILE_HEIGHT-2), BLACK)
            tile.set_at((TILE_WIDTH-2, 1), BLACK)
            tile.set_at((TILE_WIDTH-2, TILE_HEIGHT-2), BLACK)
tiles[EMPTY_TILE].fill(BLACK)

# keep track of which tile is in which position
state = {(col, row): (col, row)
            for col in range(COLUMNS) for row in range(ROWS)}

# keep track of the position of the empty tyle
(emptyc, emptyr) = EMPTY_TILE
>>>>>>> eecef75704e522fa3892296b6f66cff0a57f8472

# hefja leik
pygame.init()
display = pygame.display.set_mode(IMAGE_SIZE)
pygame.display.set_caption("shift-puzzle")
display.blit (mynd, (0, 0))
pygame.display.flip()

# víxla púslum (c, r) við púslið við hliðina
def shift (c, r) :
    global emptyc, emptyr
    display.blit(
        tiles[state[(c, r)]],
        (emptyc*TILE_WIDTH, emptyr*TILE_HEIGHT))
    display.blit(
        tiles[EMPTY_TILE],
        (c*TILE_WIDTH, r*TILE_HEIGHT))
    state[(emptyc, emptyr)] = state[(c, r)]
    state[(c, r)] = EMPTY_TILE
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
            elif r == 4 and (emptyc < COLUMNS - 1):
                shift(emptyc + 1, emptyr) # shift right
            elif r == 2 and (emptyr > 0):
                shift(emptyc, emptyr - 1) # shift up
            elif r == 3 and (emptyr < ROWS - 1):
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
            c = mouse_pos[0] / TILE_WIDTH
            r = mouse_pos[1] / TILE_HEIGHT
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
