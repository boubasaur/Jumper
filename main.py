from random import randint, choice
import pygame
from sys import exit

from player import *
from obstacles import *

def display_score():
    global score
    score_surface = game_font.render(f'Score: {score}', False, (73, 93, 130))
    score_rect = score_surface.get_rect(center=(400, 150))
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

player_stand = pygame.image.load('graphics/player/stand.png').convert_alpha()
player_stand = pygame.transform.scale(player_stand, (200, 200))
player_stand_rect = player_stand.get_rect(center=(400, 200))

peanut_1 = pygame.image.load('graphics/Peanut.png').convert_alpha()
peanut_2 = pygame.image.load('graphics/Peanut2.png').convert_alpha()
peanut_1 = pygame.transform.scale(peanut_1, (50, 50))
peanut_2 = pygame.transform.scale(peanut_2, (50, 50))

book_1 = pygame.image.load('graphics/Book.png').convert_alpha()
book_2 = pygame.image.load('graphics/Book2.png').convert_alpha()
book_1 = pygame.transform.scale(book_1, (50, 50))
book_2 = pygame.transform.scale(book_2, (50, 50))

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

        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            game_active = True

        if game_active:
            if event.type == obstacle_timer:
                item_choice = choice(['book', 'peanut'])
                if item_choice == 'book':
                    book_group.add(Obstacle(book_1, book_2))
                elif item_choice == 'peanut':
                    peanut_group.add(Obstacle(peanut_1, peanut_2))

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
        player_gravity = 0

        score_message = game_font.render(f'Your score: {score}', False, 'Black')
        score_message_rect = score_message.get_rect(center=(400, 350))
        screen.blit(game_name, game_name_rect)

        if score == 0:
            screen.blit(game_message, game_message_rect)
        else:
            screen.blit(score_message, score_message_rect)

    pygame.display.update()
    clock.tick(60)
