#   poprawic wyjezdzanie za ekran

import pygame
import sys
import random
from options import Option

pygame.init()

# variables
score = 0
i = 0
k = 0
screen_width = 800
screen_height = 720
left_rand = random.randint(50, 700)
right_rand = random.randint(50, 700)
time_left = 60
clock = pygame.time.Clock()

screen = pygame.display.set_mode((screen_width, screen_height))
square = pygame.Rect(10, 35, 50, 50)  # left, top, width, height

square2 = pygame.Rect(left_rand, right_rand, 25, 25)
background_image = pygame.image.load('images/pic1.jpg')
myFont = pygame.font.SysFont(None, 40)
pygame.display.set_caption("Funny square")

start = 3600


# Intro
def game_intro():
    intro = True
    animation = pygame.Rect(0, 0, 50, 50)
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
        if animation.x > 800 & animation.y > 800:
            animation.x += 0
            animation.y += 0
            animation.width += 0
        else:
            animation.x += 1
            animation.y += 1
            animation.width += 1

        options = [Option("1.Start game", (100, 450), screen),  Option("2.Exit game", (100, 500), screen)]  # x y

        for option in options:
            if option.rect.collidepoint(pygame.mouse.get_pos()):
                option.cover = True
            else:
                option.cover = False
            option.draw(screen)

        # Choose option by mouse
        if options[0].rect.collidepoint(pygame.mouse.get_pos()) & pygame.mouse.get_pressed()[0]:
            break
        if options[1].rect.collidepoint(pygame.mouse.get_pos()) & pygame.mouse.get_pressed()[0]:
            sys.exit(0)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_1]:
            break
        if keys[pygame.K_2]:
            sys.exit(0)
        pygame.draw.rect(screen, (120, 0, 0), animation)

        pygame.event.pump()
        pygame.display.flip()
        pygame.display.update()
        clock.tick(200)


game_intro()

while True:

    # Handle event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)

    # Time counting
    time_left = int(start / 60)
    start -= 1

    # Movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_d] | keys[pygame.K_RIGHT]:
        if square.x >= 750:
            square.x += 0
        else:
            square.x += 6
    if keys[pygame.K_s] | keys[pygame.K_DOWN]:
        if square.y > 665:
            square.y += 0
        else:
            square.y += 6
    if keys[pygame.K_w] | keys[pygame.K_UP]:
        if square.y < 10:
            square.y -= 0
        else:
            square.y -= 6
    if keys[pygame.K_a] | keys[pygame.K_LEFT]:
        if square.x <= 0:
            square.x -= 0
        else:
            square.x -= 6

    # Collision
    if pygame.Rect.colliderect(square, square2):
        score += 1
        new_left_rand = random.randint(20, 700)
        new_right_rand = random.randint(20, 700)
        square2 = pygame.Rect(new_left_rand, new_right_rand, 25, 25)

    # Score events
    if i <= 0:
        if score == 10:
            background_image = pygame.image.load('images/pic2.png')
            i += 1
            k -= 1
    if k <= 0:
        if score == 25:
            background_image = pygame.image.load('images/pic3.jpg')
            k += 1

    if start == 0:
        screen.fill((0, 0, 0))
        game_intro()

    # Drawing MAIN
    screen.blit(background_image, [0, 0])
    label = myFont.render("Your score: {}".format(score), 1, (6, 25, 45))
    label2 = myFont.render("Time left: {}".format(time_left), 1, (6, 25, 45))
    screen.blit(label, (10, 10))  # y - x
    screen.blit(label2, (630, 10))  # 630
    pygame.draw.rect(screen, (120, 0, 0), square)
    pygame.draw.rect(screen, (231, 215, 0), square2)
    pygame.display.flip()
    clock.tick(60)
