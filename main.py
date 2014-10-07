'''
Created on Sep 10, 2013

@author: Dean, God Almighty of Sex
'''
import pygame
from pygame.sprite import Sprite
import os, math, random, globals, functions, entities, maps

pygame.init()
pygame.display.set_caption('RPG Test')
screen = pygame.display.set_mode((480,480))
done = False
clock = pygame.time.Clock()
clockcounter = 0
one = entities.player_map(1,1)
maps.load_map(maps.setmap_world_map(0, 0))

while not done:
    key_pressed = pygame.key.get_pressed()
    if key_pressed[pygame.K_LEFT]:
        globals.player_map.keydown['LEFT'] = True
        globals.player_map.key_pressed = True
    else: globals.player_map.keydown['LEFT'] = False
    if key_pressed[pygame.K_RIGHT]:
        globals.player_map.keydown['RIGHT'] = True
        globals.player_map.key_pressed = True
    else: globals.player_map.keydown['RIGHT'] = False
    if key_pressed[pygame.K_UP]:
        globals.player_map.keydown['UP'] = True
        globals.player_map.key_pressed = True
    else: globals.player_map.keydown['UP'] = False
    if key_pressed[pygame.K_DOWN]:
        globals.player_map.keydown['DOWN'] = True
        globals.player_map.key_pressed = True
    else: globals.player_map.keydown['DOWN'] = False
             
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE: done = True

    for item in globals.group_player:
        item.update()


    screen.fill((0,0,0)) #wipe the screen
    for item in globals.group_tiles:
        screen.blit(item.image, item.pos)
    for item in globals.group_player:
        screen.blit(item.image, item.pos)
  
    pygame.display.flip()
    clockcounter += 1
    clock.tick(30)
    

