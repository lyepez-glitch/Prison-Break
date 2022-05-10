from shutil import move
from tkinter import Y
import pygame
from sys import exit
import time
from pygame import Color
player_height = 35
width = 330
height = 50
new_game = False





pygame.init()

game_is_running = True
guard_1_position = 645





  # screen = pygame.display.set_mode((800,400))
  # pygame.display.set_caption('Jail Break')
  # clock = pygame.time.Clock()




  # score_rectangle = score_surface.get_rect(center = (70,50))


def start_game():
    screen = pygame.display.set_mode((800,400))
    pygame.display.set_caption('Jail Break')
    clock = pygame.time.Clock()
    test_font = pygame.font.Font('arial1.ttf', 25)
  # prison_surface = pygame.Surface((700, 350))
    prison_surface = pygame.image.load('graphics/prison.png')
    prison_surface = pygame.transform.scale(prison_surface, (360,360))

      # score_surface = test_font.render('Health',False,'White')
      # score_surface = pygame.transform.scale(score_surface, (30,30))
    end_surface = test_font.render('End',False,'Black')
    end_surface = pygame.transform.scale(end_surface, (30,30))


      # text_background_surface = pygame.Surface((150, 80))
      # text_background_surface.fill('Yellow')
    ground_surface = pygame.image.load('graphics/ground.jpeg').convert_alpha()
    ground_surface = pygame.transform.scale(ground_surface, (800,800))
      # text_surface = test_font.render('Jail Break', False, 'Black')
    guard_surface = pygame.image.load('graphics/guard1.png').convert_alpha()
    guard_2_surface = pygame.image.load('graphics/guard1.png').convert_alpha()

    end_rectangle = end_surface.get_rect(center = (675,350))
    guard_rectangle = guard_surface.get_rect(topleft = (guard_1_position,player_height + 10))
    guard_rectangle_2 = guard_2_surface.get_rect(topleft = (75,315))

    full_heart = pygame.image.load('graphics/full_heart.png').convert_alpha()
    half_heart = pygame.image.load('graphics/half_heart.png').convert_alpha()
    empty_heart = pygame.image.load('graphics/empty_heart.png').convert_alpha()

    class Player(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__()
        self.image = pygame.image.load('graphics/player.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (40,40))
        self.player_width = 70
        self.player_height = 35
        self.rect = self.image.get_rect(topleft = (self.player_width,self.player_height))
        self.width = 330
        self.height = 50
        self.health = 5
        self.max_health = 10
        self.move_to_diagonal = 'n'
        self.move_to_right = 'n'
        self.move_to_left = 'n'
        self.move_to_down = 'n'
        self.move_to_up = 'n'

      def get_damage(self):
        if self.health > 0:
          self.health -= 1
          self.rect.y += 50
        elif self.health == 0:
          print('You\'re dead')
          print('press "r" to start a new game')

          self.kill()

      def get_health(self):
        if(self.health < self.max_health):
          self.health += 1

      def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
          self.move_left()
        elif keys[pygame.K_RIGHT]:
          self.move_right()
        elif keys[pygame.K_UP]:
          self.move_up()
        elif keys[pygame.K_DOWN]:
          self.move_down()
        elif keys[pygame.K_k]:
          self.move_diagonal()


      def diagonal_Out_Of_Bounds(self):
        if(self.rect.x >= 700 or self.rect.y >= 340):
          return True
        return False

      def up_Out_Of_Bounds(self):
        if(self.rect.y <= 45):
          return True
        return False

      def down_Out_Of_Bounds(self):
        if(self.rect.y >= 300):
          return True
        return False

      def right_Out_Of_Bounds(self):
        if(self.rect.x >= 630):
          return True
        return False

      def left_Out_Of_Bounds(self):
        if(self.rect.x <= 100):
          return True
        return False


      def move_diagonal(self):
        if(not self.diagonal_Out_Of_Bounds()):
          self.player_width += 29
          self.player_height += 12
          self.rect.x+= 5
          self.rect.y += 3
        else:
          pass

      def move_right(self):
        if(not self.right_Out_Of_Bounds()):
          self.rect.x += 5
        else:
          pass

      def move_left(self):
        if(not self.left_Out_Of_Bounds()):
          self.rect.x -= 5

      def move_down(self):
        if(not self.down_Out_Of_Bounds()):
          self.rect.y += 5

      def move_up(self):
        if(not self.up_Out_Of_Bounds()):
          self.rect.y -= 5

      def detect_collision(self):
        if(self.rect.colliderect(end_rectangle)):
          self.rect.y += 50
          print('You have won the game')
          print('Thanks for playing!')
          print('Press "r" to start a new game')


      def full_hearts(self):
        for heart in range(self.health):
          screen.blit(full_heart, ((heart * 50)+ 10,10))

      def empty_hearts(self):
        pass

      def update(self):
        self.detect_collision()
        self.player_input()
        self.full_hearts()

    player= pygame.sprite.GroupSingle()
    player.add(Player())

    while game_is_running:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()
          exit()
        if(event.type == pygame.KEYDOWN):
          if(event.key == pygame.K_r):
            start_game()
            # pygame.quit()
            # exit()


      # if(player.sprite.rect.colliderect(guard_rectangle) or player.sprite.rect.colliderect(guard_rectangle_2)):
      #   player.sprite.get_damage()
      #   print('health',player.sprite.health)


      if(player):
        if(guard_rectangle.colliderect(player.sprite.rect) or guard_rectangle_2.colliderect(player.sprite.rect)):
          player.sprite.get_damage()

      screen.blit(ground_surface,(0,0))
      screen.blit(prison_surface,(70,25))
      screen.blit(prison_surface,(360,30))
      player.draw(screen)
      # player.update()
      screen.blit(guard_surface, guard_rectangle)
      screen.blit(guard_2_surface, guard_rectangle_2)


      if(guard_rectangle.x >= 50):
        guard_rectangle.x -= 10

      if(guard_rectangle_2.y >= 50):
        guard_rectangle_2.y -= .5


      # text_background_surface.blit(text_surface,(20,10))
      # screen.blit(text_background_surface,(325,5))
      # pygame.draw.rect(text_background_surface, 'Red', score_rectangle)
      # pygame.draw.rect(text_background_surface, 'Red', score_rectangle, 10)
      pygame.draw.rect(screen, 'Red', end_rectangle)
      # text_background_surface.blit(score_surface,score_rectangle)
      screen.blit(end_surface,end_rectangle)
      player.update()

      pygame.display.update()
      clock.tick(60)

print('Welcome to Jail Break')
print()

new_game = input('do you want to play? Enter "y" for yes')

while(new_game.lower() != 'y'):
  print('That is not a valid response')
  new_game = input('do you want to play? Enter "y" for yes')


def main():
  if(new_game == "y"):
    print('The goal of the game is to get to the square marked "End" without getting killed by enemies')
    print('Your health bar is shown in the middle')
    print('Every time you collide with an enemy, you lose a health point')
    print('You can avoid enemies by using the following arrow keys:')
    print('press the left arrow to move your character left')
    print('press the right arrow to move your character right')
    print('press the down arrow to move your character straight down')
    print('press the up arrow to move your character straight up')
    print('Press "k" to move diagonally')
    print('Press "r" at any time to start a new game')
    print('Loading...')


  start = input('enter "y" when ready to begin')
  start = start.lower()

  while(start != 'y'):
    start = input('enter "y" when ready to begin')
    start = start.lower()
  if(start == 'y'):
    start_game()

  print('Good Luck!')
  # play_again = inpupt('do you want to play again?')

main()



