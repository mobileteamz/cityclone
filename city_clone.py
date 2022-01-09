import pygame, sys
from pygame.locals import *

FPS = 15
COLUMNS =   100
ROWS =      100

WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
CELLSIZE = 20

TILE_WIDTH = 10
TILE_HEIGHT = 10

DARKGRAY  = (40, 40, 40)
HINTCOLOR  = (40, 40, 40)
WHITE = (0, 250, 0)

def main():
    global FPSCLOCK, DISPLAYSURF

    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption('CityClone')

    while True:
        runGame()


def runGame():
    size = (700, 500)
    screen = pygame.display.set_mode(size)
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()

        drawGrid()
        all_sprites_list = pygame.sprite.Group()
        # all_sprites_list.add(rec)
        # screen.fill(WHITE)
        all_sprites_list.draw(screen)

        pygame.display.update()
        FPSCLOCK.tick(FPS)

def drawGrid():
    centerx = 0
    centery = 0
    image = pygame.image.load("art/empty_tile.png").convert()
    image = pygame.transform.scale(image, (TILE_WIDTH, TILE_HEIGHT))
    for x in range(0, WINDOW_WIDTH, CELLSIZE):
        pygame.draw.line(DISPLAYSURF, DARKGRAY, (x, 0), (x, WINDOW_HEIGHT))
        # BGIMAGE = pygame.image.load('empty_tile.png')
        centerx += x*5.0
        centery += 0
        pygame.draw.rect(DISPLAYSURF, HINTCOLOR, (centerx - 4,centery - 4, 80, 80))
        # pygame.draw.t
        image.blit(pygame.image.load("art/empty_tile.png").convert(), (x, 0))


def terminate():
    pygame.quit()
    sys.exit()


main()