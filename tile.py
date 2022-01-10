import pygame

TILE_EMPTY = 0
TILE_COMMERCIAL = 1
TILE_POLICE_DEPARTMENT = 2
TiLE_HOSPITAL = 3
TILE_STREET = 4
TILE_POWER_PLANT = 5

class Tile(pygame.sprite.Sprite):
    def __init__(self, image, x, y, width, height, type, cant_sprites=1):
        pygame.sprite.Sprite.__init__(self)
        self.tile_type = type
        self.images = []
        self.index = 0
        self.current_sprite_time = 0


        for cant_sprites in range(0, cant_sprites):
            image_name = image + "_" + str(cant_sprites+1) + ".png"
            self.images.append(pygame.image.load(image_name))
            self.rect = self.images[self.index].get_rect()
            self.rect = pygame.Rect((x, y), (width, height))
            self.image = pygame.image.load(image_name)

    def update(self, surface, delta):
        if self.current_sprite_time > 0.3:
            self.index += 1
            self.current_sprite_time = 0
        else:
            self.current_sprite_time += delta


        if self.index >= len(self.images):
            self.index = 0

        self.image = self.images[self.index]
        surface.blit(self.image, (self.rect.x, self.rect.y))

    def draw(self, surface):
        surface.blit(self.image, (self.rect.x, self.rect.y))
