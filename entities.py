'''
Created on 07/10/2014

@author: 22491
'''

import pygame, sys, os, math, textwrap
from pygame.locals import *
from random import randrange, randint
import globals, functions

class Entity(pygame.sprite.Sprite):
    def __init__(self, *args):
        pygame.sprite.Sprite.__init__(self, *args)

class player_map(Entity):
    def __init__(self, x, y):
        Entity.__init__(self, globals.group_player)
        globals.player_map = self
        self.currenttile = (x/16, y/16)
        self.desttile = (0,0)
        self.x = x*16.0
        self.y = y*16.0
        self.xvel = 0.0
        self.yvel = 0.0
        self.keydown = {'LEFT':False, 'RIGHT':False, 'UP':False, 'DOWN':False}
        self.key_pressed = False
        self.image = functions.get_image(os.path.join('resources', 'player_map','player_map.bmp'), (255,0,255))
        self.pos = (x,y)
        self.moving = False
        self.rect = pygame.Rect(x, y, 16, 16)
    
    def update(self):
        if not self.moving:
            self.desttile = (0,0)
            if self.keydown['LEFT'] and not self.keydown['RIGHT'] and not self.keydown['UP'] and not self.keydown['DOWN']:
                self.tile = True
                for item in globals.group_unwalkable:
                    if item.rect.collidepoint(self.x - 8, self.y + 8):
                        self.tile = False
                if self.tile: 
                    self.desttile = (math.floor(self.x/16) - 1, math.floor(self.y/16))
                    self.moving = True
                
            if self.keydown['RIGHT'] and not self.keydown['LEFT'] and not self.keydown['UP'] and not self.keydown['DOWN']:
                self.tile = True
                for item in globals.group_unwalkable:
                    if item.rect.collidepoint(self.x + 8 + 16, self.y + 8):
                        self.tile = False
                if self.tile: 
                    self.desttile = (math.floor(self.x/16) + 1, math.floor(self.y/16))
                    self.moving = True
                
            if self.keydown['UP'] and not self.keydown['DOWN'] and not self.keydown['LEFT'] and not self.keydown['RIGHT']:
                    self.tile = True
                    for item in globals.group_unwalkable:
                        if item.rect.collidepoint(self.x + 8, self.y - 8):
                            self.tile = False
                    if self.tile: 
                        self.desttile = (math.floor(self.x/16), math.floor(self.y/16) - 1)
                        self.moving = True
                    
            if self.keydown['DOWN'] and not self.keydown['UP'] and not self.keydown['LEFT'] and not self.keydown['RIGHT']:
                    self.tile = True
                    for item in globals.group_unwalkable:
                        if item.rect.collidepoint(self.x + 8, self.y + 16 + 8):
                            self.tile = False
                            print "DASDADAS"
                    if self.tile: 
                        self.desttile = (math.floor(self.x/16), math.floor(self.y/16) + 1)
                        self.moving = True
        if self.moving:
            self.movelr = True
            self.moveud = True
            if not self.desttile == (0,0):
                if self.desttile[0] > self.currenttile[0]:
                    self.xvel = 2
                elif self.desttile[0] < self.currenttile[0]:
                    self.xvel = -2
                else:
                    if self.x + 8 == self.desttile[0]*16 + 8:
                        self.movelr = False
                        self.xvel = 0.0
                
                if self.desttile[1] > self.currenttile[1]:
                    self.yvel = 2
                elif self.desttile[1] < self.currenttile[1]:
                    self.yvel = -2
                else:
                    if self.y + 8 == self.desttile[1]*16 + 8:
                        self.moveud = False
                        self.yvel = 0.0
            if self.movelr == False and self.moveud == False:
                self.moving = False
        
        self.x += self.xvel
        self.y += self.yvel
        self.pos = (self.x, self.y)
        self.rect.move_ip(self.pos)
        self.currenttile = (math.floor(self.x/16), math.floor(self.y/16))    
    
class walkable_map(Entity):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.pos = (x*16, y*16)
        self.rect = pygame.Rect(self.pos, (16,16))
        self.image = functions.get_image(os.path.join('resources','map_tiles','map_walkable.bmp'), (255,0,255))
        Entity.__init__(self, globals.group_tiles)
    
class water_map(Entity):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.pos = (x*16, y*16)
        self.rect = pygame.Rect(self.pos, (16,16))
        self.image = functions.get_image(os.path.join('resources','map_tiles','map_water.bmp'), (255,0,255))
        Entity.__init__(self, globals.group_tiles, globals.group_unwalkable)
        
class mountain_map(Entity):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.pos = (x*16, y*16)
        self.rect = pygame.Rect(self.pos, (16,16))
        self.image = functions.get_image(os.path.join('resources','map_tiles','map_mountain.bmp'), (255,0,255))
        Entity.__init__(self, globals.group_tiles, globals.group_unwalkable)


    