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
print(entry_tile)
# Create cars
car_list = Empty
car_list = Node(Car(entry_tile), car_list)

def Update(car_list):

  driving_cars = Empty

  while not car_list.IsEmpty:
      driving_cars = Node(car_list, driving_cars)

  return driving_cars

def Draw(car_list):
#TODO: add the draw of your cars below
#
# Use the following code to draw your car. 
# HINT: POSITION_X and POSITION_Y represent the position of the car to draw on the screen
#
  _width = int(offset / 3)
  screen.blit(pygame.transform.scale(car_texture, (_width, _width)), 
                (_width + car_list.Value.Position.X * offset, 
                _width + car_list.Value.Position.Y * offset))
  print("<3")
  print(car_list.Value.Position.X)
  print(car_list.Value.Position.Y)



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
    cars = Update(car_list)
    Draw(cars)

    pygame.display.flip()
    time.sleep(1)
    
Main()