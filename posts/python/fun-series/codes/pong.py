import pygame
import random
import sys


def ball_animation():
    global ball_speed_x, ball_speed_y, player_score, opponent_score, score_time

    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1

    if ball.left <= 10:
        player_score += 1
        score_time = pygame.time.get_ticks()

    if ball.right >= screen_width - 10:
        opponent_score += 1
        score_time = pygame.time.get_ticks()

    if ball.colliderect(player):
        ball_speed_x *= -1

        if (player.centery > last_player_y and ball_speed_y < 0) or (
                player.centery < last_player_y and ball_speed_y > 0):
            ball_speed_y *= -1

    if ball.colliderect(opponent):
        ball_speed_x *= -1

        if (opponent.centery >= last_opponent_y and ball_speed_y < 0) or (
                opponent.centery <= last_opponent_y and ball_speed_y > 0):
            ball_speed_y *= -1


def player_animation():
    global last_player_y
    last_player_y = player.centery
    player.centery += player_speed
    if player.top <= 0:
        player.top = 0
    if player.bottom >= screen_height:
        player.bottom = screen_height


def opponent_ai():
    global last_opponent_y
    last_opponent_y = opponent.centery
    if opponent.centery < ball.y:
        opponent.top += opponent_speed
    if opponent.centery > ball.y:
        opponent.bottom -= opponent_speed
    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >= screen_height:
        opponent.bottom = screen_height


def ball_start():
    global ball_speed_x, ball_speed_y, score_time

    current_time = pygame.time.get_ticks()
    ball.center = (screen_width / 2, screen_height / 2)

    if current_time - score_time < 700:
        number_three = game_font.render("3", False, light_gray)
        screen.blit(number_three, (screen_width / 2 - 5, screen_height / 2 + 15))
    if 700 < current_time - score_time < 1400:
        number_three = game_font.render("2", False, light_gray)
        screen.blit(number_three, (screen_width / 2 - 5, screen_height / 2 + 15))
    if 1400 < current_time - score_time < 2100:
        number_three = game_font.render("1", False, light_gray)
        screen.blit(number_three, (screen_width / 2 - 5, screen_height / 2 + 15))

    if current_time - score_time < 2100:
        ball_speed_x, ball_speed_y = 0, 0
    else:
        ball_speed_y = 7 * random.choice((1, -1))
        ball_speed_x = 7 * random.choice((1, -1))
        score_time = None


# General setup
pygame.init()
clock = pygame.time.Clock()

# Setting up the main window
screen_width = 848
screen_height = 565
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Pong')

# Game Rectangles
ball = pygame.Rect(screen_width / 2 - 15, screen_height / 2 - 15, 30, 30)
player = pygame.Rect(screen_width - 20, screen_height / 2 - 70, 10, 140)
opponent = pygame.Rect(10, screen_height / 2 - 70, 10, 140)
last_player_y = player.centery
last_opponent_y = opponent.centery

bg_color = pygame.Color('grey12')
light_gray = (200, 200, 200)

# Game Variables
ball_speed_x = 7 * random.choice((1, -1))
ball_speed_y = 7 * random.choice((1, -1))
player_speed = 0
opponent_speed = 7

# Text Variables
player_score = 0
opponent_score = 0
game_font = pygame.font.Font('FreeSansBold.ttf', 24)

# Score Timer
score_time = True

while True:
    # Handling input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player_speed += 7
            if event.key == pygame.K_UP:
                player_speed -= 7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player_speed -= 7
            if event.key == pygame.K_UP:
                player_speed += 7

    # Game Logic
    player_animation()
    opponent_ai()
    ball_animation()

    # Visuals
    screen.fill(bg_color)
    pygame.draw.rect(screen, light_gray, player)
    pygame.draw.rect(screen, light_gray, opponent)
    pygame.draw.ellipse(screen, light_gray, ball)
    pygame.draw.aaline(screen, light_gray, (screen_width / 2, 0), (screen_width / 2, screen_height))

    if score_time:
        ball_start()

    player_text = game_font.render(f"{player_score}", False, light_gray)
    opponent_text = game_font.render(f"{opponent_score}", False, light_gray)
    screen.blit(player_text, (screen_width / 2 + 20, screen_height / 2 - 3))
    screen.blit(opponent_text, (screen_width / 2 - 30, screen_height / 2 - 3))

    # Updating the window
    pygame.display.flip()
    clock.tick(60)
