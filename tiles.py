import pygame, csv, os
from tile import Tile

CANT_COLS = 100
TILE_EMPTY = 0
TILE_COMMERCIAL = 1
TILE_POLICE_DEPARTMENT = 2
TiLE_HOSPITAL = 3
TILE_STREET = 4
TILE_POWER_PLANT = 5

tiles = []

class TileMap():
    def __init__(self, filename, offset_x=0, offset_y=0):
        self.map_w = 100
        self.map_h = 100
        self.tile_size = 30
        self.start_x, self.start_y = 0, 0
        self.tiles = self.load_tiles(filename, offset_x, offset_y)
        self.map_surface = pygame.Surface((1000, 1000))
        self.load_map()

    def get_type_number_frames(self, type):
        if type == TILE_POWER_PLANT:
            return 5
        else:
            return 1

    def get_associated_png(self, type):
        if type == TILE_STREET:
            return 'road_straight'
        elif type == TILE_POLICE_DEPARTMENT:
            return 'police_department'
        elif type == TILE_COMMERCIAL:
            return 'commercial'
        elif type == TILE_POWER_PLANT:
            return 'power_plant'
        else:
            assert(False, "Invalid file type")

    def add(self, cell, type):
        x = cell[0]
        y = cell[1]
        pos = x * CANT_COLS + y
        self.tiles[pos] = Tile(self.get_associated_png(type), x * self.tile_size, y * self.tile_size, 30, 30,
                               TILE_STREET, self.get_type_number_frames(type))

        if type == TILE_POLICE_DEPARTMENT:
            pos = (x+1) * CANT_COLS + y
            tiles.pop(pos)
            self.tiles[pos]
            pos = x * CANT_COLS + (y+1)
            tiles.pop(pos)
            pos = (x+1) * CANT_COLS + (y+1)
            tiles.pop(pos)

        self.load_map()

    def update(self, delta):
        for tile in tiles:
            tile.update(self.map_surface, delta)


    def draw_map(self, surface):
        surface.blit(self.map_surface, (0, 0))

    def load_map(self):
        for tile in self.tiles:
            tile.draw(self.map_surface)

    def read_csv(selfself, filename):
        map = []
        with open(os.path.join(filename)) as data:
            data = csv.reader(data, delimiter=',')

            for row in data:
                map.append(list(row))

        return map

    def load_tiles(self, filename, offset_x=0, offset_y=0):
        map = self.read_csv(filename)
        x, y = offset_x, offset_y

        for row in map:
            x = 0
            for tile in row:
                if tile == '-1':
                    self.start_x, self.start_y = x * self.tile_size, y * self.tile_size
                elif int(tile) == TILE_EMPTY:
                    tiles.append(Tile('empty_tile', x * self.tile_size, y * self.tile_size, 30, 30, TILE_EMPTY))
                elif int(tile) == TILE_COMMERCIAL:
                    tiles.append(Tile('commercial', x * self.tile_size, y * self.tile_size, 60, 60, TILE_COMMERCIAL))
                elif int(tile) == TILE_POLICE_DEPARTMENT:
                    tiles.append(Tile('police_department', x * self.tile_size, y * self.tile_size, 60, 60, TILE_POLICE_DEPARTMENT ))
                elif int(tile) == TILE_STREET:
                    tiles.append(Tile('road_straight', x * self.tile_size, y * self.tile_size, 30, 30, TILE_STREET))
                elif int(tile) == TILE_POWER_PLANT:
                    tiles.append(Tile('power_plant', x * self.tile_size, y * self.tile_size, 150, 140, TILE_POWER_PLANT,self.get_type_number_frames(TILE_POWER_PLANT)))
                x += 1
            y += 1

        self.map_w, self.map_h = x * self.tile_size, y * self.tile_size
        self.tiles = tiles
        return tiles