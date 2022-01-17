from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *
import sys
from tiles import *
from toolbar import Window
from definitions import *

################################# LOAD UP A BASIC WINDOW AND CLOCK #################################

pygame.init()
DISPLAY_W, DISPLAY_H = 1170, 1170
DISPLAY_W, DISPLAY_H = 800, 600
canvas = pygame.Surface((DISPLAY_W, DISPLAY_H))
window = pygame.display.set_mode(((DISPLAY_W, DISPLAY_H)))
running = True
clock = pygame.time.Clock()

################################# LOAD PLAYER AND SPRITESHEET###################################

player_rect = (0, 0, 100, 100)
offset_x = 0
offset_y = 0
getTicksLastFrame = 0

#################################### LOAD THE LEVEL #######################################
map = TileMap('./art/level_0.csv')

app = QApplication(sys.argv)
toolbar = Window()
toolbar.show()

#pragma mark ~ Helper function

def convert_position_to_cell(pos):
    cell_x = pos[0] // TILE_SIZE
    cell_y = pos[1] // TILE_SIZE
    print("_x: ",cell_x,"_y:",cell_y)
    pp = (cell_x) + CANT_COLS * cell_y
    print("pos:",pp)
    return (cell_x, cell_y)


################################# GAME LOOP ##########################
while running:
    clock.tick(60)
    ################################# CHECK PLAYER INPUT #################################
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            cell = convert_position_to_cell(pos)
            map.add(cell, toolbar.selected_option)
            map.load_map()

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                offset_x -= 1
            elif event.key == pygame.K_RIGHT:
                offset_x += 1
            elif event.key == pygame.K_UP:
                offset_y -= 1
            elif event.key == pygame.K_DOWN:
                offset_y += 1

            # map = TileMap('./art/level_0.csv', offset_x, offset_y)

    ################################# UPDATE/ Animate SPRITE #################################
    t = pygame.time.get_ticks()
    # deltaTime in seconds.
    deltaTime = (t - getTicksLastFrame) / 1000.0
    getTicksLastFrame = t

    map.update(deltaTime)

    ################################# UPDATE WINDOW AND DISPLAY #################################
    map.draw_map(canvas)
    window.blit(canvas, (0, 0))
    pygame.display.update()