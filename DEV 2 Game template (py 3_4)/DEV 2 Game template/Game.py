import time
from threading import Thread
import os, pygame
import time
from Tile import *
from Node import *

pygame.init()
size = width, height = 600, 600
white = 255, 255, 255
green = 50, 255, 100
screen = pygame.display.set_mode(size)
offset = 30
board_size = 10
car_texture = pygame.image.load("Content\car.png").convert()
entry_tile = build_square_matrix(board_size, offset)

# Create cars
car_list = Empty
car_list = Node(Car(entry_tile.Position.X, entry_tile.Position.Y), car_list)

def Update(car_list, count):
 
  if count % 5 == 0:
      car_list = Node(Car(entry_tile.Position.X, entry_tile.Position.Y), car_list)

  # Make the cars move around    
  if not (car_list.IsEmpty):
      
      if(entry_tile.Traverseable):
          car_list.Value.PosX += entry_tile.Position.X + 1

  #TODO: add the logic of your cars here
  #HINT For filtering reasons we return a list (of cars?)
  return car_list


def Draw(car_list):
#TODO: add the draw of your cars below
#
# Use the following code to draw your car. 
# HINT: POSITION_X and POSITION_Y represent the position of the car to draw on the screen
#
  _width = int(offset / 3)
  screen.blit(pygame.transform.scale(car_texture, (_width, _width)), 
                (_width + car_list.Value.PosX * offset, 
                _width + car_list.Value.PosY * offset))
  print(car_list.Value.PosX)
  print("<3")



def Main():
  start = time.time()
  cars = Empty
  count = 0

  while True:
    pygame.event.wait()    
    screen.fill(green)  
    entry_tile.Reset()
    entry_tile.Draw(screen)

    count += 1
    cars = Update(car_list, count)
    Draw(cars)

    pygame.display.flip()
    time.sleep(1)
    
Main()