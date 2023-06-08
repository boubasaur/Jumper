import pygame
from random import randint, choice

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, type):
        super().__init__()

        if type == 'peanut':
            peanut_1 = pygame.image.load('graphics/Peanut.png').convert_alpha()
            peanut_1 = pygame.transform.scale(peanut_1, (30, 30))
            peanut_2 = pygame.image.load('graphics/Peanut2.png').convert_alpha()
            peanut_2 = pygame.transform.scale(peanut_2, (30, 30))
            self.frames = [peanut_1, peanut_2]
            y_pos = 250
        else:
            book_1 = pygame.image.load('graphics/Book.png').convert_alpha()
            book_2 = pygame.image.load('graphics/Book2.png').convert_alpha()
            book_1 = pygame.transform.scale(book_1, (25, 30))
            book_2 = pygame.transform.scale(book_2, (25, 30))
            self.frames = [book_1, book_2]
            y_pos = 350

        self.animation_index = 0
        self.image = self.frames[self.animation_index]
        self.rect = self.image.get_rect(midbottom = (randint(900,1100), y_pos))

    def animation_state(self):
        self.animation_index += 0.1
        if self.animation_index >= len(self.frames):
            self.animation_index = 0
        self.image = self.frames[int(self.animation_index)]

    def update(self):
        self.animation_state()
        self.rect.x -= 6
        self.destroy()

    def destroy(self):
        if self.rect.x <= -100:
            self.kill()