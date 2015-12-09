import pygame
import time
from pygame.locals import *
from List import *
from Car import *

pygame.init()
quit = False
game_screen = pygame.display.set_mode((500, 500))
game_screen.fill((255, 255, 255))
car_image = pygame.image.load("sprites/car.png")
sample_car = Car("Andy's Car", 5, 20, 20, car_image)
clock = pygame.time.Clock()
count = 0
car_list = Empty()

while not quit:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            done = True

    #sample_car.PosX += sample_car.Speed
    #sample_car.PosY += sample_car.Speed

    count += 1
    game_screen.fill((255, 255, 255))
        
    if(count % 5 == 0):
        car_list = Node(Car("Car", 5, 10, 10, car_image), car_list)
        game_screen.blit(car_image, (car_list.Value.PosX, car_list.Value.PosY))

    #Give the illusion of skiping a frame
    #game_screen.fill((255, 255, 255))
    #game_screen.blit(sample_car.Sprite, (sample_car.PosX, sample_car.PosY))

    pygame.display.flip()
    clock.tick(60)