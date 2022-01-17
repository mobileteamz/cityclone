import pygame
from definitions import *

class Tile(pygame.sprite.Sprite):

    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self)

    def __init__(self, image, x, y, width, height, type, pos, cant_sprites=1):
        pygame.sprite.Sprite.__init__(self)
        self.image= image
        self.x= x
        self.y= y
        self.width= width
        self.height= height
        self.can_sprites= cant_sprites
        self.pos = pos
        self.tile_type = type
        self.images = []
        self.index = 0
        self.current_sprite_time = 0
        self.rotation = ROTATION_LEFT_RIGHT
        self.load_art(image, x, y, width, height, type, cant_sprites)

    def reset(self):
        self.images = []

    def load_art(self, image, x, y, width, height, type, cant_sprites=1):
        self.images = []
        for cant_sprites in range(0, cant_sprites):
            image_url = "./art/" + image + "_" + str(cant_sprites+1) + ".png"
            try:
                self.images.append(pygame.image.load(image_url))
            except:
                print("File not really there:", image_url)

            self.rect = self.images[self.index].get_rect()
            self.rect = pygame.Rect((x, y), (width, height))
            self.image = pygame.image.load(image_url)

    def update(self, surface, delta):
        if self.current_sprite_time > 0.3:
            self.index += 1
            self.current_sprite_time = 0
        else:
            self.current_sprite_time += delta


        if self.index >= len(self.images):
            self.index = 0

        self.image = self.images[self.index]
        self.image = pygame.transform.rotate(self.image, self.rotation)
        surface.blit(self.image, (self.rect.x, self.rect.y))


    def set_rotation(self, new_rotation):
        if self.rotation != new_rotation:
            self.rotation = new_rotation
            self.image = pygame.transform.rotate(self.image, new_rotation)


    def set_new_image(self, new_image, cant_sprites):
        if self.image != new_image:
            self.load_art(new_image, self.x,  self.y,  self.width,  self.height, new_image, cant_sprites)

    def draw(self, surface):
        surface.blit(self.image, (self.rect.x, self.rect.y))
