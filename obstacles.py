import pygame
from random import randint, choice


class Obstacle(pygame.sprite.Sprite):
    def __init__(self, sprite1, sprite2):
        super().__init__()

        self.frames = [sprite1, sprite2]
        y_pos = choice([250, 350])

        self.animation_index = 0
        self.image = self.frames[self.animation_index]
        self.rect = self.image.get_rect(midbottom=(randint(900, 1100), y_pos))

    def animation_state(self):
        self.animation_index += 0.1
        if self.animation_index >= len(self.frames):
            self.animation_index = 0
        self.image = self.frames[int(self.animation_index)]

    def update(self):
        self.animation_state()
        self.rect.x -= 10
        self.destroy()

    def destroy(self):
        if self.rect.x <= -100:
            self.kill()
