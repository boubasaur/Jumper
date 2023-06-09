import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        player1 = pygame.image.load('graphics/player/1.png').convert_alpha()
        player1 = pygame.transform.scale(player1, (100, 100))
        player2 = pygame.image.load('graphics/player/2.png').convert_alpha()
        player2 = pygame.transform.scale(player2, (100, 100))
        player3 = pygame.image.load('graphics/player/3.png').convert_alpha()
        player3 = pygame.transform.scale(player3, (100, 100))
        player4 = pygame.image.load('graphics/player/4.png').convert_alpha()
        player4 = pygame.transform.scale(player4, (100, 100))
        self.player_walk = [player1, player2, player3, player4]
        self.player_index = 0
        self.player_jump = player4

        self.image = self.player_walk[self.player_index]
        self.rect = self.image.get_rect(midbottom=(50, 350))
        self.rect = self.rect.inflate(-30, 0)
        self.gravity = 0

    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.rect.bottom >= 350:
            self.gravity = -18

    def apply_gravity(self):
        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.bottom >= 350:
            self.rect.bottom = 350

    def animation_state(self):
        if self.rect.bottom < 350:
            self.image = self.player_jump
        else:
            self.player_index += 0.1
            if self.player_index >= len(self.player_walk):
                self.player_index = 0
            self.image = self.player_walk[int(self.player_index)]

    def update(self):
        self.player_input()
        self.apply_gravity()
        self.animation_state()
