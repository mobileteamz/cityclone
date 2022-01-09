import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

class Rec(pygame.sprite.Sprite):

    def __init__(self, x, y, w, height):

        super().__init__()

        self.b = 0
        self.a = 0

        self.image = pygame.image.load("art/empty_tile.png").convert()
        self.image = pygame.Surface([w, height])

        self.rock = pygame.image.load("art/tile_rock.png").convert()
        self.rock = pygame.Surface([w, height])

        self.police_department = pygame.image.load("police_department.png").convert()
        self.police_department = pygame.Surface([w, height])

        while self.b < w:
            while self.a < height:
                val = int(self.a) % 27
                if val == 0:
                    # self.image.blit(pygame.image.load("art/empty_tile.png").convert(), (self.b, self.a))
                    self.image.blit(pygame.image.load("art/tile_rock.png").convert(), (self.b, self.a))

                else:
                    # print("{self.a},{self.b}")
                    self.police_department.blit(pygame.image.load("police_department.png").convert(),
                                                (self.b, self.a))

                self.a += 30

            self.a = 0
            self.b += 30

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

pygame.init()

size = (1700, 1000)

screen = pygame.display.set_mode(size)

pygame.display.set_caption("My Game")

all_sprites_list = pygame.sprite.Group()

rec = Rec(10, 10, 1700, 1000)
all_sprites_list.add(rec)

done = False

clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    screen.fill(WHITE)
    all_sprites_list.draw(screen)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()