from random import randint, choice
import pygame
from sys import exit

from player import *
from obstacles import *


def display_score():

    global score
    score_surface = game_font.render(f'Score: {score}', False, (73, 93, 130))
    score_rect = score_surface.get_rect(center=(400, 50))
    screen.blit(score_surface, score_rect)
    return score


def collision_sprite():
    global score
    if pygame.sprite.spritecollide(player_sprite.sprite, book_group, False):
        book_group.empty()
        peanut_group.empty()
        score = 0
        return False
    elif pygame.sprite.spritecollide(player_sprite.sprite, peanut_group, True):
        score += 1
        return True
    return True


pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
game_font = pygame.font.Font('font/dogicabold.ttf', 25)
game_active = False
start_time = 0
score = 0

player_sprite = pygame.sprite.GroupSingle()
player_sprite.add(Player())

book_group = pygame.sprite.Group()
peanut_group = pygame.sprite.Group()

background_surface = pygame.image.load('graphics/School.jpg').convert()
background_surface = pygame.transform.scale(background_surface, (800, 500))

book_1 = pygame.image.load('graphics/Book.png').convert_alpha()
book_2 = pygame.image.load('graphics/Book2.png').convert_alpha()
book_1 = pygame.transform.scale(book_1, (25, 30))
book_2 = pygame.transform.scale(book_2, (25, 30))
book_frames = [book_1, book_2]
book_index = 0
book_surface = book_frames[book_index]
book_rect = book_surface.get_rect(bottomleft=(800, 200))

peanut_1 = pygame.image.load('graphics/Peanut.png').convert_alpha()
peanut_1 = pygame.transform.scale(peanut_1, (30, 30))
peanut_2 = pygame.image.load('graphics/Peanut2.png').convert_alpha()
peanut_2 = pygame.transform.scale(peanut_2, (30, 30))
peanut_frames = [peanut_1, peanut_2]
peanut_index = 0
peanut_surface = peanut_frames[peanut_index]
peanut_rect = peanut_surface.get_rect(midbottom=(800, 200))

# obstacle_rect_list = []

player1 = pygame.image.load('graphics/player/1.png').convert_alpha()
player2 = pygame.image.load('graphics/player/2.png').convert_alpha()
player3 = pygame.image.load('graphics/player/3.png').convert_alpha()
player4 = pygame.image.load('graphics/player/4.png').convert_alpha()
player_walk = [player1, player2, player3, player4]
player_index = 0
player_jump = player4

player = player_walk[player_index]
player_rect = player.get_rect(midbottom=(50, 200))
player_gravity = 0

player_stand = pygame.image.load('graphics/player/stand.png').convert_alpha()
player_stand = pygame.transform.scale(player_stand, (200, 200))
player_stand_rect = player_stand.get_rect(center=(400, 200))

game_name = game_font.render('Anya Forger Loves Peanuts', False, 'Black')
game_name_rect = game_name.get_rect(center=(400, 100))

game_message = game_font.render('Press space to start', False, 'Black')
game_message_rect = game_message.get_rect(center=(400, 350))

obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1500)

book_animation_timer = pygame.USEREVENT + 2
pygame.time.set_timer(book_animation_timer, 200)

peanut_animation_timer = pygame.USEREVENT + 3
pygame.time.set_timer(peanut_animation_timer, 200)

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if game_active:
            if event.type == pygame.MOUSEBUTTONDOWN and player_rect.bottom >= 200:
                # player_gravity = -300
                pass
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom >= 200:
                    pass
                    # player_gravity = -300
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                book_rect.left = 800
                start_time = int(pygame.time.get_ticks() / 1000)

        if game_active:
            if event.type == obstacle_timer:
                item_choice = choice(['book', 'peanut'])
                if item_choice == 'book':
                    book_group.add(Obstacle('book'))
                elif item_choice == 'peanut':
                    peanut_group.add(Obstacle('peanut'))

            if event.type == book_animation_timer:
                if book_index == 0:
                    book_index = 1
                else:
                    book_index = 0
                book_surface = book_frames[book_index]

            if event.type == peanut_animation_timer:
                if peanut_index == 0:
                    peanut_index = 1
                else:
                    peanut_index = 0
                peanut_surface = peanut_frames[peanut_index]

    if game_active:
        screen.blit(background_surface, (0, 0))
        score = display_score()

        player_sprite.draw(screen)
        player_sprite.update()

        book_group.draw(screen)
        book_group.update()
        peanut_group.draw(screen)
        peanut_group.update()

        game_active = collision_sprite()

    else:
        screen.fill((73, 93, 130))
        screen.blit(player_stand, player_stand_rect)
        # obstacle_rect_list.clear()
        player_gravity = 0

        score_message = game_font.render(
            f'Your score: {score}', False, 'Black')
        score_message_rect = score_message.get_rect(center=(400, 350))
        screen.blit(game_name, game_name_rect)

        if score == 0:
            screen.blit(game_message, game_message_rect)
        else:
            screen.blit(score_message, score_message_rect)

    pygame.display.update()
    clock.tick(60)
