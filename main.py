#Name: Ajay Saini
import pygame
import random

from pygame import draw
from pygame.constants import MOUSEBUTTONDOWN

width, height = 800, 600
pygame.display.set_caption("Catch the Falling Objects")
pygame.init()
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
paddle_width, paddle_height = 100, 20
pad_x, pad_y = 350, 560
paddle_speed = 8
obj_width, obj_height = 50, 50
object_x = random.randint(0, width - obj_width)
object_y = 0
object_speed = 5
GameState = "Main"
start_screen = pygame.image.load("starting.jpg")
start_screen = pygame.transform.scale(start_screen, (width, height))
lives = 3
score = 0
hp = pygame.image.load("hp.png")
hp = pygame.transform.scale(hp, (50, 50))
game_over = pygame.image.load("game_over.webp")
game_over = pygame.transform.scale(game_over, (width, height))


def key_input():
  global pad_x
  if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
    pad_x = pad_x - paddle_speed
  if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
    pad_x = pad_x + paddle_speed


def main():
  screen.fill((255, 255, 255))


def lose_con(screen, x, y, lives, image):
  for i in range(lives):
    hp_rect = hp.get_rect()
    hp_rect.x = x + 30 * i
    hp_rect.y = y
    screen.blit(hp, hp_rect)


def drawings():
  pygame.draw.rect(screen, (0, 0, 0),
                   (pad_x, pad_y, paddle_width, paddle_height))
  pygame.draw.rect(screen, (255, 0, 0),
                   (object_x, object_y, obj_width, obj_height))


def collision():
  global object_x, object_y, score
  object_rect = pygame.Rect(object_x, object_y, obj_width, obj_height)
  pad_rect = pygame.Rect(pad_x, pad_y, paddle_width, paddle_height)
  if object_rect.colliderect(pad_rect):
    object_x = random.randint(0, width - obj_width)
    object_y = 0
    score = score + 1


def unbound():
  global object_x, object_y, lives
  if object_y > height:
    object_x = random.randint(0, width - obj_width)
    object_y = 0
    lives = lives - 1

  if lives < 1:
    screen.blit(game_over, (0, 0))


def score_on_screen():
  global score
  score_font = pygame.font.SysFont("Arial", 50)
  score_txt = score_font.render(f"Score: {score}", True, (0, 0, 0))
  screen.blit(score_txt, (300, 15))


text = pygame.font.SysFont("Arial", 50)
text_render = text.render("Press Start", True, (255, 255, 255), (17, 20, 20))
text_rect = text_render.get_rect(center=(455, 420))

clock = pygame.time.Clock()
while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
    if event.type == MOUSEBUTTONDOWN:
      pos = pygame.mouse.get_pos()
      if text_rect.collidepoint(event.pos):
        GameState = "Press Start"
  if score > 10:
    object_speed = 10
    paddle_speed = 11
  elif score > 20:
    object_speed = 11
    paddle_speed = 12
  elif score > 30:
    object_speed = 12
    paddle_speed = 13
  else:
    object_speed = 8
    paddle_speed = 8

  if GameState == "Main":
    screen.blit(start_screen, (0, 0))
    screen.blit(text_render, text_rect)
  elif GameState == "Press Start":
    object_y = object_y + object_speed
    main()
    drawings()
    score_on_screen()
    key_input()
    unbound()
    collision()
    lose_con(screen, 5, 20, lives, hp)

  pygame.display.update()
  clock.tick(60)
