import pygame, csv, os
from tile import Tile
from definitions import *

tiles = []

class TileMap():
    def __init__(self, filename, offset_x=0, offset_y=0):
        self.map_w = 100
        self.map_h = 100
        self.tile_size = TILE_SIZE
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
        elif type == TILE_STREET_CURVE:
            return 'road_curve'
        else:
            assert(False, "Invalid file type")


    def get_tile_size(self, tile_type):
        if tile_type == TILE_POWER_PLANT:
            return TILE_SIZE*4
        else:
            return TILE_SIZE

    def add(self, cell, type):
        x = cell[0]
        y = cell[1]
        pos = x + CANT_COLS * y

        self.tiles[pos] = Tile(self.get_associated_png(type),
                               x * self.tile_size,
                               y * self.tile_size,
                               self.get_tile_size(type),
                               self.get_tile_size(type),
                               type,
                               pos,
                               self.get_type_number_frames(type))

        if type == TILE_POLICE_DEPARTMENT:
            self.set_transparent_area(pos, 2, 2, x, y)
        elif type == TILE_POWER_PLANT:
            self.set_transparent_area(pos, 4, 5, x, y)

    def set_transparent_area(self, pos, ii, jj, x, y):
        for i in range(0, ii):
            for j in range(0, jj):
                new_pos = (x + j) + CANT_COLS * (y + i)
                if new_pos != pos:
                    self.tiles[new_pos] = Tile('transparent_tile', x * self.tile_size, y * self.tile_size, TILE_SIZE,
                                               TILE_SIZE, TILE_TRANSPARENT, pos,
                                               self.get_type_number_frames(TILE_TRANSPARENT))

    def update(self, delta):
        pos = 0
        for tile in tiles:
            tile.update(self.map_surface, delta)
            tile = self.check_tile_road(pos, tile, tiles)
            pos += 1

    def check_tile_road(self, pos, tile, tiles):
        assert(len(tiles) < 9611, "Tiles should never exceed 9610")

        if tile.tile_type != TILE_STREET and tile.tile_type != TILE_STREET_CURVE:
            return tile

        if (pos-1) < 0 and (pos+1) > len(tiles):
            return tile

        if self.is_triple_case(pos):
            tile.reset()
            tile.tile_type = TILE_STREET_TRIPLE_CURVE
            tile.set_new_image('road_triple', 1)
            tile.set_rotation(self.get_triple_angle(pos))
            return tile

        if self.is_curve_case(pos):
            tile.tile_type = TILE_STREET_CURVE
            tile.set_new_image('road_curve', 1)
            ang = self.get_curve_angle(pos)
            tile.set_rotation(ang)
            return tile


        prev_tile = tiles[pos - CANT_COLS]
        pos_tile = tiles[pos + CANT_COLS]

        if prev_tile.tile_type == TILE_STREET or pos_tile.tile_type == TILE_STREET:
            tile.set_rotation(ROTATION_UP_DOWN)
            return tile

        return tile

    def is_curve_case(self, pos):
        rv = False

        if tiles[pos - 1].tile_type == TILE_STREET and tiles[pos + CANT_COLS].tile_type == TILE_STREET:
            rv = True

        if tiles[pos + 1].tile_type == TILE_STREET and tiles[pos + CANT_COLS].tile_type == TILE_STREET:
            rv = True

        if tiles[pos - 1].tile_type == TILE_STREET and tiles[pos - CANT_COLS].tile_type == TILE_STREET:
            rv = True

        if tiles[pos + 1].tile_type == TILE_STREET and tiles[pos - CANT_COLS].tile_type == TILE_STREET:
            rv = True

        return rv

    def is_triple_case(self, pos):
        rv = False

        if tiles[pos - 1].tile_type == TILE_STREET and \
            tiles[pos + 1].tile_type == TILE_STREET and \
            tiles[pos - CANT_COLS].tile_type == TILE_STREET:
            rv = True

        if tiles[pos - 1].tile_type == TILE_STREET and \
                tiles[pos + 1].tile_type == TILE_STREET and \
                tiles[pos + CANT_COLS].tile_type == TILE_STREET:
            rv = True

        return rv



    def get_curve_angle(self, pos):
        rv = 0
        # caso a:
        if tiles[pos - 1].tile_type == TILE_STREET and tiles[pos + CANT_COLS].tile_type == TILE_STREET:
            rv = 0

        # caso b:
        if tiles[pos + 1].tile_type == TILE_STREET and tiles[pos + CANT_COLS].tile_type == TILE_STREET:
            rv = 90

        # caso c:
        if tiles[pos - 1].tile_type == TILE_STREET and tiles[pos - CANT_COLS].tile_type == TILE_STREET:
            rv = 270

        # caso d:
        if tiles[pos + 1].tile_type == TILE_STREET and tiles[pos - CANT_COLS].tile_type == TILE_STREET:
            rv = 180

        return rv

    def get_triple_angle(self, pos):
        if tiles[pos - CANT_COLS].tile_type == TILE_STREET:
            rv = 180
        else:
            rv = 0

        return rv

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
        pos = 0

        for row in map:
            x = 0
            for tile in row:
                if tile == '-1':
                    self.start_x, self.start_y = x * self.tile_size, y * self.tile_size
                elif int(tile) == TILE_EMPTY:
                    tiles.append(Tile('empty_tile', x * self.tile_size, y * self.tile_size, TILE_SIZE, TILE_SIZE, TILE_EMPTY, pos))
                elif int(tile) == TILE_COMMERCIAL:
                    tiles.append(Tile('commercial', x * self.tile_size, y * self.tile_size, 60, 60, TILE_COMMERCIAL, pos))
                elif int(tile) == TILE_POLICE_DEPARTMENT:
                    tiles.append(Tile('police_department', x * self.tile_size, y * self.tile_size, 60, 60, TILE_POLICE_DEPARTMENT, pos))
                elif int(tile) == TILE_STREET:
                    tiles.append(Tile('road_straight', x * self.tile_size, y * self.tile_size, TILE_SIZE, TILE_SIZE, TILE_STREET, pos))
                elif int(tile) == TILE_POWER_PLANT:
                    tiles.append(Tile('power_plant', x * self.tile_size, y * self.tile_size, 4*TILE_SIZE, TILE_SIZE, 4*TILE_POWER_PLANT, pos, self.get_type_number_frames(TILE_POWER_PLANT)))
                elif int(tile) == TILE_STREET_CURVE:
                    tiles.append(Tile('road_curve', x * self.tile_size, y * self.tile_size, TILE_SIZE, TILE_SIZE, TILE_STREET_CURVE,pos, self.get_type_number_frames(TILE_STREET_CURVE)))
                elif int(tile) < 0:
                    tiles.append(Tile('transparent_tile', x * self.tile_size, y * self.tile_size, TILE_SIZE, TILE_SIZE, TILE_TRANSPARENT,pos, self.get_type_number_frames(TILE_TRANSPARENT)))
                pos += 1
                x += 1
            y += 1

        self.map_w, self.map_h = x * self.tile_size, y * self.tile_size
        return tiles